import csv
from datetime import datetime

file_path = "data/raw/customers.csv"

seen_emails = []
#open csv file
with open(file_path, "r", encoding="utf-8") as file:

  #read every row and go to customers one by one
  reader = csv.DictReader(file)
  for customer in reader:
    name = customer["first_name"]
    email = customer["email"]
    signup_date = customer["signup_date"]



    #check if email is missing
    if email == "":
      print(name, "- Missing email")
    else:
      print(name,"-",email)

    if email != "":    
      if email in seen_emails:
        print(name, "- Duplicate customer")
      else:
        seen_emails.append(email)


    #check if the date is valid
    #print("DATE:", signup_date) -test
    try:
      datetime.strptime(signup_date, "%Y-%m-%d")
    except ValueError:
      print(name, "- Invalid date")
    