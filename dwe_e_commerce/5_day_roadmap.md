# TikTok Data Warehouse Engineer Graduate — 5-Day Intensive Sprint Roadmap
**Role**: Data Warehouse Engineer Graduate (Data Platform, Global E-Commerce) — 2027 Start  
**Location**: Singapore | **Target Job Code**: A13880  
**Timeframe**: 5 Days (~4–5 Hours / Day = 20–25 Total Preparation Hours)

---

## 🎯 Executive Strategy & Core Constraints

1. **Interview Structure (Confirmed vs. Inferred)**:
   - **🟢 Tier A: Recruiter-Confirmed**:
     - Technical Round 1 (Senior Peer / Potential Mentor) + Technical Round 2 (Hiring Manager) + HR Round.
     - Live coding strictly with **Zero AI Assistance**.
     - Discussion of past data experience, school projects, research/internship, career motivation & future plans.
   - **🟡 Tier B: Inferred Signals (JD & DE Reports)**:
     - SQL/DSA live coding questions, Data Warehousing, Spark/Kafka conceptual reasoning, TikTok Shop business case.
2. **Candidate Positioning**: Bridge NTU REP Engineering/Math background & Clinical AI (GERD time-series ML) experience into Data Warehouse Engineering. Frame ML experience as discovering that **data quality, scalable pipelines, and warehousing are the true backbone of all data/ML products**.

---

## 📅 5-Day High-Yield Sprint Schedule

```
Day 1: SQL Fundamentals, E-Commerce Metrics & Project Story Foundations (4h SQL + 1h Project)
Day 2: Live Coding & Algorithm Problem Solving + Daily SQL Drill (4h Coding + 1h SQL)
Day 3: Data Warehousing, ETL & TikTok Shop Business Reasoning (5h Warehouse/ETL/Metrics)
Day 4: Pipeline Reliability, Spark/Kafka & Networks (2.5h Spark/Kafka + 1h Networks + 1.5h Pipeline Reliability)
Day 5: GERD Project Deep-Dive, Behavioral Prep & Full Mock Rounds (1h GERD + 1h STAR + 3h Mocks)
```

---

### Day 1: SQL Fundamentals, E-Commerce Metrics & Project Story Foundations
> **Goal**: Solve common analytical SQL problems independently in ~15–20 minutes while establishing a 100% defensible project story.

* **Hour 1: CV Anchor & 100% Defensible GERD Story**
  - Formulate 90-second self-introduction and 2-minute GERD time-series project pitch.
  - **Defensible Narrative**: *"My research work made me appreciate how much downstream analysis and modelling depends on clean, well-structured, and reliable data. Working with physiological time-series data showed me that preprocessing, data quality, and how data is organised are just as important as the model itself."*
  - Connect project to data engineering: Ingestion → Signal Segmentation → Event Extraction → Data Quality Checks.
* **Hour 2: SQL Core Patterns & Window Functions**
  - Advanced JOINs, `GROUP BY` / `HAVING`, `CASE WHEN`, `NULL` handling semantics.
  - Window Functions: `ROW_NUMBER()`, `RANK()`, `DENSE_RANK()`, `LAG()`, `LEAD()`, `SUM/AVG OVER (PARTITION BY ... ORDER BY ...)`.
* **Hours 3–4: TikTok E-Commerce Analytical SQL Drills (No-AI Practice)**
  1. **Top-N Sellers per Category**: Top 3 sellers by GMV per product category each month.
  2. **User Retention / Consecutive Purchase**: Users purchasing in 3 consecutive days/months.
  3. **Rolling 7-Day Metrics**: Daily 7-day moving average of GMV per region.
  4. **Deduplication & State Tracking**: Deduplicate payment status logs keeping latest state per order.
  5. **Conversion Funnel**: Drop-off rate across `Impression` → `Click` → `Add-to-Cart` → `Purchase` → `Refund`.
* **Hour 5: Analytical Warehouse Optimization**
  - Explain partition pruning, clustering/bucketing, reducing scanned data, join strategies, pre-aggregation, and avoiding shuffles (rather than OLTP indexing).

---

### Day 2: Live Coding & Data Structures (+ Daily SQL Drill)
> **Goal**: Clean Python problem-solving of LeetCode Easy-Medium patterns without IDE hints.

* **Hour 1: Live Coding Protocol**
  - Verbally state brute-force ($O(N^2)$) → Propose optimal approach ($O(N)$) → Implement clean Python code → Dry-run sample inputs → Test edge cases.
* **Hours 2–3: High-Frequency Patterns**
  - **Arrays & HashMaps**: Two Sum / 3Sum, Subarray Sum Equals K, Group Anagrams.
  - **Sliding Window & Two Pointers**: Longest Substring Without Repeating Characters, Container With Most Water.
  - **Prefix Sums & Range Queries**: Range Sum Query, Subarray Sum Equals K, Product of Array Except Self.
* **Hour 4: Tree Traversals & Secondary Patterns**
  - **Trees / BFS / DFS**: Binary Tree Level Order Traversal, Lowest Common Ancestor, Number of Islands, Top K Frequent Elements.
* **Hour 5: Daily SQL Drill (1 Hour)**
  - 2 timed window function problems (15 mins each) + handling NULLs and duplicates.

---

### Day 3: Data Warehousing, ETL & TikTok Shop Business Reasoning
> **Goal**: Master dimensional modelling, grain definition, ETL idempotency, and E-Commerce business metric cases.

* **Hour 1: Core Warehousing Principles & Golden Rule**
  - *"Before choosing tables or drawing schemas, I first clarify the analytical use cases and explicitly define the grain of each fact."*
  - OLTP vs OLAP, Star vs Snowflake, SCD Type 1 vs SCD Type 2.
* **Hours 2–3: Case Study — TikTok Shop Analytics Warehouse**
  - **Fact Tables**: `fact_order_item` (Grain: one row per ordered SKU item), `fact_product_event` (views/clicks/livestreams), `fact_refund`.
  - **Dimension Tables**: `dim_user`, `dim_seller`, `dim_product`, `dim_date`.
  - **Partitioning Strategy**: Partition by `event_date` / `order_date` + cluster/bucket by `user_id` / `seller_id`.
* **Hours 4–5: Business Partner Metrics & Incident Triage**
  - **Metric Definitions**: Exact definition of GMV (Gross value of paid orders before refunds vs. completed orders).
  - **Mutable States**: Preserving history as an order transitions (`Paid` → `Cancelled` → `Refunded`).
  - **Attribution Logic**: Attributing delayed purchases across Livestreams vs. Short Videos vs. Search.
  - **Incident Triage Case**: *"Business team reports seller performance dropped 15% yesterday. How do you investigate?"*
    (1. Clarify metric → 2. Check segment/scope → 3. Validate data pipeline freshness → 4. Inspect schema/source changes → 5. Reconcile raw event logs).

---

### Day 4: Pipeline Reliability, Spark/Kafka & Networks
> **Goal**: Demonstrate strong trade-off reasoning for distributed data pipelines, debugging slow/skewed jobs, and network basics.

* **Hours 1–2.5: Apache Spark & Kafka (Conceptual & Debugging Focus)**
  - **Spark**: Driver vs. Executors, Shuffle mechanics (Wide vs. Narrow), Data Skew diagnosis & **salting** strategy, Broadcast Joins for small $\times$ large tables.
  - **Kafka**: Topics, Partitions, Consumer Groups, Offsets, **Consumer Lag** causes and fixes.
* **Hours 2.5–3.5: Pipeline Reliability & Defensible Scaling Reasoning**
  - Idempotent pipeline design (re-running DAGs without double-counting metrics).
  - Handling late-arriving data and schema drift.
  - **Defensible Project Scaling**: *"I'd first clarify ingestion frequency, latency requirements, file sizes, and downstream consumers. If continuous low-latency ingestion is required, I'd evaluate a streaming architecture; otherwise, a scheduled batch pipeline with partitioned storage is simpler, cheaper, and easier to maintain."*
* **Hours 3.5–5: Computer Networks Fundamentals**
  - TCP vs. UDP (Reliability vs. Latency trade-offs), HTTP/HTTPS status codes & REST, DNS resolution flow, Latency vs. Throughput, Retries + Idempotency keys in API pipelines.

---

### Day 5: Project Deep-Dive, Behavioral Prep & Full Mock Rounds
> **Goal**: Defend GERD project thoroughly, refine STAR stories, and complete 2 full simulated mock interviews.

* **Hour 1: GERD Time-Series Clinical AI Defense**
  - Deep-dive into MII-pH time-series preprocessing, windowing, class imbalance, and cross-patient validation without data leakage.
* **Hour 2: Behavioral & STAR Stories**
  - Technical challenge under pressure, team disagreement, translating tech concepts to non-technical partners, learning a new technology quickly.
* **Hours 3–5: Simulated Mock Interviews**
  - **Mock 1 (Senior Peer)**: 15-min Intro & GERD project probe + 20-min Live SQL + 15-min Python DSA.
  - **Mock 2 (Hiring Manager)**: 15-min Career Motivation ("Why Data Platform?") + 20-min TikTok Shop Warehouse & Incident Triage Case + 15-min Scale & Reliability Q&A.

---

## 🛠️ Daily Execution Checklist

| Day | Primary Focus | Daily Deliverable | Status |
|:---|:---|:---|:---:|
| **Day 1** | SQL & Project Story | Solved 5 analytical SQL queries + Drafted defensible GERD pitch | 🟩 Pending |
| **Day 2** | Live Coding DSA + SQL | Solved 5 Python LeetCode Mediums + 2 Timed SQL Drills | 🟩 Pending |
| **Day 3** | Warehousing & Business | Designed TikTok Shop Schema + Solved Incident Triage & GMV cases | 🟩 Pending |
| **Day 4** | Pipelines, Spark & Networks | Mastered pipeline skew/lag reasoning & network/idempotency basics | 🟩 Pending |
| **Day 5** | GERD Defense & 2 Mocks | Completed GERD cross-examination + 2 Full Mock Interviews | 🟩 Pending |

---

## 💡 Key Questions to Ask TikTok Interviewers

1. **For Senior Peer / Potential Mentor**:
   - *"What does the typical end-to-end workflow look like for a graduate engineer on the Data Platform Business Partnering team—from business requirement to metric layer release?"*
   - *"How does the team balance building batch ETL pipelines versus real-time streaming warehouses for global e-commerce events?"*
2. **For Hiring Manager**:
   - *"What are the biggest technical scaling challenges the Global E-Commerce Data Platform team is planning to tackle over the next 1–2 years?"*
   - *"What does success look like for a new graduate joining this team during their first 6 to 12 months?"*
