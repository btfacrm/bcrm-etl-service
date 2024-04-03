import json
import random
import csv
from faker import Faker
from datetime import datetime, timedelta

# Initialize Faker to generate fake data
fake = Faker()

# Function to generate a single record
def generate_record(index):
    first_name = fake.first_name()
    last_name = fake.last_name()
    middle_name = fake.first_name()
    full_name = f"{first_name} {middle_name} {last_name}"
    gender = fake.random_element(elements=('M', 'F'))
    ssn = random.randint(100000000, 999999999)
    ssn_flag = fake.random_element(elements=(True, False))
    dob = fake.date_of_birth(None, 18, 80)
    dod = fake.date_between_dates(datetime(2020, 1, 1), datetime(2023, 12, 31))
    active_flag = random.choice([True, False])
    disbursement_flag = fake.random_element(elements=(True, False))
    date = fake.date_time_between_dates(datetime(2023, 1, 1), datetime(2024, 4, 1))

    return {
        "contactId": str(index),
        "firstName": first_name,
        "lastName": last_name,
        "middleInitial": middle_name,
        "name": full_name,
        "gender": gender,
        "ssn": str(ssn),
        "ssnFlag": ssn_flag,
        "dob": dob.strftime('%Y-%m-%d'),
        "dod": dod.strftime('%Y-%m-%d'),
        "activeFlag": active_flag,
        "disbursementFlag": disbursement_flag,
        "date": date
    }

# Generate records
records = [generate_record(70000 + i) for i in range(10000)]

# Custom function to convert datetime values to string with different formats for JSON
def convert_date_to_json_string(value):
    if isinstance(value, datetime):
        return value.strftime('%Y-%m-%dT%H:%M:%SZ')
    return value

# Write records to a JSON file
with open('contacts.json', 'w') as f:
    json.dump(records, f, indent=4, default=convert_date_to_json_string )
    
print("Fake records generated and saved to 'contacts.json'")

# Change field names
for record in records:
    record['ContactID'] = record.pop('contactId')
    record['PrimaryFirstName'] = record.pop('firstName')
    record['PrimaryLastName'] = record.pop('lastName')
    record['PrimaryMiddleInitial'] = record.pop('middleInitial')
    record['ContactName'] = record.pop('name')
    record['PrimaryGender'] = record.pop('gender')
    record['SSN'] = record.pop('ssn')
    record['SSNFlag'] = record.pop('ssnFlag')
    record['DateOfBirth'] = record.pop('dob')
    record['DateOfDeath'] = record.pop('dod')
    record['ActiveFlag'] = record.pop('activeFlag')
    record['DisbursementEligibilityFlag'] = record.pop('disbursementFlag')
    record['ValidFrom'] = record.pop('date')

# Update values for database
for record in records:
    record['SSNFlag'] = -1 if record['SSNFlag'] == 'true' else 0
    record['ActiveFlag'] = -1 if record['ActiveFlag'] == 'true' else 0
    record['DisbursementEligibilityFlag'] = -1 if record['DisbursementEligibilityFlag'] == 'true' else 0

# Custom function to convert datetime values to string with different formats for CSV
def convert_date_to_csv_string(value):
    if isinstance(value, datetime):
        return value.strftime('%m/%d/%Y %H:%M:%S.%f')[:-3]
    return value

# Write records to a CSV file
csv_file = 'contacts.csv'
with open(csv_file, 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=records[0].keys())
    writer.writeheader()
    for record in records:
        csv_record = {key: convert_date_to_csv_string(value) for key, value in record.items()}
        writer.writerow(csv_record)

print("Fake records saved to 'contacts.csv'")
