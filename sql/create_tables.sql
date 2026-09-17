-- customers table
CREATE TABLE IF NOT EXISTS customers (
    customer_id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(100),
    country VARCHAR(50),
    signup_date DATE
);