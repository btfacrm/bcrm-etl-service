import json
import string
import random
import csv
from faker import Faker
from datetime import datetime, timedelta

# Initialize Faker to generate fake data
fake = Faker()

VIEW_NAME = "disbursement"

# Function to generate a single record
def generate_record(index):
    code = fake.random_element(elements=('CASHDEP',
                                        'CASHDSB',
                                        'CHECKDEP',
                                        'CHECKDSB',
                                        'ACHDEP',
                                        'ACHDSB',
                                        'AIPURCH',
                                        'AISELL',
                                        'DIV',
                                        'INT',
                                        'INTOTHER',
                                        'JNLDSB',
                                        'LOANDFLT'
                                        ))
    disbursement_text = "Disbursement"
    debit_credit = fake.random_element(elements=('D','C'))
    status = "SETT"
    settle_flag = random.choice([True, False])
    income_indicator = fake.random_element(elements=('I','P'))
    tax_code = fake.random_element(elements=('163','205','304','901'))
    tax_year = fake.random_element(elements=('2020','2021','2022','2023','2024'))
    date = fake.date_time_between_dates(datetime(2023, 1, 1), datetime(2024, 4, 1))
    
    return {
        "transaction": str(index),
        "code": code,
        "disbursementText": disbursement_text,
        "account": "960U0" + str(index),
        "debitCreditIndicator": debit_credit,
        "amount": index,
        "settleDate": date,
        "status": status,
        "settleFlag": settle_flag,
        "incomeIndicator": income_indicator,
        "taxCode": tax_code,
        "taxYear": tax_year,
        "date": date
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