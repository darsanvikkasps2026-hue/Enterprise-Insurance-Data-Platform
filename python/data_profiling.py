from pathlib import Path
import pandas as pd
import re
import xml.etree.ElementTree as ET


# ============================================================
# PROJECT PATHS
# ============================================================

BASE_DIR = Path(__file__).resolve().parent.parent

# Existing dataset folder - DO NOT MOVE OR RENAME FILES
DATASET_DIR = BASE_DIR / "datasets"

# Report output folder
REPORT_DIR = BASE_DIR / "reports"
REPORT_DIR.mkdir(exist_ok=True)


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def profile_dataframe(df, dataset_name):
    """Create column-level profiling information."""

    rows = []

    for column in df.columns:
        series = df[column]

        missing_count = series.isna().sum()
        unique_count = series.nunique(dropna=True)

        rows.append({
            "Dataset": dataset_name,
            "Column": column,
            "Data Type": str(series.dtype),
            "Total Rows": len(df),
            "Missing Count": missing_count,
            "Missing Percentage": round(
                (missing_count / len(df)) * 100, 2
            ) if len(df) > 0 else 0,
            "Unique Values": unique_count,
            "Duplicate Values": len(series) - unique_count - missing_count
        })

    return pd.DataFrame(rows)


def dataset_summary(df, dataset_name):
    """Create dataset-level summary."""

    return {
        "Dataset": dataset_name,
        "Rows": len(df),
        "Columns": len(df.columns),
        "Duplicate Rows": int(df.duplicated().sum()),
        "Memory Usage (KB)": round(
            df.memory_usage(deep=True).sum() / 1024, 2
        )
    }


# ============================================================
# 1. CUSTOMER PROFILE - JS FILE
# ============================================================

def read_customer_profile_js(file_path):
    """
    Read customer profile records from the existing JavaScript file.
    The original file is only read; it is never modified.
    """

    text = file_path.read_text(
        encoding="utf-8-sig"
    )

    records = []

    # Find JavaScript objects containing customer_id.
    # This approach does not assume a particular order of fields.
    object_pattern = re.compile(
        r'\{(.*?)\}',
        re.DOTALL
    )

    for obj in object_pattern.findall(text):

        if "customer_id" not in obj:
            continue

        record = {}

        # Extract key/value pairs such as:
        # customer_id: 123
        # customer_id: "123"
        # customer_id: '123'
        pairs = re.findall(
            r'["\']?([A-Za-z_][A-Za-z0-9_]*)["\']?\s*:\s*'
            r'(?:"([^"]*)"|\'([^\']*)\'|([^,\n}]+))',
            obj
        )

        for key, double_value, single_value, plain_value in pairs:

            if double_value != "":
                value = double_value
            elif single_value != "":
                value = single_value
            else:
                value = plain_value.strip()

            record[key] = value

        if "customer_id" in record:
            records.append(record)

    if not records:
        raise ValueError(
            f"Could not extract customer records from {file_path.name}"
        )

    df = pd.DataFrame(records)

    # Keep the expected customer-profile fields when they exist.
    expected_columns = [
        "DateOfBirth",
        "gender",
        "State",
        "customer_id"
    ]

    existing_columns = [
        col for col in expected_columns
        if col in df.columns
    ]

    if existing_columns:
        df = df[existing_columns]

    return df


# ============================================================
# 2. CUSTOMER DETAILS - SQL FILE
# ============================================================

def read_customer_details_sql(file_path):
    """
    Read customer details from the existing PostgreSQL SQL file.

    The source SQL file is only read.
    It is never modified, renamed, or moved.
    """

    text = file_path.read_text(
        encoding="utf-8-sig"
    )

    records = []

    # Actual format in the file:
    #
    # INSERT INTO stg.stg_customer_details
    # (customer_id, Contact, Segment)
    # VALUES
    # (21868593,E'789-916-8172',E'Platinum');

    pattern = re.compile(
        r"VALUES\s*"
        r"\(\s*(\d+)\s*,\s*"
        r"E?'([^']*)'\s*,\s*"
        r"E?'([^']*)'\s*\)",
        re.IGNORECASE
    )

    matches = pattern.findall(text)

    for customer_id, contact, segment in matches:

        records.append({
            "customer_id": customer_id,
            "Contact": contact,
            "Segment": segment
        })

    if not records:
        raise ValueError(
            f"Could not extract customer records from {file_path.name}"
        )

    return pd.DataFrame(records)

def read_claim_xml(file_path):
    """
    Read claim records from the existing XML file.

    The XML source file is only read.
    It is never modified, renamed, or moved.
    """

    tree = ET.parse(file_path)
    root = tree.getroot()

    records = []

    for element in root.iter():

        children = list(element)

        if not children:
            continue

        # Remove XML namespace if present
        child_tags = {
            child.tag.split("}")[-1]
            for child in children
        }

        # A claim record contains customer_id
        if "customer_id" not in child_tags:
            continue

        record = {}

        for child in children:

            tag = child.tag.split("}")[-1]

            value = child.text

            if value is not None:
                value = value.strip()

            record[tag] = value

        if record:
            records.append(record)

    if not records:
        raise ValueError(
            f"Could not extract claim records from {file_path.name}"
        )

    return pd.DataFrame(records)

# ============================================================
# MAIN PROGRAM
# ============================================================

print("=" * 70)
print("ENTERPRISE INSURANCE DATA PLATFORM")
print("DATA PROFILING")
print("=" * 70)

print(f"\nProject directory:")
print(BASE_DIR)

print(f"\nDataset directory:")
print(DATASET_DIR)


# Check dataset folder
if not DATASET_DIR.exists():
    raise FileNotFoundError(
        f"Dataset folder does not exist:\n{DATASET_DIR}"
    )


# ============================================================
# FILE LOCATIONS
# ============================================================

customer_profile_file = (
    DATASET_DIR / "dataset_1_customer_profile (1).js"
)

customer_details_file = (
    DATASET_DIR / "customer details.txt.sql"
)

claims_file = (
    DATASET_DIR / "insurance_claims_with_customer_id (1).csv"
)

claim_details_file = (
    DATASET_DIR / "dataset_3_claim_details (1).csv"
)

xml_file = (
    DATASET_DIR / "claim cleaned.xml"
)

health_file = (
    DATASET_DIR / "datset health insurance.csv"
)


# ============================================================
# CHECK FILES
# ============================================================

files_to_check = [
    customer_profile_file,
    customer_details_file,
    claims_file,
    claim_details_file,
    xml_file,
    health_file
]

print("\nChecking dataset files...")

for file in files_to_check:

    if file.exists():
        print(f"[OK] {file.name}")
    else:
        print(f"[MISSING] {file.name}")


# ============================================================
# READ DATASETS
# ============================================================

print("\nReading datasets...")


# Customer Profile
customer_profile = read_customer_profile_js(
    customer_profile_file
)

print(
    f"[OK] Customer Profile: "
    f"{customer_profile.shape[0]} rows, "
    f"{customer_profile.shape[1]} columns"
)


# Customer Details
customer_details = read_customer_details_sql(
    customer_details_file
)

print(
    f"[OK] Customer Details: "
    f"{customer_details.shape[0]} rows, "
    f"{customer_details.shape[1]} columns"
)


# Insurance Claims
claims = pd.read_csv(
    claims_file
)

print(
    f"[OK] Insurance Claims: "
    f"{claims.shape[0]} rows, "
    f"{claims.shape[1]} columns"
)


# Claim Details
claim_details = pd.read_csv(
    claim_details_file
)

print(
    f"[OK] Claim Details: "
    f"{claim_details.shape[0]} rows, "
    f"{claim_details.shape[1]} columns"
)


# Cleaned Claims XML
cleaned_claims = read_claim_xml(
    xml_file
)

print(
    f"[OK] Cleaned Claims XML: "
    f"{cleaned_claims.shape[0]} rows, "
    f"{cleaned_claims.shape[1]} columns"
)


# Health Insurance
health_insurance = pd.read_csv(
    health_file
)

print(
    f"[OK] Health Insurance: "
    f"{health_insurance.shape[0]} rows, "
    f"{health_insurance.shape[1]} columns"
)


# ============================================================
# CREATE DATASET SUMMARY
# ============================================================

datasets = {
    "Customer Profile": customer_profile,
    "Customer Details": customer_details,
    "Insurance Claims": claims,
    "Claim Details": claim_details,
    "Cleaned Claims": cleaned_claims,
    "Health Insurance": health_insurance
}


summary_rows = []

for name, df in datasets.items():
    summary_rows.append(
        dataset_summary(df, name)
    )

summary_df = pd.DataFrame(summary_rows)


# ============================================================
# CREATE COLUMN PROFILE
# ============================================================

print("\nGenerating column profiles...")

profile_list = []

for name, df in datasets.items():

    profile = profile_dataframe(
        df,
        name
    )

    profile_list.append(profile)


column_profile_df = pd.concat(
    profile_list,
    ignore_index=True
)


# ============================================================
# CREATE CATEGORICAL PROFILE
# ============================================================

categorical_rows = []

for name, df in datasets.items():

    for column in df.columns:

        if (
            df[column].dtype == "object"
            or str(df[column].dtype).startswith("string")
        ):

            value_counts = (
                df[column]
                .fillna("MISSING")
                .value_counts()
                .head(20)
            )

            for value, count in value_counts.items():

                categorical_rows.append({
                    "Dataset": name,
                    "Column": column,
                    "Value": value,
                    "Count": int(count)
                })


categorical_profile_df = pd.DataFrame(
    categorical_rows
)


# ============================================================
# EXPORT EXCEL REPORT
# ============================================================

report_file = (
    REPORT_DIR / "Data_Profiling_Report.xlsx"
)

print("\nCreating Excel report...")

with pd.ExcelWriter(
    report_file,
    engine="openpyxl"
) as writer:

    summary_df.to_excel(
        writer,
        sheet_name="Dataset Summary",
        index=False
    )

    column_profile_df.to_excel(
        writer,
        sheet_name="Column Profile",
        index=False
    )

    categorical_profile_df.to_excel(
        writer,
        sheet_name="Categorical Profile",
        index=False
    )


# ============================================================
# FINAL OUTPUT
# ============================================================

print("\n" + "=" * 70)
print("DATA PROFILING COMPLETED SUCCESSFULLY")
print("=" * 70)

print(f"\nReport created at:")
print(report_file)

print("\nDatasets profiled:")

for name, df in datasets.items():

    print(
        f"  {name}: "
        f"{len(df)} rows × {len(df.columns)} columns"
    )

print("\nNo source files were modified, renamed, moved, or deleted.")