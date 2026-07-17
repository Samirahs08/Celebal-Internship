import pandas as pd
import random

TOTAL_PRODUCTS = 200

CATEGORIES = [
    "Electronics",
    "Clothing",
    "Books",
    "Home",
    "Sports",
    "Beauty",
    "Toys",
    "Groceries"
]

PRODUCT_NAMES = [
    "Laptop",
    "Smartphone",
    "Headphones",
    "Keyboard",
    "Mouse",
    "Monitor",
    "T-Shirt",
    "Jeans",
    "Jacket",
    "Shoes",
    "Novel",
    "Notebook",
    "Water Bottle",
    "Dining Table",
    "Chair",
    "Football",
    "Cricket Bat",
    "Face Wash",
    "Shampoo",
    "Toy Car",
    "Building Blocks",
    "Rice",
    "Milk",
    "Chocolate",
    "Coffee",
    "Mixer",
    "Air Conditioner",
    "Refrigerator",
    "Microwave",
    "Backpack"
]


def generate_product(product_id):

    product_name = random.choice(PRODUCT_NAMES)

    if random.random() < 0.10:

        if random.choice([True, False]):
            product_name = "   " + product_name + "   "
        else:
            product_name = product_name.swapcase()

    return {
        "product_id": product_id,
        "product_name": product_name,
        "category": random.choice(CATEGORIES),
        "cost_price": round(random.uniform(100, 100000), 2)
    }


def generate_products():

    products = []

    for i in range(1, TOTAL_PRODUCTS + 1):
        products.append(generate_product(i))

    return pd.DataFrame(products)


def save_products(df):

    df.to_csv("../data/products.csv", index=False)


def main():

    df = generate_products()

    save_products(df)

    print(df.head())

    print("\nProducts.csv generated successfully!")


if __name__ == "__main__":
    main()