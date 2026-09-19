# Python ETL Pipelines — TikTok Data Warehouse Engineer Interview Guide

## ❓ Will They Ask Me ETL Pipeline Questions in the Interview?

**YES, absolutely.** In fact, developing, maintaining, and optimizing ETL jobs is explicitly listed as a primary responsibility for this TikTok Data Warehouse Engineer (Data Platform, Global E-Commerce) role.

Interviewers (both Senior Peer/Mentor and Hiring Manager) test ETL in two distinct ways:

### 1. Live Python Coding / Scripting (Hands-On Implementation)
- You may be asked to write a Python script that takes a list of raw event dictionaries/JSON payloads or CSV data, processes them, calculates business metrics, handles missing/malformed records, and returns clean deduplicated records ready for database insertion.

### 2. Architectural & System Design Q&A (Design & Trade-Offs)
- *"How do you make sure an ETL job is idempotent so re-running it doesn't double-count GMV?"*
- *"What happens if source schema changes or corrupt records enter the pipeline?"*
- *"How do you handle late-arriving events in batch vs. streaming ETL?"*

---

## ⚖️ Pure Python vs. Pandas: Which Should You Use in the Interview?

| Feature | Pure Python (`csv.DictReader` / Dicts) | Pandas (`pd.DataFrame`) |
| :--- | :--- | :--- |
| **Interview Availability** | Available everywhere (no dependencies) | Usually available in DE interviews, but check first |
| **Code Length** | ~100 lines (explicit loops, type parsing) | ~25 lines (vectorized arithmetic, `groupby().last()`) |
| **Deduplication** | Dict tracking (`if event_ts > existing_ts`) | `df.sort_values().groupby().last()` |
| **Data Quality / DLQ** | Explicit `if/else` checks per record | Boolean indexing (`df[df['col'].isna()]`) |
| **Memory Scalability** | Low memory footprint with generators | High memory overhead (loads full dataset into RAM) |

### 💡 Interview Pro-Tip:
1. **Always ask the interviewer first**: *"Would you prefer I use Pandas for vectorization, or write standard Python data structures?"*
2. **If Pandas is allowed**: Use Pandas! It shows data manipulation maturity and takes 1/4th the time to write.
3. **If standard Python is requested**: Use `csv.DictReader`, dictionaries, and `datetime` objects.

---

## 🏗️ The 4 Pillars of a Production-Grade Python ETL

```
┌──────────┐     ┌───────────┐     ┌─────────────┐     ┌──────────┐
│ EXTRACT  │ ──> │ TRANSFORM │ ──> │ DATA QUALITY│ ──> │   LOAD   │
│ (Raw CSV/│     │(Clean/    │     │ (DQ Checks/ │     │(Idempotent│
│ S3/Kafka)│     │ Dedup/Net)│     │  DLQ Route) │     │  UPSERT) │
└──────────┘     └───────────┘     └─────────────┘     └──────────┘
```

---

## 💻 Practice Implementations in This Directory

- 📄 **[python_etl_pandas.py](file:///Users/yangxu/code/tiktok/dwe_e_commerce/etl_pipelines/python_etl_pandas.py)**  
  *(Recommended)* Vectorized Pandas ETL pipeline using `pd.read_csv`, `groupby().last()`, and boolean DLQ filtering.
  
- 📄 **[python_etl_pipeline.py](file:///Users/yangxu/code/tiktok/dwe_e_commerce/etl_pipelines/python_etl_pipeline.py)**  
  Standard Python library ETL pipeline using `csv.DictReader`, explicit loops, and dictionary-based deduplication.

- 📄 **[raw_order_events.csv](file:///Users/yangxu/code/tiktok/dwe_e_commerce/etl_pipelines/raw_order_events.csv)**  
  Source CSV landing data.

---

## 🎯 Top 5 Interview Follow-Up Questions & Best Responses

### Q1: "How do you make your Python ETL idempotent?"
> **Response**: *"I make pipelines idempotent by structuring the load phase as an UPSERT (or SQL `MERGE INTO`), keyed on the natural business key like `order_id`. Additionally, for partition-based batch jobs, I use atomic overwrites (`INSERT OVERWRITE PARTITION`) so re-executing a daily backfill completely replaces that specific partition rather than appending duplicates."*

### Q2: "What if a file contains 10 million rows and doesn't fit into RAM?"
> **Response**: *"In Pandas, loading a multi-gigabyte CSV into memory causes Out-Of-Memory (OOM) errors. I would process the file in chunks using `pd.read_csv(..., chunksize=100000)`, or switch to **Apache Spark** DataFrames for distributed batch execution."*

### Q3: "How do you handle late-arriving events (e.g., a refund event for an order created 3 days ago)?"
> **Response**: *"In batch ETL, late-arriving events update the dimensional status via Slowly Changing Dimensions (SCD Type 2) or trigger a targeted partition overwrite. In real-time streaming, watermarks are defined to allow a specified latency window for late events before updating state tables."*

### Q4: "What is a Dead-Letter Queue (DLQ)?"
> **Response**: *"A DLQ is a secondary storage location (like an S3 bucket or Kafka topic) where records that fail schema validation or type parsing are routed alongside their error stack trace. This prevents a single malformed row from crashing the entire batch while preserving the corrupt data for debugging."*

### Q5: "How do you reconcile business metrics across daily batch and real-time streaming pipelines?"
> **Response**: *"I use a **Lambda/Kappa Architecture** pattern where real-time streaming provides fast, approximate metrics for real-time dashboards, while the nightly batch ETL runs comprehensive data quality reconciliations against authoritative source transactional DBs to lock down final financial numbers."*
