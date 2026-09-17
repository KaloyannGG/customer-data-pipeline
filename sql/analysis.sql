-- customer orders
SELECT
    c.first_name,
    c.last_name,
    o.order_id,
    o.order_date,
    o.amount
FROM customers c
JOIN orders o
    ON c.customer_id = o.customer_id;


-- total amount spent by each customer
SELECT
    c.first_name,
    c.last_name,
    SUM(o.amount) AS total_spent
FROM customers c
JOIN orders o
    ON c.customer_id = o.customer_id
GROUP BY
    c.customer_id,
    c.first_name,
    c.last_name
ORDER BY
    total_spent DESC;

-- number of orders by customer
SELECT
    c.first_name,
    c.last_name,
    COUNT(o.order_id) AS order_count
FROM customers c
JOIN orders o
    ON c.customer_id = o.customer_id
GROUP BY
    c.customer_id,
    c.first_name,
    c.last_name
ORDER BY
    order_count DESC;

-- total order value by country
SELECT
    c.country,
    SUM(o.amount) AS total_order_value
FROM customers c
JOIN orders o
    ON c.customer_id = o.customer_id
GROUP BY
    c.country
ORDER BY
    total_order_value DESC;

-- total order value by month
SELECT
    DATE_TRUNC('month', o.order_date) AS month,
    SUM(o.amount) AS total_order_value
FROM orders o
GROUP BY
    DATE_TRUNC('month', o.order_date)
ORDER BY
    month;