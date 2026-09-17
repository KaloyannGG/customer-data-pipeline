import csv
import psycopg
from getpass import getpass

password = getpass("PostgreSQL password: ")

# connect to customer_data
connection = psycopg.connect(
    dbname="customer_data",
    user="postgres",
    password=password,
    host="localhost",
    port="5432"
)

# open cleaned customer data
with open("data/processed/valid_customers.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    cursor = connection.cursor()

    for customer in reader:
        cursor.execute(
            """
            INSERT INTO customers
            (customer_id, first_name, last_name, email, country, signup_date)
            VALUES (%s, %s, %s, %s, %s, %s)
            """,
            (
                customer["customer_id"],
                customer["first_name"],
                customer["last_name"],
                customer["email"],
                customer["country"],
                customer["signup_date"]
            )
        )

connection.commit()

print("Customers loaded successfully!")

cursor.close()
connection.close()