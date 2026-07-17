import pandas as pd
import random

TOTAL_ORDER_ITEMS = 2500
TOTAL_ORDERS = 1000
TOTAL_PRODUCTS = 200


def generate_order_item(item_id):

    quantity = random.randint(1, 5)

    # 3% negative quantities
    if random.random() < 0.03:
        quantity = -quantity

    return {
        "item_id": item_id,
        "order_id": random.randint(1, TOTAL_ORDERS),
        "product_id": random.randint(1, TOTAL_PRODUCTS),
        "quantity": quantity,
        "unit_price": round(random.uniform(100, 100000), 2),
        "discount_percent": random.randint(0,100)
    }


def generate_order_items():

    order_items = []

    for i in range(1, TOTAL_ORDER_ITEMS + 1):
        order_items.append(generate_order_item(i))

    return pd.DataFrame(order_items)


def save_order_items(df):

    df.to_csv("../data/order_items.csv", index=False)


def main():

    df = generate_order_items()

    save_order_items(df)

    print(df.head())

    print("\n--------------------------------")
    print("order_items.csv generated successfully!")
    print(f"Total Order Items : {len(df)}")


if __name__ == "__main__":
    main()