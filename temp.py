import json

# Load JSON data from a file

with open('data.json', 'r') as file:
    data = json.load(file)

companyNames = set()

for row in data:
    companyNames.add(row["company"])

with open('company_names.json', 'w') as file:
    json.dump(list(companyNames), file, indent=4)

