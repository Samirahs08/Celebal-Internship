# Incremental Data Processing with Delta Lake

## Objective
Load sales data into a Delta table, clean it, simulate an incremental batch (updates + new records), and use MERGE to upsert it — then validate the results.

## Dataset
- `file_1` — base dataset (9,494 rows)
- `file_2` — incremental batch (500 new rows)

## Steps
1. **Load** `file_1` into Delta table `sales_delta` (renamed columns to remove spaces).
2. **Clean** — removed nulls in key columns and duplicate rows.
3. **Simulate incremental data** — took 5 existing rows with modified Sales/Profit (updates) + all of `file_2` (new rows), saved as `sales_incremental`.
4. **MERGE** — matched rows updated, unmatched rows inserted, using `Row_ID` as the key.
5. **Validate** — checked row count, confirmed no duplicate Row_IDs, verified updated rows show new values.
6. **Final output** — displayed merged table and `DESCRIBE HISTORY` to show the transaction log.

## Tools
Databricks, PySpark, Delta Lake (Unity Catalog)

## Result
MERGE completed successfully — existing records updated, new records inserted, no duplicates in final table.
