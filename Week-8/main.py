import sqlite3
from datetime import datetime, timedelta


def connect_database():
    return sqlite3.connect("sql/ecommerce.db")


def get_user_input():
    print("\n==========================================")
    print("      E-Commerce Analytics System")
    print("==========================================")

    report_type = input("Enter Report Type (daily/weekly/monthly): ").lower()

    start_date = input("Enter Start Date (YYYY-MM-DD): ")
    end_date = input("Enter End Date (YYYY-MM-DD): ")

    return report_type, start_date, end_date


def get_total_orders(cursor, start_date, end_date):
    cursor.execute("""
    SELECT COUNT(*)
    FROM orders
    WHERE order_date BETWEEN ? AND ?;
    """, (start_date, end_date))

    return cursor.fetchone()[0]


def get_total_revenue(cursor, start_date, end_date):
    cursor.execute("""
    SELECT ROUND(
        IFNULL(SUM(
            oi.quantity *
            oi.unit_price *
            (1 - oi.discount_percent / 100.0)
        ),0),
        2
    )
    FROM order_items oi
    JOIN orders o
    ON oi.order_id = o.order_id
    WHERE o.order_date BETWEEN ? AND ?;
    """, (start_date, end_date))

    return cursor.fetchone()[0]


def get_unique_customers(cursor, start_date, end_date):
    cursor.execute("""
    SELECT COUNT(DISTINCT customer_id)
    FROM orders
    WHERE order_date BETWEEN ? AND ?;
    """, (start_date, end_date))

    return cursor.fetchone()[0]


def get_top_products(cursor, start_date, end_date):
    cursor.execute("""
    SELECT
        p.product_name,
        SUM(oi.quantity) AS total_quantity
    FROM products p
    JOIN order_items oi
    ON p.product_id = oi.product_id
    JOIN orders o
    ON oi.order_id = o.order_id
    WHERE o.order_date BETWEEN ? AND ?
    GROUP BY p.product_name
    ORDER BY total_quantity DESC
    LIMIT 3;
    """, (start_date, end_date))

    return cursor.fetchall()


def previous_period(report_type, start_date, end_date):
    start = datetime.strptime(start_date, "%Y-%m-%d")
    end = datetime.strptime(end_date, "%Y-%m-%d")

    if report_type == "daily":
        days = 1
    elif report_type == "weekly":
        days = 7
    elif report_type == "monthly":
        days = 30
    else:
        days = (end - start).days + 1

    previous_end = start - timedelta(days=1)
    previous_start = previous_end - timedelta(days=days - 1)

    return (
        previous_start.strftime("%Y-%m-%d"),
        previous_end.strftime("%Y-%m-%d")
    )


def revenue_change(cursor, report_type, start_date, end_date):

    current = get_total_revenue(cursor, start_date, end_date)

    previous_start, previous_end = previous_period(
        report_type,
        start_date,
        end_date
    )

    previous = get_total_revenue(
        cursor,
        previous_start,
        previous_end
    )

    if previous == 0:
        return current, previous, 0

    change = ((current - previous) / previous) * 100

    return current, previous, round(change, 2)


def display_report(cursor, report_type, start_date, end_date):

    total_orders = get_total_orders(
        cursor,
        start_date,
        end_date
    )

    total_revenue = get_total_revenue(
        cursor,
        start_date,
        end_date
    )

    unique_customers = get_unique_customers(
        cursor,
        start_date,
        end_date
    )

    top_products = get_top_products(
        cursor,
        start_date,
        end_date
    )

    current, previous, change = revenue_change(
        cursor,
        report_type,
        start_date,
        end_date
    )

    print("\n==========================================")
    print("            SUMMARY REPORT")
    print("==========================================")

    print(f"Report Type        : {report_type.title()}")
    print(f"Date Range         : {start_date} to {end_date}")

    print("------------------------------------------")

    print(f"Total Orders       : {total_orders}")
    print(f"Total Revenue      : {total_revenue}")
    print(f"Unique Customers   : {unique_customers}")

    print("------------------------------------------")

    print("Top 3 Products")

    for i, product in enumerate(top_products, start=1):
        print(f"{i}. {product[0]} (Quantity Sold: {product[1]})")

    print("------------------------------------------")

    print(f"Previous Revenue   : {previous}")
    print(f"Current Revenue    : {current}")
    print(f"Revenue Change     : {change}%")

    print("==========================================")


def main():

    conn = connect_database()

    cursor = conn.cursor()

    report_type, start_date, end_date = get_user_input()

    display_report(
        cursor,
        report_type,
        start_date,
        end_date
    )

    conn.close()


if __name__ == "__main__":
    main()