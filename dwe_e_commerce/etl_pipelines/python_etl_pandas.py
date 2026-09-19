"""
TikTok Shop Order Events — Pandas-Based Python ETL Pipeline
------------------------------------------------------------
Demonstrates vectorized ETL transformations using Pandas:
1. Extract   : pd.read_csv()
2. Transform : Type conversion, vector arithmetic (net_amount), deduplication via groupby/sort
3. Validate  : Data Quality (DQ) filtering & Dead-Letter Queue (DLQ) separation
4. Load      : Storage / Warehouse payload export
"""

import os
import pandas as pd
import numpy as np


def run_pandas_etl(csv_filepath: str):
    print(f"🚀 Starting Pandas ETL Pipeline for: {csv_filepath}\n")

    # ==========================================
    # 1. EXTRACT
    # ==========================================
    if not os.path.exists(csv_filepath):
        raise FileNotFoundError(f"Source file missing: {csv_filepath}")
        
    df_raw = pd.read_csv(csv_filepath, dtype=str)
    print(f"📥 [Extract] Raw rows read: {len(df_raw)}")

    # ==========================================
    # 2. TRANSFORM & VALIDATE SCHEMA (DLQ Separation)
    # ==========================================
    required_cols = ["order_id", "buyer_id", "seller_id", "gross_amount", "status", "timestamp"]
    
    # Identify rows with missing/null required values
    is_missing = df_raw[required_cols].isna().any(axis=1) | (df_raw[required_cols] == "").any(axis=1)
    
    dlq_missing = df_raw[is_missing].copy()
    dlq_missing["error_reason"] = "Missing required fields"
    
    df_valid = df_raw[~is_missing].copy()

    # Data Type Conversions & Cleaning
    df_valid["gross_amount"] = pd.to_numeric(df_valid["gross_amount"], errors="coerce")
    df_valid["discount_amount"] = pd.to_numeric(df_valid["discount_amount"].fillna("0.00"), errors="coerce").fillna(0.0)
    df_valid["timestamp"] = pd.to_datetime(df_valid["timestamp"], errors="coerce", utc=True)
    df_valid["status"] = df_valid["status"].str.strip().str.upper()

    # Check for type conversion failures
    is_corrupt_type = df_valid["gross_amount"].isna() | df_valid["timestamp"].isna()
    dlq_corrupt = df_valid[is_corrupt_type].copy()
    dlq_corrupt["error_reason"] = "Type conversion failure"

    df_valid = df_valid[~is_corrupt_type].copy()

    # Vectorized Metric Calculation: net_amount = gross_amount - discount_amount
    df_valid["net_amount"] = (df_valid["gross_amount"] - df_valid["discount_amount"]).round(2)

    # ==========================================
    # 3. DATA QUALITY (DQ) FILTERING
    # ==========================================
    valid_statuses = ["CREATED", "PAID", "CANCELLED", "REFUNDED", "SHIPPED"]
    
    dq_failed = (df_valid["net_amount"] < 0) | (~df_valid["status"].isin(valid_statuses))
    dlq_dq = df_valid[dq_failed].copy()
    dlq_dq["error_reason"] = "Data quality rule violation (negative amount or invalid status)"

    df_clean = df_valid[~dq_failed].copy()

    # Combine Dead-Letter Queue (DLQ)
    dlq_full = pd.concat([dlq_missing, dlq_corrupt, dlq_dq], ignore_index=True)

    # ==========================================
    # 4. DEDUPLICATION (Keep Latest Status per Order)
    # ==========================================
    # Sort by order_id and timestamp, then keep the last record per order_id
    df_deduped = (
        df_clean
        .sort_values(by=["order_id", "timestamp"])
        .groupby("order_id", as_index=False)
        .last()
    )

    # ==========================================
    # 5. LOAD / SUMMARY REPORT
    # ==========================================
    print(f"⚙️  [Transform & DQ Summary]")
    print(f"   - Raw Records: {len(df_raw)}")
    print(f"   - Dead-Letter Queue (DLQ): {len(dlq_full)} records")
    print(f"   - Deduplicated Final Warehouse Rows: {len(df_deduped)}")

    if not dlq_full.empty:
        print("\n⚠️ [Dead-Letter Queue Sample]")
        print(dlq_full[["event_id", "order_id", "error_reason"]])

    print("\n✅ [Final Warehouse Table Output: fact_order_item]")
    output_cols = ["order_id", "buyer_id", "seller_id", "item_id", "gross_amount", "discount_amount", "net_amount", "status", "timestamp"]
    print(df_deduped[output_cols].to_string(index=False))

    return df_deduped, dlq_full


if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    csv_file = os.path.join(script_dir, "raw_order_events.csv")
    print
    run_pandas_etl(csv_file)
