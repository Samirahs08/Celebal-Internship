import pandas as pd


# ---------------------------------------
# Validate Emails
# ---------------------------------------

def validate_emails(df):

    df = df[df["email"].str.contains("@", na=False)]

    return df


# ---------------------------------------
# Check Referential Integrity
# ---------------------------------------

def check_referential_integrity(customers, products, orders, order_items):

    # Remove orders having customer_ids that don't exist
    orders = orders[
        orders["customer_id"].isin(customers["customer_id"])
    ]

    # Remove order_items having invalid order_ids
    order_items = order_items[
        order_items["order_id"].isin(orders["order_id"])
    ]

    # Remove order_items having invalid product_ids
    order_items = order_items[
        order_items["product_id"].isin(products["product_id"])
    ]

    return orders, order_items


# ---------------------------------------
# Clean Customers
# ---------------------------------------

def clean_customers():

    df = pd.read_csv("../data/customers.csv")

    df = validate_emails(df)

    df.to_csv("../cleaned-data/clean_customers.csv", index=False)

    print("Customers cleaned successfully!")

    return df


# ---------------------------------------
# Clean Products
# ---------------------------------------

def clean_products():

    df = pd.read_csv("../data/products.csv")

    df["product_name"] = df["product_name"].str.strip()

    df["product_name"] = df["product_name"].str.title()

    df.to_csv("../cleaned-data/clean_products.csv", index=False)

    print("Products cleaned successfully!")

    return df


# ---------------------------------------
# Clean Orders
# ---------------------------------------

def clean_orders():

    df = pd.read_csv("../data/orders.csv")

    df = df.dropna(subset=["customer_id"])

    df["order_date"] = pd.to_datetime(
        df["order_date"],
        format="mixed"
    )

    df["order_date"] = df["order_date"].dt.strftime("%Y-%m-%d")

    print("Orders cleaned successfully!")

    return df


# ---------------------------------------
# Clean Order Items
# ---------------------------------------

def clean_order_items():

    df = pd.read_csv("../data/order_items.csv")

    df = df[df["quantity"] > 0]

    print("Order Items cleaned successfully!")

    return df


# ---------------------------------------
# Main
# ---------------------------------------

def main():

    customers = clean_customers()

    products = clean_products()

    orders = clean_orders()

    order_items = clean_order_items()

    orders, order_items = check_referential_integrity(
        customers,
        products,
        orders,
        order_items
    )

    orders.to_csv("../cleaned-data/clean_orders.csv", index=False)

    order_items.to_csv(
        "../cleaned-data/clean_order_items.csv",
        index=False
    )

    print("\n--------------------------------")
    print("All datasets cleaned successfully!")


if __name__ == "__main__":
    main()