import pandas as pd
import json

# Read Kaggle dataset
input_file = "datasets/insurance_customer_reviews_gemini_enhanced.csv"

df = pd.read_csv(input_file)

# Select required columns
columns = [
    "ReviewID",
    "CustomerID",
    "ReviewDate",
    "Rating",
    "ReviewText",
    "Sentiment",
    "GeneratedTask",
    "AIGenerated"
]

df = df[columns]

# Rename columns
df.columns = [
    "review_id",
    "customer_id",
    "review_date",
    "rating",
    "review_text",
    "sentiment",
    "generated_task",
    "ai_generated"
]

# Convert data types
df["review_id"] = df["review_id"].astype(int)
df["customer_id"] = df["customer_id"].astype(int)
df["rating"] = df["rating"].astype(int)
df["ai_generated"] = df["ai_generated"].astype(bool)

# Convert date to string
df["review_date"] = df["review_date"].astype(str)

# Convert DataFrame to list of dictionaries
data = df.to_dict(orient="records")

# Create JSON file
output_file = "datasets/customer_service_application.json"

with open(output_file, "w", encoding="utf-8") as json_file:
    json.dump(data, json_file, indent=2, ensure_ascii=False)

print("CSV converted to JSON successfully.")
print("Records:", len(data))
print("Created:", output_file)