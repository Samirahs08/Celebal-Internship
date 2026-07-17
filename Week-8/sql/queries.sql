-------------------------------------------------------
-- Query 1 : Total Revenue Per Category
-------------------------------------------------------
SELECT p.category,ROUND(SUM(oi.quantity *oi.unit_price
 *(1 - oi.discount_percent / 100.0)),2) 
AS total_revenue FROM products p
JOIN order_items oi
ON p.product_id = oi.product_id
GROUP BY p.category
ORDER BY total_revenue DESC;

-------------------------------------------------------
-- Query 2 : Top 10 Customers by Total Order Value
-------------------------------------------------------

SELECT c.customer_id,
c.customer_name,
ROUND(SUM(oi.quantity*oi.unit_price*(1-oi.discount_percent/100.0)),2) AS total_order_value
FROM customers c
JOIN orders o
ON c.customer_id=o.customer_id
JOIN order_items oi
ON o.order_id=oi.order_id
GROUP BY c.customer_id,c.customer_name
ORDER BY total_order_value DESC
LIMIT 10;

-------------------------------------------------------
-- Query 3 : Month-wise Order Count
-------------------------------------------------------

SELECT strftime('%Y-%m',order_date) AS month,
COUNT(order_id) AS total_orders
FROM orders
GROUP BY strftime('%Y-%m',order_date)
ORDER BY month;

-------------------------------------------------------
-- Query 4 : Customers With No Delivered Orders
-------------------------------------------------------

SELECT c.customer_id,
c.customer_name
FROM customers c JOIN orders o
ON c.customer_id=o.customer_id
GROUP BY c.customer_id,c.customer_name
HAVING SUM(CASE
WHEN o.status='DELIVERED' THEN 1
ELSE 0 END)=0;

-------------------------------------------------------
-- Query 5 : Products With More Returns Than Purchases
-------------------------------------------------------

SELECT p.product_id,
p.product_name,
SUM(CASE
WHEN o.status='RETURNED' THEN 1
ELSE 0
END) AS returned_orders,
SUM(CASE
WHEN o.status<>'RETURNED' THEN 1
ELSE 0
END) AS purchased_orders
FROM products p
JOIN order_items oi
ON p.product_id=oi.product_id
JOIN orders o
ON oi.order_id=o.order_id
GROUP BY p.product_id,p.product_name
HAVING returned_orders>purchased_orders;

-------------------------------------------------------
-- Query 6 : Return Rate Per Category
-------------------------------------------------------

SELECT p.category,
COUNT(*) AS total_orders,
SUM(CASE
WHEN o.status='RETURNED' THEN 1
ELSE 0
END) AS returned_orders,
ROUND(
SUM(CASE
WHEN o.status='RETURNED' THEN 1
ELSE 0
END)*100.0/COUNT(*),
2
) AS return_rate
FROM products p
JOIN order_items oi
ON p.product_id=oi.product_id
JOIN orders o
ON oi.order_id=o.order_id
GROUP BY p.category
ORDER BY return_rate DESC;

-------------------------------------------------------
-- Query 7 : Running Total of Revenue
-------------------------------------------------------

WITH daily_revenue AS
(
SELECT o.order_date,
ROUND(SUM(
oi.quantity*
oi.unit_price*
(1-oi.discount_percent/100.0)
),2) AS revenue
FROM orders o
JOIN order_items oi
ON o.order_id=oi.order_id
GROUP BY o.order_date
)

SELECT order_date,
revenue,
ROUND(
SUM(revenue) OVER(
ORDER BY order_date
),
2
) AS running_total
FROM daily_revenue
ORDER BY order_date;

-------------------------------------------------------
-- Query 8 : Rank Customers by Total Revenue
-------------------------------------------------------

WITH customer_revenue AS
(
SELECT c.customer_id,
c.customer_name,
ROUND(SUM(
oi.quantity*
oi.unit_price*
(1-oi.discount_percent/100.0)
),2) AS total_revenue
FROM customers c
JOIN orders o
ON c.customer_id=o.customer_id
JOIN order_items oi
ON o.order_id=oi.order_id
GROUP BY c.customer_id,c.customer_name
)

SELECT customer_id,
customer_name,
total_revenue,
DENSE_RANK() OVER(
ORDER BY total_revenue DESC
) AS customer_rank
FROM customer_revenue
ORDER BY customer_rank;

-------------------------------------------------------
-- Query 9 : Compare Customer Revenue Using LAG
-------------------------------------------------------

WITH customer_revenue AS
(
SELECT c.customer_id,
c.customer_name,
ROUND(SUM(
oi.quantity*
oi.unit_price*
(1-oi.discount_percent/100.0)
),2) AS total_revenue
FROM customers c
JOIN orders o
ON c.customer_id=o.customer_id
JOIN order_items oi
ON o.order_id=oi.order_id
GROUP BY c.customer_id,c.customer_name
)

SELECT customer_id,
customer_name,
total_revenue,
LAG(total_revenue) OVER(
ORDER BY total_revenue DESC
) AS previous_revenue,
ROUND(
total_revenue-
LAG(total_revenue) OVER(
ORDER BY total_revenue DESC
),
2
) AS revenue_difference
FROM customer_revenue
ORDER BY total_revenue DESC;

-------------------------------------------------------
-- Query 10 : Multi-Level CTE
-------------------------------------------------------

WITH customer_category_revenue AS
(
SELECT c.customer_id,
c.customer_name,
p.category,ROUND(SUM(
oi.quantity*
oi.unit_price*
(1-oi.discount_percent/100.0)
),2) AS total_revenue
FROM customers c
JOIN orders o
ON c.customer_id=o.customer_id
JOIN order_items oi
ON o.order_id=oi.order_id
JOIN products p
ON oi.product_id=p.product_id
GROUP BY c.customer_id,
c.customer_name,
p.category
),
ranked_customers AS
(
SELECT customer_id,
customer_name,
category,
total_revenue,
DENSE_RANK() OVER(
PARTITION BY category
ORDER BY total_revenue DESC
) AS rank_no
FROM customer_category_revenue
)

SELECT customer_id,
customer_name,
category,
total_revenue
FROM ranked_customers
WHERE rank_no=1
ORDER BY category;

-------------------------------------------------------
-- Query 11 : Customer Quartiles Using NTILE
-------------------------------------------------------

WITH customer_revenue AS
(
SELECT c.customer_id,
c.customer_name,
ROUND(SUM(
oi.quantity*
oi.unit_price*
(1-oi.discount_percent/100.0)
),2) AS total_revenue
FROM customers c
JOIN orders o
ON c.customer_id=o.customer_id
JOIN order_items oi
ON o.order_id=oi.order_id
GROUP BY c.customer_id,
c.customer_name
)

SELECT customer_id,
customer_name,
total_revenue,
NTILE(4) OVER(
ORDER BY total_revenue DESC
) AS spending_group
FROM customer_revenue
ORDER BY total_revenue DESC;

-------------------------------------------------------
-- Query 12 : Year-over-Year Revenue Comparison
-------------------------------------------------------

WITH yearly_revenue AS
(
SELECT strftime('%Y',o.order_date) AS year,
ROUND(SUM(
oi.quantity*
oi.unit_price*
(1-oi.discount_percent/100.0)
),2) AS total_revenue
FROM orders o
JOIN order_items oi
ON o.order_id=oi.order_id
GROUP BY strftime('%Y',o.order_date)
)

SELECT year,
total_revenue,
LAG(total_revenue) OVER(
ORDER BY year
) AS previous_year_revenue,
ROUND(
total_revenue-
LAG(total_revenue) OVER(
ORDER BY year
),
2
) AS revenue_difference
FROM yearly_revenue
ORDER BY year;

-------------------------------------------------------
-- Query 13 : First and Last Order Value
-------------------------------------------------------

WITH order_value AS
(
SELECT o.customer_id,
o.order_id,
o.order_date,
ROUND(SUM(oi.quantity*oi.unit_price*(1-oi.discount_percent/100.0)),2) AS order_value
FROM orders o
JOIN order_items oi
ON o.order_id=oi.order_id
GROUP BY o.customer_id,
o.order_id,
o.order_date
)

SELECT customer_id,
order_id,
order_date,
order_value,
FIRST_VALUE(order_value) OVER(
PARTITION BY customer_id
ORDER BY order_date
) AS first_order_value,
LAST_VALUE(order_value) OVER(
PARTITION BY customer_id
ORDER BY order_date
ROWS BETWEEN UNBOUNDED PRECEDING
AND UNBOUNDED FOLLOWING
) AS last_order_value
FROM order_value
ORDER BY customer_id,
order_date;

-------------------------------------------------------
-- Query 14 : Customer Revenue Distribution
-------------------------------------------------------

WITH customer_revenue AS
(
SELECT c.customer_id,
c.customer_name,
ROUND(SUM(oi.quantity*oi.unit_price*(1-oi.discount_percent/100.0)),2) AS total_revenue
FROM customers c
JOIN orders o
ON c.customer_id=o.customer_id
JOIN order_items oi
ON o.order_id=oi.order_id
GROUP BY c.customer_id,
c.customer_name
)

SELECT customer_id,customer_name,total_revenue,
ROUND(CUME_DIST() OVER(
ORDER BY total_revenue DESC),2) AS cumulative_distribution
FROM customer_revenue
ORDER BY total_revenue DESC;

-------------------------------------------------------
-- Query 15 : Cohort Analysis
-------------------------------------------------------

SELECT strftime('%Y-%m',c.registration_date) AS cohort_month,
COUNT(DISTINCT c.customer_id) AS total_customers,
COUNT(o.order_id) AS total_orders
FROM customers c
LEFT JOIN orders o
ON c.customer_id=o.customer_id
GROUP BY strftime('%Y-%m',c.registration_date)
ORDER BY cohort_month;

-------------------------------------------------------
-- Query 16 : Previous Order and Days Difference
-------------------------------------------------------

SELECT customer_id,
order_id,
order_date,
LAG(order_date) OVER(
PARTITION BY customer_id
ORDER BY order_date) AS previous_order_date,
ROUND(julianday(order_date)-julianday(
    LAG(order_date) OVER(
PARTITION BY customer_id
ORDER BY order_date)),0) AS days_between_orders
FROM orders
ORDER BY customer_id,
order_date;