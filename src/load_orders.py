import csv
import os
import psycopg
from dotenv import load_dotenv

load_dotenv()

password = os.getenv("DB_PASSWORD")

connection = psycopg.connect(
    dbname="customer_data",
    user="postgres",
    password=password,
    host="localhost",
    port="5432"
)

with open("data/raw/orders.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    cursor = connection.cursor()

    for order in reader:
        cursor.execute(
            """
            INSERT INTO orders
            (order_id, customer_id, order_date, amount)
            VALUES (%s, %s, %s, %s)
            ON CONFLICT (order_id) DO NOTHING
            """,
            (
                order["order_id"],
                order["customer_id"],
                order["order_date"],
                order["amount"]
            )
        )

connection.commit()

print("Orders loaded successfully!")

cursor.close()
connection.close()