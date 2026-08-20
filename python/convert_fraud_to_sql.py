import pandas as pd

# Read Kaggle dataset
df = pd.read_csv("datasets/insurance_data.csv")

# Select only required non-sensitive columns
columns = [
    "TRANSACTION_ID",
    "CUSTOMER_ID",
    "POLICY_NUMBER",
    "LOSS_DT",
    "REPORT_DT",
    "INSURANCE_TYPE",
    "CLAIM_AMOUNT",
    "CLAIM_STATUS",
    "INCIDENT_SEVERITY",
    "AUTHORITY_CONTACTED",
    "ANY_INJURY",
    "POLICE_REPORT_AVAILABLE",
    "INCIDENT_STATE",
    "INCIDENT_CITY",
    "INCIDENT_HOUR_OF_THE_DAY",
    "AGENT_ID",
    "VENDOR_ID"
]

df = df[columns]

# Rename columns
df.columns = [
    "transaction_id",
    "customer_id",
    "policy_number",
    "loss_date",
    "report_date",
    "insurance_type",
    "claim_amount",
    "claim_status",
    "incident_severity",
    "authority_contacted",
    "any_injury",
    "police_report_available",
    "incident_state",
    "incident_city",
    "incident_hour",
    "agent_id",
    "vendor_id"
]

# Create SQL file
output_file = "datasets/fraud_investigation.sql"

with open(output_file, "w", encoding="utf-8") as f:

    f.write("CREATE TABLE fraud_investigation (\n")
    f.write("    transaction_id VARCHAR(20),\n")
    f.write("    customer_id VARCHAR(20),\n")
    f.write("    policy_number VARCHAR(20),\n")
    f.write("    loss_date DATE,\n")
    f.write("    report_date DATE,\n")
    f.write("    insurance_type VARCHAR(50),\n")
    f.write("    claim_amount DECIMAL(12,2),\n")
    f.write("    claim_status VARCHAR(20),\n")
    f.write("    incident_severity VARCHAR(50),\n")
    f.write("    authority_contacted VARCHAR(50),\n")
    f.write("    any_injury INTEGER,\n")
    f.write("    police_report_available INTEGER,\n")
    f.write("    incident_state VARCHAR(10),\n")
    f.write("    incident_city VARCHAR(100),\n")
    f.write("    incident_hour INTEGER,\n")
    f.write("    agent_id VARCHAR(20),\n")
    f.write("    vendor_id VARCHAR(20)\n")
    f.write(");\n\n")

    for _, row in df.iterrows():

        values = []

        for column in df.columns:
            value = row[column]

            if pd.isna(value):
                values.append("NULL")

            elif column in ["loss_date", "report_date"]:
                values.append(f"'{value}'")

            elif column == "claim_amount":
                values.append(str(float(value)))

            elif column in ["any_injury",
                            "police_report_available",
                            "incident_hour"]:
                values.append(str(int(value)))

            else:
                value = str(value).replace("'", "''")
                values.append(f"'{value}'")

        f.write(
            "INSERT INTO fraud_investigation VALUES "
            "(" + ", ".join(values) + ");\n"
        )

print("Created:", output_file)
print("Records:", len(df))