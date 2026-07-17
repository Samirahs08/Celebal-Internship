# Week-8: E-Commerce Order Analytics System

## 📌 Project Overview

The **E-Commerce Order Analytics System** is a mini Data Engineering project that demonstrates the complete data pipeline from data generation to analytics and reporting.

The project simulates an e-commerce environment by generating synthetic datasets, cleaning inconsistent data, storing it in a SQLite database, performing SQL-based business analysis, generating analytical reports using Python, and validating important edge cases.

This project showcases essential Data Engineering concepts including:

- Synthetic Data Generation
- Data Cleaning
- Data Validation
- SQLite Database Management
- SQL Analytics
- Window Functions
- Common Table Expressions (CTEs)
- Python and SQL Integration
- Business Reporting
- Edge Case Testing

---

# 🎯 Objectives

The main objectives of this project are:

- Generate realistic e-commerce datasets
- Introduce intentional data quality issues
- Clean and validate the generated datasets
- Load cleaned data into SQLite
- Perform SQL-based business analysis
- Build a command-line reporting application
- Validate data integrity using edge case tests

---

# 🛠 Technologies Used

| Technology | Purpose |
|------------|----------|
| Python | Data Generation, Cleaning, Reporting |
| SQLite | Database |
| SQL | Data Analysis |
| Pandas | CSV Handling |
| Faker | Synthetic Data Generation |
| Random Module | Randomized Data Creation |
| Datetime | Date Operations |
| VS Code | Development Environment |

---

# 📁 Project Structure

```
WEEK-8
│
├── cleaned-data
│   ├── clean_customers.csv
│   ├── clean_order_items.csv
│   ├── clean_orders.csv
│   └── clean_products.csv
│
├── data
│   ├── customers.csv
│   ├── order_items.csv
│   ├── orders.csv
│   └── products.csv
│
├── Screenshots
│
├── scripts
│   ├── generate_customers.py
│   ├── generate_products.py
│   ├── generate_orders.py
│   ├── generate_order_items.py
│   ├── clean_data.py
│   └── load_to_sqlite.py
│
├── sql
│   ├── ecommerce.db
│   ├── queries.sql
│   └── check.py
│
├── main.py
│
├── edge_cases.py
│
└── README.md
```

---

# 📂 Dataset Description

The project consists of four datasets.

## 1. Customers Dataset

Contains customer information.

Columns:

- customer_id
- customer_name
- email
- registration_date
- customer_type

---

## 2. Products Dataset

Contains product information.

Columns:

- product_id
- product_name
- category
- price

---

## 3. Orders Dataset

Contains order information.

Columns:

- order_id
- customer_id
- order_date
- status
- region

---

## 4. Order Items Dataset

Contains product-level order details.

Columns:

- order_item_id
- order_id
- product_id
- quantity
- unit_price
- discount_percent

---

# 🚀 Project Workflow

The project is divided into five major phases.

---

# Phase 1 : Data Generation

Synthetic datasets are generated using Python.

Files:

- generate_customers.py
- generate_products.py
- generate_orders.py
- generate_order_items.py

The generated datasets intentionally contain invalid records to simulate real-world scenarios.

Examples include:

- Invalid email addresses
- Missing customer IDs
- Incorrect dates
- Negative quantities
- Invalid product names

Output:

```
data/
```

---

# Phase 2 : Data Cleaning

The generated datasets are cleaned using:

```
clean_data.py
```

Cleaning operations include:

### Customers

- Remove invalid emails
- Standardize values

### Products

- Remove unwanted spaces
- Correct formatting

### Orders

- Remove invalid dates
- Handle missing customer IDs

### Order Items

- Remove negative quantities
- Validate discount values

Output:

```
cleaned-data/
```

---

# Phase 3 : Loading Data into SQLite

The cleaned CSV files are loaded into SQLite using

```
load_to_sqlite.py
```

Database:

```
sql/ecommerce.db
```

Tables created:

- customers
- products
- orders
- order_items

---

# Phase 4 : SQL Analytics

Business insights are generated using SQL.

Queries include:

### Revenue Analysis

- Total Revenue per Category

### Customer Analysis

- Top Customers
- Customer Ranking
- Revenue Distribution

### Product Analysis

- Top Products
- Return Rate
- Product Performance

### Time Analysis

- Monthly Revenue
- Running Revenue
- Previous Order Date
- Year-over-Year Revenue

### Advanced SQL Concepts

- CTEs
- Window Functions
- LAG()
- DENSE_RANK()
- FIRST_VALUE()
- LAST_VALUE()
- NTILE()
- CUME_DIST()

All SQL queries are stored in

```
sql/queries.sql
```

---

# Phase 5 : Python Reporting System

The reporting application is implemented in

```
main.py
```

The program accepts user input for:

- Report Type
- Start Date
- End Date

The application generates:

- Total Orders
- Total Revenue
- Unique Customers
- Top 3 Selling Products
- Previous Period Revenue Comparison
- Revenue Growth Percentage

This demonstrates Python and SQLite integration.

---

# Edge Case Testing

Edge case validation is implemented in

```
edge_cases.py
```

The following scenarios are tested.

### Test Case 1

Invalid Order ID

Checks whether order_items contains order IDs that do not exist in the orders table.

---

### Test Case 2

Discount Greater Than 100%

Ensures that discount values do not exceed 100%.

---

### Test Case 3

Zero Quantity

Checks whether products were ordered with zero quantity.

---

### Test Case 4

Future Order Date

Verifies that no order has a future date.

---

# How to Run the Project

## Step 1

Generate datasets

```
python scripts/generate_customers.py
python scripts/generate_products.py
python scripts/generate_orders.py
python scripts/generate_order_items.py
```

---

## Step 2

Clean the datasets

```
python scripts/clean_data.py
```

---

## Step 3

Load cleaned data into SQLite

```
python scripts/load_to_sqlite.py
```

---

## Step 4

(Optional)

Verify database

```
python sql/check.py
```

---

## Step 5

Run the reporting system

```
python main.py
```

---

## Step 6

Run edge case testing

```
python edge_cases.py
```

---

# Sample Report Output

```
==========================================
E-Commerce Analytics System
==========================================

Report Type : Monthly

Date Range : 2025-01-01 to 2025-12-31

Total Orders : 1000

Total Revenue : 458732.50

Unique Customers : 496

Top 3 Products

Laptop
Smartphone
Headphones

Revenue Change : +14.62%
```

---

# Key Concepts Demonstrated

✔ Data Generation

✔ Data Cleaning

✔ Data Validation

✔ CSV Processing

✔ SQLite

✔ SQL Joins

✔ Aggregate Functions

✔ Window Functions

✔ CTEs

✔ Python Database Connectivity

✔ Business Analytics

✔ Reporting

✔ Edge Case Testing

---


# Conclusion

This project demonstrates an end-to-end data engineering workflow, beginning with synthetic data generation and ending with business reporting and data validation. It provides hands-on experience with Python, SQL, SQLite, data cleaning, analytical queries, and reporting, making it a practical demonstration of core Data Engineering skills.
