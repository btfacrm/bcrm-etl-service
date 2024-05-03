import json
import string
import random
import csv
from faker import Faker
from datetime import datetime, timedelta

# Initialize Faker to generate fake data
fake = Faker()

VIEW_NAME = "account"

# Function to generate a single record
def generate_record(index):
    tier_level = fake.random_element(elements=(103, 302, 305, 315, 102))
    tier_description = fake.random_element(elements=('Estate',
                                                     'Community Development',
                                                     'Operations & Maintenance',
                                                     'Education',
                                                     'Operations & Maintenance',
                                                     'Adult Non-Compos Mentis'
                                                     ))
    type_code = fake.random_element(elements=(100, 200, 300, 400, 500))
    type_description = fake.random_element(elements=('IIM Accounts',
                                                     'House Accounts',
                                                     'Tribal Accounts',
                                                     'IIM POOL ACCOUNTS'
                                                     ))
    category_code = fake.random_element(elements=(101, 103, 105, 201, 202))
    category_description = fake.random_element(elements=('House',
                                                     'Escrow',
                                                     'Oil & Gas',
                                                     'Tribal Deposit Fund',
                                                     'Original Allottee',
                                                     'Holding Account for Ad Valerom',
                                                     'Forestry Management Deduction',
                                                     'Alaskan Native Escrow Sttlmnt'
                                                     ))
    freeze_code = fake.random_element(elements=('W01', 'W06', 'KAP', 'W03', 'W06'))
    freeze_description = fake.random_element(elements=('WAU = NCOA',
                                                     'WAU = Correspondence Check Return',
                                                     'Kennerly Appeal Pending',
                                                     'WAU = Awaiting Address Confim',
                                                     'WAU = Fee Only'
                                                     ))
    admin_officer_id = "1"
    admin_officer_name = "John Smith"
    active_flag = random.choice([True, False])
    open_date = fake.date_between_dates(datetime(2000, 1, 1), datetime(2023, 12, 31))
    close_date = fake.date_between_dates(datetime(2000, 1, 1), datetime(2023, 12, 31))
    close_flag = random.choice([True, False])
    
    translator = str.maketrans('', '', string.punctuation + "\n")
    line1 = fake.text().translate(translator)
    line2 = fake.text().translate(translator)
    line3 = fake.text().translate(translator)
    line4 = fake.text().translate(translator)
    date = fake.date_time_between_dates(datetime(2023, 1, 1), datetime(2024, 4, 1))
    statement_date = fake.date_time_between_dates(datetime(2023, 1, 1), datetime(2024, 4, 1))
    
    return {
        "account": "960U0" + str(index),
        "contactId": str(index),
        "tierLevelCode": tier_level,
        "tierLevelDescription": tier_description,
        "typeCode": type_code,
        "typeDescription": type_description,        
        "categoryCode": category_code,
        "categoryDescription": category_description,        
        "freezeCode": freeze_code,
        "freezeDescription": freeze_description, 
        "adminOfficerId": admin_officer_id,
        "adminOfficerName": admin_officer_name,
        "activeFlag": active_flag,
        "openedDate": open_date.strftime('%Y-%m-%d'),
        "closedDate": close_date.strftime('%Y-%m-%d'),
        "closedFlag": close_flag,
        "line1": line1[:40],
        "line2": line2[:40],
        "line3": line3[:40],
        "line4": line4[:40],
        "date": date,
        "statementDate": statement_date
    }

# Generate records
records = [generate_record(70000 + i) for i in range(20)]

# Custom function to convert datetime values to string with different formats for JSON
def convert_date_to_json_string(value):
    if isinstance(value, datetime):
        return value.strftime('%Y-%m-%dT%H:%M:%SZ')
    return value

# Write records to a JSON file
with open(VIEW_NAME + '.json', 'w') as f:
    json.dump(records, f, indent=4, default=convert_date_to_json_string )
    
print("Fake records generated and saved to " + VIEW_NAME + ".json")

# Change field names
for record in records:
    record['CustomerAccountNumber'] = record.pop('account')
    record['OwnerContactID'] = record.pop('contactId')
    record['AccountTierLevelNum'] = record.pop('tierLevelCode')
    record['AccountTierLevelDesc'] = record.pop('tierLevelDescription')
    record['AccountTypeCode'] = record.pop('typeCode')
    record['AccountTypeDescription'] = record.pop('typeDescription')
    record['AccountCategoryCode'] = record.pop('categoryCode')
    record['AccountCategoryDescription'] = record.pop('categoryDescription')
    record['FreezeCode'] = record.pop('freezeCode')
    record['FreezeDesc'] = record.pop('freezeDescription')
    record['AdminOfficerContactID'] = record.pop('adminOfficerId')
    record['AdministratorName'] = record.pop('adminOfficerName')
    record['ActiveFlag'] = record.pop('activeFlag')
    record['DateOpened'] = record.pop('openedDate')
    record['ClosedDate'] = record.pop('closedDate')
    record['ClosedFlag'] = record.pop('closedFlag')
    record['CustomerDescriptionLine1'] = record.pop('line1')
    record['CustomerDescriptionLine2'] = record.pop('line2')
    record['CustomerDescriptionLine3'] = record.pop('line3')
    record['CustomerDescriptionLine4'] = record.pop('line4')
    record['ValidFrom'] = record.pop('date')
    record['StatementDateTime'] = record.pop('statementDate')
    
# Update values for database
for record in records:
    record['ClosedFlag'] = -1 if record['ClosedFlag'] == 'true' else 0
    record['ActiveFlag'] = -1 if record['ActiveFlag'] == 'true' else 0

# Custom function to convert datetime values to string with different formats for CSV
def convert_date_to_csv_string(value):
    if isinstance(value, datetime):
        return value.strftime('%m/%d/%Y %H:%M:%S.%f')[:-3]
    return value

# Write records to a CSV file
csv_file = VIEW_NAME + '.csv'
with open(csv_file, 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=records[0].keys())
    writer.writeheader()
    for record in records:
        csv_record = {key: convert_date_to_csv_string(value) for key, value in record.items()}
        writer.writerow(csv_record)

print("Fake records saved to " + VIEW_NAME + ".csv")