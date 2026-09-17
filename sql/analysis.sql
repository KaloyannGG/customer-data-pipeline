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