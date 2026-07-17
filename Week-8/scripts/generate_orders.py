import pandas as pd
from faker import Faker
import random

fake = Faker()

TOTAL_ORDERS = 1000
TOTAL_CUSTOMERS = 500

ORDER_STATUS = [
    "PLACED",
    "SHIPPED",
    "DELIVERED",
    "CANCELLED",
    "RETURNED"
]

REGIONS = [
    "North",
    "South",
    "East",
    "West"
]


def generate_order(order_id):

    customer_id = random.randint(1, TOTAL_CUSTOMERS)

    # 5% NULL customer_id
    if random.random() < 0.05:
        customer_id = None

    order_date = fake.date_between(start_date="-2y", end_date="today")

    # 5% wrong date format
    if random.random() < 0.05:
        order_date = order_date.strftime("%d-%m-%Y")
    else:
        order_date = order_date.strftime("%Y-%m-%d")

    return {
        "order_id": order_id,
        "customer_id": customer_id,
        "order_date": order_date,
        "status": random.choice(ORDER_STATUS),
        "region_code": random.choice(REGIONS)
    }


def generate_orders():

    orders = []

    for i in range(1, TOTAL_ORDERS + 1):
        orders.append(generate_order(i))

    return pd.DataFrame(orders)


def save_orders(df):

    df.to_csv("../data/orders.csv", index=False)


def main():

    df = generate_orders()

    save_orders(df)

    print(df.head())

    print("\n--------------------------------")
    print("orders.csv generated successfully!")
    print(f"Total Orders : {len(df)}")


if __name__ == "__main__":
    main()