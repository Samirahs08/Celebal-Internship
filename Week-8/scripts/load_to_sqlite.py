import pandas as pd
import sqlite3


def load_data():

    # Create/Open SQLite database
    conn = sqlite3.connect("../ecommerce.db")

    # Read cleaned CSV files
    customers = pd.read_csv("../cleaned-data/clean_customers.csv")

    products = pd.read_csv("../cleaned-data/clean_products.csv")

    orders = pd.read_csv("../cleaned-data/clean_orders.csv")

    order_items = pd.read_csv("../cleaned-data/clean_order_items.csv")

    # Load into SQLite tables
    customers.to_sql(
        "customers",
        conn,
        if_exists="replace",
        index=False
    )

    products.to_sql(
        "products",
        conn,
        if_exists="replace",
        index=False
    )

    orders.to_sql(
        "orders",
        conn,
        if_exists="replace",
        index=False
    )

    order_items.to_sql(
        "order_items",
        conn,
        if_exists="replace",
        index=False
    )

    conn.close()

    print("Data loaded into SQLite successfully!")


def main():

    load_data()


if __name__ == "__main__":
    main()