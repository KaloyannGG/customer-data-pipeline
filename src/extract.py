import csv

file_path = "data/raw/customers.csv"

with open(file_path, mode="r", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
      print(row)