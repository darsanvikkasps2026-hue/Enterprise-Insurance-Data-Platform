import csv
import json

input_file = "datasets/underwriting.csv"
output_file = "datasets/underwriting.json"

with open(input_file, "r", encoding="utf-8") as csv_file:
    reader = csv.DictReader(csv_file)
    data = list(reader)

for row in data:
    row["age"] = int(row["age"])
    row["bmi"] = float(row["bmi"])
    row["children"] = int(row["children"])
    row["charges"] = float(row["charges"])

with open(output_file, "w", encoding="utf-8") as json_file:
    json.dump(data, json_file, indent=2)

print("CSV converted to JSON successfully.")
print("Records:", len(data))