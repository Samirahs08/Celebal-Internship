import sqlite3
from datetime import datetime


def test_invalid_order_id(cursor):

    cursor.execute("""
    SELECT COUNT(*)
    FROM order_items oi
    LEFT JOIN orders o
    ON oi.order_id=o.order_id
    WHERE o.order_id IS NULL;
    """)

    count = cursor.fetchone()[0]

    print("1. Invalid Order IDs :", count)


def test_invalid_discount(cursor):

    cursor.execute("""
    SELECT COUNT(*)
    FROM order_items
    WHERE discount_percent>100;
    """)

    count = cursor.fetchone()[0]

    print("2. Discount >100 :", count)


def test_zero_quantity(cursor):

    cursor.execute("""
    SELECT COUNT(*)
    FROM order_items
    WHERE quantity=0;
    """)

    count = cursor.fetchone()[0]

    print("3. Zero Quantity :", count)


def test_future_orders(cursor):

    today = datetime.today().strftime("%Y-%m-%d")

    cursor.execute("""
    SELECT COUNT(*)
    FROM orders
    WHERE order_date>?;
    """, (today,))

    count = cursor.fetchone()[0]

    print("4. Future Orders :", count)


def main():

    conn = sqlite3.connect("sql/ecommerce.db")
    cursor = conn.cursor()

    print("========== Edge Case Testing ==========\n")

    test_invalid_order_id(cursor)
    test_invalid_discount(cursor)
    test_zero_quantity(cursor)
    test_future_orders(cursor)

    conn.close()


if __name__ == "__main__":
    main()