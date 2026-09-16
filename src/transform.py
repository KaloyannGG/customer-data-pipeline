import csv
from datetime import datetime

file_path = "data/raw/customers.csv"

seen_emails = []
valid_customers = []
invalid_customers = []

#open csv file
with open(file_path, "r", encoding="utf-8") as file:

  #read every row and go to customers one by one
  reader = csv.DictReader(file)
  for customer in reader:
    name = customer["first_name"]
    email = customer["email"]
    signup_date = customer["signup_date"]
    has_error = False



    #check if email is missing
    if email == "":
      print(name, "- Missing email")
      has_error = True
    else:
      print(name,"-",email)

    if email != "":    
      if email in seen_emails:
        print(name, "- Duplicate customer")
        has_error = True
      else:
        seen_emails.append(email)


    #check if the date is valid
    #print("DATE:", signup_date) -test
    try:
      datetime.strptime(signup_date, "%Y-%m-%d")
    except ValueError:
      print(name, "- Invalid date")
      has_error = True

    if has_error:
      invalid_customers.append(customer)
    else:
      valid_customers.append(customer)

print("Valid customers:", len(valid_customers))
print("Invalid customers:", len(invalid_customers)) 

# Save valid customers to a new CSV file
with open("data/processed/valid_customers.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=reader.fieldnames)

    writer.writeheader()
    writer.writerows(valid_customers)

# Save invalid customers to a new CSV file
with open("data/processed/invalid_customers.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=reader.fieldnames)

    writer.writeheader()
    writer.writerows(invalid_customers)