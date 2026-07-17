import pandas as pd
from faker import Faker
import random

fake = Faker()

TOTAL_CUSTOMERS = 500
INVALID_EMAIL_PERCENT = 0.02

CUSTOMER_TYPES = [
    "REGULAR",
    "PREMIUM",
    "VIP"
]


def generate_customers():

    invalid_email_count = int(
        TOTAL_CUSTOMERS * INVALID_EMAIL_PERCENT
    )

    invalid_email_ids = random.sample(
        range(1, TOTAL_CUSTOMERS + 1),
        invalid_email_count
    )

    customers = []

    for i in range(1, TOTAL_CUSTOMERS + 1):

        email = fake.email()

        if i in invalid_email_ids:

            if random.choice([True, False]):
                email = email.replace("@", "")
            else:
                email = email.split("@")[0] + "@"

        customer = {
            "customer_id": i,
            "customer_name": fake.name(),
            "email": email,
            "registration_date": fake.date_between(
                start_date="-5y",
                end_date="today"
            ),
            "customer_type": random.choice(CUSTOMER_TYPES)
        }

        customers.append(customer)

    return pd.DataFrame(customers)


def save_customers(df):

    df.to_csv("../data/customers.csv", index=False)

def main():

    df = generate_customers()

    save_customers(df)

    print(df.head())

    print("\ncustomers.csv generated successfully!")


if __name__ == "__main__":
    main()