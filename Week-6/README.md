#  Spark Fundamentals

A quick recap of what I learned and practiced this week with Apache Spark (PySpark on Databricks), using a sample sales dataset (`sales_data`).

---

## 📌 Topics Covered

### 1. Driver, Executor, and Cluster Understanding
Learned how a Spark application actually runs behind the scenes — the **Driver** plans and coordinates the job, the **Cluster Manager** allocates machines/resources, and **Executors** do the real work of processing data in parallel. Also understood why the Driver crashing is different (and more serious) than an Executor crashing.

### 2. Creating DataFrames, Schema, and Column Operations
Practiced creating DataFrames from files, checking schema with `.printSchema()`, and performing common column-level operations — renaming columns, casting data types (e.g., String to Double), and adding new calculated columns.

### 3. CSV vs Parquet — Read/Write
Understood the difference between CSV (row-based) and Parquet (columnar) storage, and why Parquet is more efficient for big data due to compression and predicate pushdown. Practiced reading/writing both formats in Spark.

### 4. Filter, GroupBy, and Partitioning
Worked with `.filter()` using AND/OR conditions, used `.groupBy()` for aggregations, and got a basic understanding of how Spark partitions data across executors for parallel processing.

### 5. Assignment — Spark Assignment
Applied all of the above concepts hands-on in a structured assignment using a 750-record sales dataset, covering both theory questions and actual PySpark code on Databricks.

---

## 🛠️ Tools Used

- **Databricks Notebooks** for running PySpark code
- **Unity Catalog Volumes** for uploading and reading data files
- **PySpark DataFrame API** for all transformations

---

## 🔑 Key Takeaways

- Spark distributes work across a cluster, which is why it handles huge datasets far better than single-machine tools like Pandas or Excel.
- Lazy evaluation lets Spark optimize a whole chain of transformations before actually running anything.
- Parquet is generally the better storage choice over CSV for performance-heavy pipelines.
- Filtering, grouping, and understanding partitioning are the building blocks for almost all real Spark data processing tasks.
