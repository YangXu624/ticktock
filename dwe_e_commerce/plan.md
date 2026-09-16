TikTok Data Warehouse Engineer Graduate (Data Platform, Global E-Commerce) — 2027 Start

Interview Preparation Context + Roadmap

Purpose of this file: Give a coding/interview-preparation agent enough context to coach me specifically for TikTok's Data Warehouse Engineer Graduate (Data Platform, Global E-Commerce) — 2027 Start role in Singapore.

Important: This is the full-time graduate/regular role, not the internship role. Ignore earlier discussion about part-time internships unless I explicitly bring it up again.

Target Job Code: A13880
Location: Singapore
Employment Type: Regular
Official listing: https://lifeattiktok.com/search/7664884785422256389

1. Target Role — Canonical Job Description

Team

Data Platform Business Partnering, Global E-Commerce

TikTok describes the team as being at the core of its E-Commerce business. The team generates and manages very large volumes of data and provides data-access services and applications to business and engineering teams. Its work supports analysis, business strategy, product development, and growth.

This is not a pure dashboard/BI role and not a pure backend SWE role. It spans:
- data warehousing
- batch and streaming data processing
- ETL
- data modelling
- business metrics
- data products
- analytics
- dashboards and data communication
- cross-functional work with business and engineering teams

Official Responsibilities
- Translate business requirements and end-to-end solution designs into technical implementations.
- Build batch and real-time data warehouses.
- Lead data modelling design.
- Develop, maintain, and optimize ETL jobs.
- Collaborate with business teams to define and build data metrics based on the data warehouse.
- Build and maintain data products supporting business analysis and decision-making.
- Participate in system rollouts, upgrades, implementations, and releases.
- Develop analytical techniques and data applications to turn raw data into meaningful insights.

Official Minimum Qualifications
- Completing or recently completed a Bachelor's / Master's degree in CS, Software Engineering, or related technical discipline.
- Solid CS fundamentals: data structures and algorithms, SQL, computer networks.
- Strong coding skills in at least one of: C, C++, Java, Python, Golang.

2. What This Role Actually Optimizes For

The role combines:
Data Engineer / Data Warehouse Engineer + Analytics Engineer + Business-facing Data Platform Engineer.

The technical center of gravity is:
- SQL
- Data modelling / Data warehouse design
- ETL / Data pipelines
- General coding / DSA
- Batch vs streaming concepts
- Data quality, reliability, and business metrics
- Large-scale data reasoning & stakeholder communication

3. Confirmed Interview Process From Recruiter (Tier A — High Confidence)

From recruiter voice notes (16 Sep 2026):
- Technical Round 1: Senior peer / senior member of the team (potential mentor).
- Technical Round 2: Hiring Manager.
- HR Round: Behavioral questions, teamwork, career plans, admin.
- Live Coding Constraint: Must be completed independently with ZERO AI assistance.
- Confirmed Themes: Discussion of past data experience, school projects, research/internships, career motivation, live coding, and teamwork.

4. External Interview Signals — Use With Caution (Tier B — Inferred / Supporting Only)

Not guaranteed for this exact process, but common in Singapore DE reports:
- SQL coding (window functions, aggregations)
- Python live coding
- Data pipeline & warehouse modelling concepts
- Conceptual Spark (data skew, shuffle) & Kafka (consumer lag, topics/partitions)
- Short data design / metric triage questions

5. Candidate Context — Relevant Background

Education:
- Nanyang Technological University (NTU)
- Renaissance Engineering Programme (REP) — interdisciplinary engineering/science/management background
- Mathematics Minor — strong background in probability, calculus, linear algebra, analysis.

Research / Data Experience:
- NTU Research Assistant — Clinical AI (GERD / MII-pH 24-hour physiological time-series data).
- Relevant angles: raw time-series ingestion, windowing, signal preprocessing, event extraction, class imbalance, cross-patient validation without data leakage.

Strengths:
- Mathematical/analytical reasoning, Python fluency, algorithmic problem solving, explaining technical concepts.

6. Interview Positioning / Personal Narrative (100% Defensible)

Core Narrative:
"My research work made me appreciate how much downstream analysis and modelling depends on clean, well-structured, and reliable data. Working with physiological time-series data showed me that preprocessing, data quality, and how data is organised are just as important as the model itself. I want to build those core platform foundations at TikTok E-Commerce."

Defensible Scaling Reasoning:
"When scaling data ingestion, I'd first clarify ingestion frequency, latency requirements, file sizes, and downstream consumers. If continuous low-latency ingestion is required, I'd evaluate a streaming architecture; otherwise a scheduled batch pipeline with partitioned storage is simpler, cheaper, and easier to maintain."

7. Preparation Priority Hierarchy (5-Day Focus)

1. CV & Project Mastery (GERD project defense & 90s pitch)
2. SQL Fluency (15–20 min daily drills, analytical warehouse optimization)
3. Independent Python Live Coding (LeetCode Easy-Medium without AI)
4. Data Warehousing & ETL Fundamentals (Grain statement first, star schema, SCDs, idempotency)
5. TikTok Shop Business Data Reasoning (GMV definitions, mutable states, attribution, seller performance triage)
6. Pipeline Reliability & Scale Reasoning
7. Spark / Kafka Conceptual Understanding
8. Computer Network Fundamentals

8. Technical Preparation Syllabus

8.1 SQL — Highest Priority
- Master: SELECT, WHERE, GROUP BY, HAVING, JOINs, CTEs, CASE WHEN, NULL handling.
- Window Functions: ROW_NUMBER, RANK, DENSE_RANK, LAG, LEAD, SUM/AVG OVER (PARTITION BY ... ORDER BY ...).
- Patterns: Top N per group, deduplication, 7-day rolling GMV, retention, conversion funnels.
- Warehouse Optimization: Partition pruning, clustering/bucketing, reducing scanned data, join strategies, pre-aggregation.

8.2 Data Structures & Algorithms
- Framework: Clarify → Verbalize brute force $O(N^2)$ → Propose optimal $O(N)$ → Code → Dry-run → Edge cases.
- Patterns: HashMaps, Two Pointers, Sliding Window, Prefix Sum / Range Queries, Binary Trees (BFS/DFS), Heaps.

8.3 Data Warehousing & ETL
- Golden Rule: "Before choosing tables, clarify analytical use cases and define the grain of each fact."
- Concepts: OLTP vs OLAP, Star vs Snowflake, Fact vs Dimension, Grain (`order_item`), SCD Type 1 vs Type 2, Idempotency, Backfills.

8.4 Spark & Kafka Fundamentals
- Focus: Conceptual understanding and debugging slow/skewed pipelines.
- Spark: Driver vs Executors, Shuffle, Data Skew & Salting strategy, Broadcast Join.
- Kafka: Topics, Partitions, Consumer Groups, Offsets, Consumer Lag causes/solutions.

8.5 Computer Networks & Reliability
- TCP vs UDP, HTTP/HTTPS, DNS lookup, Latency vs Throughput, Retries + Idempotency keys in distributed APIs.

9. Role-Specific Case: TikTok Shop Analytics Warehouse
- Fact Tables: `fact_order_item`, `fact_product_event`, `fact_refund`.
- Dimensions: `dim_user`, `dim_seller`, `dim_product`, `dim_date`.
- Business Metrics: GMV definitions, Order state transitions (`Paid` → `Cancelled` → `Refunded`), Livestream/Video conversion attribution.
- Incident Triage: "Seller performance dropped 15% yesterday" diagnostic steps.

10. Active 5-Day Intensive Sprint Roadmap
Refer to [5_day_roadmap.md](file:///Users/yangxu/code/tiktok/dwe_e_commerce/5_day_roadmap.md) for the active hourly schedule, daily deliverables, and execution checklist.

Summary Schedule:
- Day 1: SQL Fundamentals, E-Commerce Metrics & Project Story Foundations (4h SQL + 1h CV)
- Day 2: Live Coding & Algorithm Problem Solving + Daily SQL Drill (4h Coding + 1h SQL)
- Day 3: Data Warehousing, ETL & TikTok Shop Business Reasoning (5h Warehouse/ETL/Metrics)
- Day 4: Pipeline Reliability, Spark/Kafka & Networks (2.5h Spark/Kafka + 1h Networks + 1.5h Reliability)
- Day 5: GERD Project Deep-Dive, Behavioral Prep & Full Mock Rounds (1h GERD + 1h STAR + 3h Mocks)

11. Questions to Ask Interviewers
- Peer/Mentor: "What does a typical workflow look like from business requirement to metric layer release?"
- Hiring Manager: "What are the largest technical scaling challenges the Global E-Commerce Data Platform team is tackling over the next 1–2 years?"
