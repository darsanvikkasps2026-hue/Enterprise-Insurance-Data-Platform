import pandas as pd
import json
import re
import xml.etree.ElementTree as ET
from pathlib import Path

# ============================================================
# SPRINT 2 - PHASE 1: DATA PROFILING
# Enterprise Insurance Data Platform
# ============================================================

# Run from repository root:
# python python/data_profiling.py

DATASET_DIR = Path("datasets")
OUTPUT_DIR = Path("profiling_output")
OUTPUT_DIR.mkdir(exist_ok=True)


def load_customer_profile():
    file_path = DATASET_DIR / "dataset_1_customer_profile.js"
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)
    return pd.DataFrame(data["data"])


def load_sql_claims():
    file_path = DATASET_DIR / "customer_details.txt.sql"

    with open(file_path, "r", encoding="utf-8") as file:
        sql_text = file.read()

    pattern = re.compile(
        r"INSERT INTO\s+\S+\s*"
        r"\((.*?)\)\s*VALUES\s*\((.*?)\);",
        re.IGNORECASE
    )

    rows = []

    for match in pattern.finditer(sql_text):
        values_text = match.group(2)

        value_match = re.match(
            r"\s*(\d+)\s*,"
            r"\s*(\d+)\s*,"
            r"E?'([^']*)'\s*,"
            r"'([^']*)'\s*,"
            r"E?'([^']*)'\s*",
            values_text
        )

        if value_match:
            rows.append({
                "customer_id": value_match.group(1),
                "claim_id": value_match.group(2),
                "incident_cause": value_match.group(3),
                "claim_date": value_match.group(4),
                "claim_area": value_match.group(5)
            })

    return pd.DataFrame(rows)


def load_claim_details():
    file_path = DATASET_DIR / "dataset_3_claim_details.csv"
    return pd.read_csv(file_path)


def load_claim_additional_csv():
    file_path = DATASET_DIR / "dataset_4_claim_additional.csv"

    if not file_path.exists():
        return None

    return pd.read_csv(file_path)


def load_customer_additional_xml():
    file_path = DATASET_DIR / "dataset_4_claim_additional.xml"

    if not file_path.exists():
        return None

    root = ET.parse(file_path).getroot()
    rows = []

    for row in root.findall(".//Row"):
        record = {}

        for child in row:
            record[child.tag] = child.text.strip() if child.text else None

        rows.append(record)

    return pd.DataFrame(rows)


def profile_dataset(name, df):
    print("\n" + "=" * 70)
    print(name)
    print("=" * 70)

    print("\nRows:", len(df))
    print("Columns:", len(df.columns))

    print("\nColumn names:")
    print(df.columns.tolist())

    print("\nData types:")
    print(df.dtypes)

    print("\nMissing values:")
    print(df.isnull().sum())

    print("\nDuplicate complete rows:")
    print(df.duplicated().sum())

    print("\nUnique values:")
    for column in df.columns:
        print(f"{column}: {df[column].nunique(dropna=True)}")

    return {
        "dataset": name,
        "rows": len(df),
        "columns": len(df.columns),
        "duplicate_rows": int(df.duplicated().sum()),
        "total_missing_values": int(df.isnull().sum().sum())
    }


def main():

    print("\nSPRINT 2 - PHASE 1")
    print("INSURANCE DATA PROFILING")
    print("=" * 70)

    # --------------------------------------------------------
    # Load datasets
    # --------------------------------------------------------

    customer = load_customer_profile()
    sql_claims = load_sql_claims()
    claim_details = load_claim_details()
    claim_additional_csv = load_claim_additional_csv()
    customer_additional_xml = load_customer_additional_xml()

    results = []

    results.append(
        profile_dataset("Customer Profile - JS/JSON", customer)
    )

    results.append(
        profile_dataset("Claim Details - SQL", sql_claims)
    )

    results.append(
        profile_dataset("Claim Details - CSV", claim_details)
    )

    if claim_additional_csv is not None:
        results.append(
            profile_dataset("Claim Additional - CSV", claim_additional_csv)
        )

    if customer_additional_xml is not None:
        results.append(
            profile_dataset("Customer Additional - XML", customer_additional_xml)
        )

    # --------------------------------------------------------
    # CUSTOMER QUALITY CHECKS
    # --------------------------------------------------------

    print("\n" + "=" * 70)
    print("CUSTOMER DATA QUALITY CHECKS")
    print("=" * 70)

    print("\nCustomer profile duplicate IDs:",
          customer["customer_id"].duplicated().sum())

    print("Customer profile missing IDs:",
          customer["customer_id"].isnull().sum())

    # DOB validation
    dob = pd.to_datetime(
        customer["DateOfBirth"],
        format="%d-%b-%y",
        errors="coerce"
    )

    print("Invalid DateOfBirth values:",
          dob.isnull().sum())

    # --------------------------------------------------------
    # SQL CLAIM QUALITY CHECKS
    # --------------------------------------------------------

    print("\n" + "=" * 70)
    print("SQL CLAIM DATA QUALITY CHECKS")
    print("=" * 70)

    print("\nSQL rows:", len(sql_claims))

    print("Duplicate claim IDs:",
          sql_claims["claim_id"].duplicated().sum())

    print("Missing customer IDs:",
          sql_claims["customer_id"].isnull().sum())

    print("Missing claim IDs:",
          sql_claims["claim_id"].isnull().sum())

    claim_dates = pd.to_datetime(
        sql_claims["claim_date"],
        format="%m/%d/%Y",
        errors="coerce"
    )

    print("Invalid claim dates:",
          claim_dates.isnull().sum())

    # --------------------------------------------------------
    # CLAIM CSV QUALITY CHECKS
    # --------------------------------------------------------

    print("\n" + "=" * 70)
    print("CLAIM CSV DATA QUALITY CHECKS")
    print("=" * 70)

    print("\nCSV rows:", len(claim_details))

    print("Duplicate claim IDs:",
          claim_details["claim_id"].duplicated().sum())

    print("Missing customer IDs:",
          claim_details["customer_id"].isnull().sum())

    print("Missing claim IDs:",
          claim_details["claim_id"].isnull().sum())

    # --------------------------------------------------------
    # CLAIM ADDITIONAL CSV QUALITY CHECKS
    # This is where claim_amount actually exists.
    # --------------------------------------------------------

    if claim_additional_csv is not None:

        print("\n" + "=" * 70)
        print("CLAIM ADDITIONAL CSV QUALITY CHECKS")
        print("=" * 70)

        print("\nRows:", len(claim_additional_csv))

        print("Missing claim amounts:",
              claim_additional_csv["claim_amount"].isnull().sum())

        print("Missing total policy claims:",
              claim_additional_csv["total_policy_claims"].isnull().sum())

        print("Duplicate customer IDs:",
              claim_additional_csv["customer_id"].duplicated().sum())

        claim_amount_numeric = pd.to_numeric(
            claim_additional_csv["claim_amount"]
            .astype("string")
            .str.replace("$", "", regex=False)
            .str.replace(",", "", regex=False)
            .str.strip(),
            errors="coerce"
        )

        print("Invalid claim amounts:",
              claim_amount_numeric.isnull().sum())

        print("Negative claim amounts:",
              (claim_amount_numeric < 0).sum())

        print("\nClaim type values:")
        print(claim_additional_csv["claim_type"].value_counts(dropna=False))

        print("\nPolice report values:")
        print(claim_additional_csv["police_report"].value_counts(dropna=False))

        print("\nFraudulent values:")
        print(claim_additional_csv["fraudulent"].value_counts(dropna=False))

    # --------------------------------------------------------
    # XML QUALITY CHECKS
    # --------------------------------------------------------

    if customer_additional_xml is not None:

        print("\n" + "=" * 70)
        print("XML CUSTOMER DATA QUALITY CHECKS")
        print("=" * 70)

        xml_ids = (
            customer_additional_xml["customer_id"]
            .astype("string")
            .str.strip()
        )

        print("\nXML rows:", len(customer_additional_xml))

        print("Duplicate XML customer IDs:",
              xml_ids.duplicated().sum())

        print("Missing XML customer IDs:",
              xml_ids.isnull().sum())

        print("XML IDs with leading zeros:",
              xml_ids.str.startswith("0").sum())

        print("\nSegment values:")
        print(
            customer_additional_xml["Segment"]
            .value_counts(dropna=False)
        )

    # --------------------------------------------------------
    # Save summary
    # --------------------------------------------------------

    summary = pd.DataFrame(results)

    summary_file = OUTPUT_DIR / "profiling_summary.csv"
    summary.to_csv(summary_file, index=False)

    print("\n" + "=" * 70)
    print("PROFILING COMPLETED")
    print("=" * 70)

    print("\nSummary saved to:")
    print(summary_file)


if __name__ == "__main__":
    main()