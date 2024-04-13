import json
import random
import datetime
from faker import Faker

fake = Faker()


def generate_customer_data(num_records):
    customers = []
    for i in range(1, num_records + 1):
        name = fake.name()
        first_name = name.split(" ")[0].lower()
        email = f"{first_name}@example.com"
        purchase_amount = round(random.uniform(10.0, 1000.0), 2)
        year = random.randint(2018, 2024)
        month = random.randint(1, 12)
        day = random.randint(1, 28)
        purchase_date = datetime.date(year, month, day).isoformat()
        customer = {
            "customer_id": i,
            "name": name,
            "email": email,
            "purchase_amount": purchase_amount,
            "purchase_date": purchase_date,
        }
        customers.append(customer)
    return customers


def write_to_json(data, filename):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)


# Generate 5000 more records
cust_data = generate_customer_data(5000)

# Write to a new JSON file
write_to_json(cust_data, "data/CustData.json")
