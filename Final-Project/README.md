# Retail Data Warehouse — Medallion Architecture (Databricks + PySpark)

A centralized data platform that ingests raw CRM and ERP retail data, cleans and standardizes it, and models it into an analytics-ready Star Schema — built using the Bronze, Silver, Gold Medallion Architecture on Databricks.

## Platform
- **Databricks Free Edition** (Serverless compute)
- **PySpark** for transformations, **Delta Lake** for storage
- **Unity Catalog** for schema/table governance (`workspace.bronze`, `workspace.silver`, `workspace.gold`)

## Source Data
| System | Files |
|---|---|
| CRM | `cust_info.csv`, `prd_info.csv`, `sales_details.csv` |
| ERP | `CUST_AZ12.csv`, `LOC_A101.csv`, `PX_CAT_G1V2.csv` |

---

## 🟤 Bronze Layer — Raw Ingestion
**Notebook:** `bronze_ingestion`

**What happens:** Each of the 6 raw CSVs is read as-is and written into a Delta table, with zero cleaning or transformation. Two audit columns (`source_file`, `load_time`) are added to every table to track where and when the data was loaded — this preserves full lineage for auditing.

**Tables created:**
| Table | Rows |
|---|---|
| `bronze.crm_cust_info` | 18,494 |
| `bronze.crm_prd_info` | 398 |
| `bronze.crm_sales_details` | 60,398 |
| `bronze.erp_cust_az12` | 18,484 |
| `bronze.erp_loc_a101` | 18,484 |
| `bronze.erp_px_cat_g1v2` | 37 |

**Output:** 6 raw, unmodified Delta tables — the permanent, queryable source-of-truth copy of the original files.

---

## ⚪ Silver Layer — Cleaning & Standardization
**Notebook:** `silver_transformation`

**What happens:** Each Bronze table is read, cleaned, and re-saved. Fixes applied per table:

| Table | Key operations |
|---|---|
| `crm_cust_info` | Deduplicated (kept latest record per customer), trimmed names, standardized gender (`Male`/`Female`/`n/a`) and marital status (`Married`/`Single`/`n/a`) |
| `crm_prd_info` | Split compound product key into `cat_id` + `prd_key`, defaulted null costs to 0, mapped product line codes to full names, derived accurate `prd_end_dt` using a window function |
| `crm_sales_details` | Converted integer dates (`YYYYMMDD`) to real dates with invalid values nulled out, recalculated `sls_sales`/`sls_price` where they didn't match `quantity × price` |
| `erp_cust_az12` | Stripped inconsistent `CID` prefix, nulled out invalid future birthdates, standardized gender |
| `erp_loc_a101` | Removed dashes from `CID`, standardized country values (`US`/`USA` → `United States`, `DE` → `Germany`, blanks → `n/a`) |
| `erp_px_cat_g1v2` | Light whitespace trim (source was already clean) |

**Output:** 6 clean, standardized Delta tables — same row counts as Bronze except `crm_cust_info` (18,485 after removing duplicates), ready to be modeled.

---

## 🟡 Gold Layer — Star Schema
**Notebook:** `gold_transformation`

**What happens:** Silver tables are joined, standardized further, and reshaped into a business-friendly Star Schema. Every dimension gets a surrogate key, independent of the source system's natural key.

**Dimensions:**
- **`dim_customers`** — merges CRM + ERP customer data (identity, gender, marital status, birthdate, country). Implements **SCD Type 2**: `dw_start_date`, `dw_end_date`, `is_current` track every historical version of a customer record.
- **`dim_products`** — merges product data with category lookup. Carries version history via `start_date`/`end_date`.
- **`dim_geography`** — standalone country dimension.
- **`dim_date`** — generated calendar table spanning the full range of order dates, with year/month/quarter/day-of-week.

**Fact table:**
- **`fact_sales`** — one row per sales transaction, storing only surrogate keys (`customer_key`, `product_key`, `geography_key`, `order_date_key`) plus measures (`quantity`, `price`, `sales_amount`).

**Output:** A fully connected Star Schema — 4 dimension tables + 1 fact table — with validated relationships (no orphan foreign keys) and a demonstrated SCD Type 2 mechanism.

---

## 🟢 Optimization & Reporting
**Notebook:** `optimization_reporting`

**What happens:**
- `OPTIMIZE ... ZORDER BY` on `fact_sales` to improve file-skipping on common join/filter columns
- `ANALYZE TABLE ... COMPUTE STATISTICS` so Spark's optimizer can choose efficient join strategies
- `.explain()` used to confirm Spark selects a **Broadcast Hash Join** for small dimension tables, running on Databricks' Photon engine
- Documented scalability reasoning (Delta file compaction, star schema design, surrogate key strategy)
- 4 business insight queries proving the Gold layer answers the project's target questions: **sales trends**, **customer behavior**, and **regional performance**

**Output:** Evidence that the pipeline is performance-aware and that the finished Gold tables directly support BI-style reporting queries and dashboards.

---

## End-to-End Flow
```
Raw CSVs → Bronze (raw Delta tables) → Silver (cleaned/standardized) → Gold (Star Schema) → BI/Reporting
```
