"""
TikTok Shop Order Events — Production-Grade Python ETL Pipeline
----------------------------------------------------------------
This script demonstrates an end-to-end Python ETL pipeline implementing:
1. Extract   : Reading raw order payload events from a CSV input file
2. Transform : Schema enforcement, timestamp normalization, business metrics (net amount), deduplication
3. Validate  : Data Quality (DQ) checks (null checks, range validation)
4. Load      : Idempotent Upsert (Merge) into target Data Warehouse storage
"""

import csv
import json
import os
from datetime import datetime, timezone
from typing import Dict, List, Any, Tuple


# ==========================================
# 1. EXTRACT STEP
# ==========================================
def extract_raw_events(csv_filepath: str) -> List[Dict[str, Any]]:
    """Reads raw order payload events from a CSV file into a list of dictionaries using csv.DictReader."""
    if not os.path.exists(csv_filepath):
        raise FileNotFoundError(f"Input CSV file not found at path: {csv_filepath}")

    records = []
    with open(csv_filepath, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            records.append(dict(row))
            
    return records


# ==========================================
# 2. TRANSFORM STEP
# ==========================================
def transform_events(raw_records: List[Dict[str, Any]]) -> Tuple[List[Dict[str, Any]], List[Dict[str, Any]]]:
    """
    Cleans, enriches, deduplicates, and calculates business metrics.
    Returns:
        valid_records: List of transformed records
        dead_letter_queue: List of invalid/corrupt records with error reasons
    """
    valid_records = []
    dead_letter_queue = []
    
    # Map to track latest state per order_id for deduplication
    latest_orders: Dict[str, Dict[str, Any]] = {}

    for record in raw_records:
        # Schema Validation: Check required non-empty string fields
        required_fields = ["order_id", "buyer_id", "seller_id", "gross_amount", "status", "timestamp"]
        missing_fields = [field for field in required_fields if not record.get(field) or str(record.get(field)).strip() == ""]
        if missing_fields:
            dead_letter_queue.append({
                "record": record,
                "error": f"Missing or empty required fields: {missing_fields}"
            })
            continue

        try:
            # Data Type Conversions & Metrics Calculation
            gross = float(record["gross_amount"])
            discount = float(record.get("discount_amount") or "0.00")
            net_amount = round(gross - discount, 2)
            
            # Timestamp parsing
            parsed_dt = datetime.strptime(record["timestamp"].strip(), "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)
            
            transformed_record = {
                "order_id": str(record["order_id"]).strip(),
                "buyer_id": str(record["buyer_id"]).strip(),
                "seller_id": str(record["seller_id"]).strip(),
                "item_id": str(record.get("item_id", "UNKNOWN")).strip(),
                "gross_amount": gross,
                "discount_amount": discount,
                "net_amount": net_amount,
                "status": str(record["status"]).strip().upper(),
                "event_timestamp": parsed_dt,
                "processed_at": datetime.now(timezone.utc)
            }

            # Deduplication Logic (Keep record with latest timestamp)
            existing = latest_orders.get(transformed_record["order_id"])
            if not existing or transformed_record["event_timestamp"] > existing["event_timestamp"]:
                latest_orders[transformed_record["order_id"]] = transformed_record

        except ValueError as e:
            dead_letter_queue.append({
                "record": record,
                "error": f"Type conversion failure: {str(e)}"
            })

    valid_records = list(latest_orders.values())
    return valid_records, dead_letter_queue


# ==========================================
# 3. DATA QUALITY (DQ) VALIDATION STEP
# ==========================================
def validate_data_quality(records: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Runs data quality sanity checks before loading into warehouse."""
    passed_records = []
    for record in records:
        # DQ Check 1: Non-negative amounts
        if record["net_amount"] < 0 or record["gross_amount"] < 0:
            print(f"⚠️ [DQ Alert] Negative amount (${record['gross_amount']}) detected for order {record['order_id']}. Dropping record.")
            continue
        
        # DQ Check 2: Valid Status enum
        valid_statuses = {"CREATED", "PAID", "CANCELLED", "REFUNDED", "SHIPPED"}
        if record["status"] not in valid_statuses:
            print(f"⚠️ [DQ Alert] Unknown status '{record['status']}' for order {record['order_id']}. Dropping record.")
            continue
            
        passed_records.append(record)
    return passed_records


# ==========================================
# 4. LOAD STEP (Idempotent Storage Simulation)
# ==========================================
class TargetDataWarehouse:
    """Simulates a target relational Data Warehouse table with Upsert capability."""
    def __init__(self):
        self.table: Dict[str, Dict[str, Any]] = {}

    def upsert(self, records: List[Dict[str, Any]]):
        """Idempotently merges records based on Primary Key (order_id)."""
        inserted_count = 0
        updated_count = 0
        
        for rec in records:
            order_id = rec["order_id"]
            if order_id in self.table:
                self.table[order_id] = rec
                updated_count += 1
            else:
                self.table[order_id] = rec
                inserted_count += 1
                
        print(f"✅ [Load Complete] Inserts: {inserted_count} | Updates (UPSERT): {updated_count} | Warehouse Total Rows: {len(self.table)}")

    def display_contents(self):
        print("\n--- 📊 Target Warehouse Table: fact_order_item ---")
        for order_id, data in self.table.items():
            dt_str = data["event_timestamp"].strftime("%Y-%m-%d %H:%M:%S")
            print(f"Order: {order_id} | Buyer: {data['buyer_id']} | Seller: {data['seller_id']} | "
                  f"Net GMV: ${data['net_amount']:.2f} | Status: {data['status']} | EventTime: {dt_str}")


# ==========================================
# 5. PIPELINE ORCHESTRATOR
# ==========================================
def run_etl_pipeline(csv_path: str):
    print(f"🚀 Starting TikTok Shop Order ETL Pipeline for source file: {csv_path}...")
    
    # 1. Extract
    raw_data = extract_raw_events(csv_path)
    print(f"📥 [Extract] Successfully read {len(raw_data)} rows from CSV.")

    # 2. Transform
    valid_data, dlq = transform_events(raw_data)
    print(f"⚙️  [Transform] Valid deduplicated records: {len(valid_data)} | Sent to Dead-Letter Queue (DLQ): {len(dlq)}")
    if dlq:
        for idx, item in enumerate(dlq, 1):
            print(f"   --> [DLQ #{idx}] Error: {item['error']} | Record: {item['record']}")

    # 3. Quality Assurance
    clean_data = validate_data_quality(valid_data)

    # 4. Load
    dw = TargetDataWarehouse()
    dw.upsert(clean_data)
    dw.display_contents()


if __name__ == "__main__":
    # Path relative to script location
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_csv = os.path.join(script_dir, "raw_order_events.csv")
    run_etl_pipeline(input_csv)
