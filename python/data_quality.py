from pathlib import Path
import pandas as pd
import re
import xml.etree.ElementTree as ET


# ============================================================
# PROJECT PATHS
# ============================================================

BASE_DIR = Path(__file__).resolve().parent.parent

DATASET_DIR = BASE_DIR / "datasets"

REPORT_DIR = BASE_DIR / "reports"
REPORT_DIR.mkdir(exist_ok=True)


# ============================================================
# DATA READING FUNCTIONS
# ============================================================

def read_customer_profile_js(file_path):

    text = file_path.read_text(
        encoding="utf-8-sig"
    )

    records = []

    object_pattern = re.compile(
        r'\{(.*?)\}',
        re.DOTALL
    )

    for obj in object_pattern.findall(text):

        if "customer_id" not in obj:
            continue

        record = {}

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
            f"Could not read customer profile: {file_path.name}"
        )

    return pd.DataFrame(records)


def read_customer_details_sql(file_path):

    text = file_path.read_text(
        encoding="utf-8-sig"
    )

    records = []

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
            f"Could not read customer details: {file_path.name}"
        )

    return pd.DataFrame(records)


def read_claim_xml(file_path):

    tree = ET.parse(file_path)

    root = tree.getroot()

    records = []

    for element in root.iter():

        children = list(element)

        if not children:
            continue

        child_tags = {
            child.tag.split("}")[-1]
            for child in children
        }

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
            f"Could not read claim XML: {file_path.name}"
        )

    return pd.DataFrame(records)


# ============================================================
# LOAD DATASETS
# ============================================================

print("=" * 70)
print("ENTERPRISE INSURANCE DATA PLATFORM")
print("DATA QUALITY VALIDATION")
print("=" * 70)

print("\nDataset directory:")
print(DATASET_DIR)


customer_profile = read_customer_profile_js(
    DATASET_DIR / "dataset_1_customer_profile (1).js"
)

customer_details = read_customer_details_sql(
    DATASET_DIR / "customer details.txt.sql"
)

claims = pd.read_csv(
    DATASET_DIR / "insurance_claims_with_customer_id (1).csv"
)

claim_details = pd.read_csv(
    DATASET_DIR / "dataset_3_claim_details (1).csv"
)

cleaned_claims = read_claim_xml(
    DATASET_DIR / "claim cleaned.xml"
)

health_insurance = pd.read_csv(
    DATASET_DIR / "datset health insurance.csv"
)


print("\nDatasets loaded successfully.")


# ============================================================
# STANDARDIZE CUSTOMER IDs FOR COMPARISON
# ============================================================

customer_profile_ids = set(
    customer_profile["customer_id"]
    .astype(str)
    .str.strip()
)

customer_details_ids = set(
    customer_details["customer_id"]
    .astype(str)
    .str.strip()
)

claims_ids = set(
    claims["customer_id"]
    .astype(str)
    .str.strip()
)

claim_details_ids = set(
    claim_details["customer_id"]
    .astype(str)
    .str.strip()
)

cleaned_claims_ids = set(
    cleaned_claims["customer_id"]
    .astype(str)
    .str.strip()
)

health_customer_ids = set(
    health_insurance["customer_id"]
    .dropna()
    .astype(str)
    .str.strip()
)


# ============================================================
# QUALITY RESULTS
# ============================================================

quality_results = []


def add_result(
    category,
    dataset,
    field,
    issue,
    count,
    total,
    severity,
    action
):

    percentage = (
        round((count / total) * 100, 2)
        if total > 0
        else 0
    )

    quality_results.append({

        "Category": category,

        "Dataset": dataset,

        "Field": field,

        "Issue": issue,

        "Affected Records": count,

        "Total Records": total,

        "Percentage": percentage,

        "Severity": severity,

        "Recommended Action": action
    })


# ============================================================
# 1. DUPLICATE RECORD CHECKS
# ============================================================

for name, df in {
    "Customer Profile": customer_profile,
    "Customer Details": customer_details,
    "Insurance Claims": claims,
    "Claim Details": claim_details,
    "Cleaned Claims": cleaned_claims,
    "Health Insurance": health_insurance
}.items():

    duplicate_count = int(
        df.duplicated().sum()
    )

    add_result(
        "Duplicate Check",
        name,
        "All Columns",
        "Duplicate complete records",
        duplicate_count,
        len(df),
        "HIGH" if duplicate_count > 0 else "PASS",
        "Investigate and remove duplicates during cleaning"
        if duplicate_count > 0
        else "No action required"
    )


# ============================================================
# 2. CUSTOMER ID DUPLICATES
# ============================================================

for name, df in {
    "Customer Profile": customer_profile,
    "Customer Details": customer_details
}.items():

    duplicate_ids = int(
        df["customer_id"].duplicated().sum()
    )

    add_result(
        "Duplicate Customer ID",
        name,
        "customer_id",
        "Duplicate customer IDs",
        duplicate_ids,
        len(df),
        "HIGH" if duplicate_ids > 0 else "PASS",
        "Investigate duplicate master records"
        if duplicate_ids > 0
        else "No action required"
    )


# ============================================================
# 3. MISSING VALUES
# ============================================================

for name, df in {
    "Customer Profile": customer_profile,
    "Customer Details": customer_details,
    "Insurance Claims": claims,
    "Claim Details": claim_details,
    "Cleaned Claims": cleaned_claims,
    "Health Insurance": health_insurance
}.items():

    for column in df.columns:

        missing = int(
            df[column].isna().sum()
        )

        if missing > 0:

            severity = "HIGH"

            if missing / len(df) < 0.05:
                severity = "MEDIUM"

            if missing / len(df) >= 0.50:
                severity = "HIGH"

            add_result(
                "Missing Value",
                name,
                column,
                "Missing values detected",
                missing,
                len(df),
                severity,
                "Investigate source and apply appropriate imputation or Unknown value"
            )


# ============================================================
# 4. CLAIM AMOUNT VALIDATION
# ============================================================

claim_amount_columns = [
    "total_claim_amount",
    "injury_claim",
    "property_claim",
    "vehicle_claim"
]

for column in claim_amount_columns:

    if column in claims.columns:

        numeric_values = pd.to_numeric(
            claims[column],
            errors="coerce"
        )

        invalid = int(
            (numeric_values < 0).sum()
        )

        add_result(
            "Invalid Numeric Value",
            "Insurance Claims",
            column,
            "Negative claim amounts",
            invalid,
            len(claims),
            "HIGH" if invalid > 0 else "PASS",
            "Investigate invalid claim amount"
            if invalid > 0
            else "No action required"
        )


# ============================================================
# 5. CLAIM COMPONENT CONSISTENCY
# ============================================================

if all(
    column in claims.columns
    for column in claim_amount_columns
):

    total_claim = pd.to_numeric(
        claims["total_claim_amount"],
        errors="coerce"
    )

    component_total = (
        pd.to_numeric(
            claims["injury_claim"],
            errors="coerce"
        )
        +
        pd.to_numeric(
            claims["property_claim"],
            errors="coerce"
        )
        +
        pd.to_numeric(
            claims["vehicle_claim"],
            errors="coerce"
        )
    )

    mismatch = int(
        (total_claim != component_total).sum()
    )

    add_result(
        "Business Rule",
        "Insurance Claims",
        "Claim Amount Components",
        "Total claim does not equal injury + property + vehicle claim",
        mismatch,
        len(claims),
        "HIGH" if mismatch > 0 else "PASS",
        "Investigate claim amount calculation"
        if mismatch > 0
        else "No action required"
    )


# ============================================================
# 6. POLICY PREMIUM VALIDATION
# ============================================================

premium = pd.to_numeric(
    claims["policy_annual_premium"],
    errors="coerce"
)

negative_premium = int(
    (premium <= 0).sum()
)

add_result(
    "Invalid Numeric Value",
    "Insurance Claims",
    "policy_annual_premium",
    "Zero or negative policy premium",
    negative_premium,
    len(claims),
    "HIGH" if negative_premium > 0 else "PASS",
    "Investigate invalid premium values"
    if negative_premium > 0
    else "No action required"
)


# ============================================================
# 7. PREMIUM OUTLIER CHECK
# ============================================================

q1 = premium.quantile(0.25)

q3 = premium.quantile(0.75)

iqr = q3 - q1

upper_bound = q3 + (1.5 * iqr)

premium_outliers = int(
    (premium > upper_bound).sum()
)

add_result(
    "Statistical Outlier",
    "Insurance Claims",
    "policy_annual_premium",
    "Premium values above IQR upper bound",
    premium_outliers,
    len(claims),
    "REVIEW" if premium_outliers > 0 else "PASS",
    "Review outliers; do not automatically delete valid business records"
    if premium_outliers > 0
    else "No action required"
)


# ============================================================
# 8. UMBRELLA LIMIT VALIDATION
# ============================================================

if "umbrella_limit" in claims.columns:

    umbrella = pd.to_numeric(
        claims["umbrella_limit"],
        errors="coerce"
    )

    invalid_umbrella = int(
        (umbrella < 0).sum()
    )

    add_result(
        "Business Rule",
        "Insurance Claims",
        "umbrella_limit",
        "Negative umbrella limit",
        invalid_umbrella,
        len(claims),
        "HIGH" if invalid_umbrella > 0 else "PASS",
        "Investigate negative umbrella limits"
        if invalid_umbrella > 0
        else "No action required"
    )


# ============================================================
# 9. UNKNOWN / '?' VALUES
# ============================================================

for name, df in {
    "Insurance Claims": claims,
    "Claim Details": claim_details,
    "Cleaned Claims": cleaned_claims,
    "Health Insurance": health_insurance
}.items():

    for column in df.columns:

        unknown_count = int(
            (
                df[column]
                .astype(str)
                .str.strip()
                .eq("?")
            ).sum()
        )

        if unknown_count > 0:

            add_result(
                "Invalid / Unknown Value",
                name,
                column,
                "Question-mark placeholder detected",
                unknown_count,
                len(df),
                "MEDIUM",
                "Standardize '?' to an appropriate Unknown/null representation"
            )


# ============================================================
# 10. REFERENTIAL INTEGRITY
# ============================================================

missing_customer_details = (
    customer_details_ids -
    customer_profile_ids
)

add_result(
    "Referential Integrity",
    "Customer Details",
    "customer_id",
    "Customer IDs missing from Customer Profile",
    len(missing_customer_details),
    len(customer_details),
    "HIGH" if missing_customer_details else "PASS",
    "Investigate unmatched customer master records"
    if missing_customer_details
    else "No action required"
)


missing_claims = (
    claims_ids -
    customer_profile_ids
)

add_result(
    "Referential Integrity",
    "Insurance Claims",
    "customer_id",
    "Claim customer IDs missing from Customer Profile",
    len(missing_claims),
    len(claims),
    "HIGH" if missing_claims else "PASS",
    "Investigate unmatched customer IDs"
    if missing_claims
    else "No action required"
)


missing_claim_details = (
    claim_details_ids -
    customer_profile_ids
)

add_result(
    "Referential Integrity",
    "Claim Details",
    "customer_id",
    "Claim detail customer IDs missing from Customer Profile",
    len(missing_claim_details),
    len(claim_details),
    "HIGH" if missing_claim_details else "PASS",
    "Investigate unmatched customer IDs"
    if missing_claim_details
    else "No action required"
)


missing_cleaned_claims = (
    cleaned_claims_ids -
    customer_profile_ids
)

add_result(
    "Referential Integrity",
    "Cleaned Claims",
    "customer_id",
    "XML claim customer IDs missing from Customer Profile",
    len(missing_cleaned_claims),
    len(cleaned_claims),
    "HIGH" if missing_cleaned_claims else "PASS",
    "Investigate unmatched customer IDs"
    if missing_cleaned_claims
    else "No action required"
)


# ============================================================
# 11. HEALTH INSURANCE CUSTOMER ID CHECK
# ============================================================

missing_health_ids = (
    health_customer_ids -
    customer_profile_ids
)

add_result(
    "Referential Integrity",
    "Health Insurance",
    "customer_id",
    "Non-null health insurance customer IDs missing from Customer Profile",
    len(missing_health_ids),
    len(health_customer_ids),
    "HIGH" if missing_health_ids else "PASS",
    "Investigate unmatched customer IDs"
    if missing_health_ids
    else "No action required"
)


# ============================================================
# 12. HEALTH INSURANCE NEGATIVE VALUES
# ============================================================

for column in [
    "premiums_written",
    "losses_paid",
    "taxes_paid"
]:

    if column in health_insurance.columns:

        values = pd.to_numeric(
            health_insurance[column],
            errors="coerce"
        )

        negative_count = int(
            (values < 0).sum()
        )

        add_result(
            "Invalid Numeric Value",
            "Health Insurance",
            column,
            "Negative financial value",
            negative_count,
            len(health_insurance),
            "HIGH" if negative_count > 0 else "PASS",
            "Investigate negative financial values according to source business rules"
            if negative_count > 0
            else "No action required"
        )


# ============================================================
# 13. CUSTOMER MASTER CONSISTENCY
# ============================================================

if (
    "gender" in customer_profile.columns
    and "insured_sex" in claims.columns
    and "customer_id" in claims.columns
):

    master_gender = customer_profile[
        ["customer_id", "gender"]
    ].copy()

    master_gender["customer_id"] = (
        master_gender["customer_id"]
        .astype(str)
        .str.strip()
    )

    master_gender["gender"] = (
        master_gender["gender"]
        .astype(str)
        .str.strip()
        .str.upper()
    )

    claim_gender = claims[
        ["customer_id", "insured_sex"]
    ].copy()

    claim_gender["customer_id"] = (
        claim_gender["customer_id"]
        .astype(str)
        .str.strip()
    )

    claim_gender["insured_sex"] = (
        claim_gender["insured_sex"]
        .astype(str)
        .str.strip()
        .str.upper()
    )

    merged_gender = claim_gender.merge(
        master_gender,
        on="customer_id",
        how="left"
    )

    gender_mismatch = int(
        (
            merged_gender["insured_sex"]
            != merged_gender["gender"]
        ).sum()
    )

    add_result(
        "Cross-Dataset Consistency",
        "Insurance Claims vs Customer Profile",
        "gender / insured_sex",
        "Customer master gender differs from insured sex in claim record",
        gender_mismatch,
        len(merged_gender),
        "HIGH" if gender_mismatch > 0 else "PASS",
        "Investigate source consistency before standardizing"
        if gender_mismatch > 0
        else "No action required"
    )


# ============================================================
# CREATE DATA QUALITY DATAFRAME
# ============================================================

quality_df = pd.DataFrame(
    quality_results
)


# ============================================================
# CREATE SUMMARY
# ============================================================

summary_df = pd.DataFrame({

    "Metric": [
        "Total Quality Checks",
        "Passed Checks",
        "High Severity Issues",
        "Medium Severity Issues",
        "Review Items"
    ],

    "Count": [

        len(quality_df),

        int(
            (quality_df["Severity"] == "PASS").sum()
        ),

        int(
            (quality_df["Severity"] == "HIGH").sum()
        ),

        int(
            (quality_df["Severity"] == "MEDIUM").sum()
        ),

        int(
            (quality_df["Severity"] == "REVIEW").sum()
        )
    ]
})


# ============================================================
# EXPORT REPORT
# ============================================================

report_file = (
    REPORT_DIR / "Data_Quality_Report.xlsx"
)

print("\nCreating Data Quality Report...")

with pd.ExcelWriter(
    report_file,
    engine="openpyxl"
) as writer:

    summary_df.to_excel(
        writer,
        sheet_name="Quality Summary",
        index=False
    )

    quality_df.to_excel(
        writer,
        sheet_name="Quality Issues",
        index=False
    )


# ============================================================
# CONSOLE SUMMARY
# ============================================================

print("\n" + "=" * 70)
print("DATA QUALITY VALIDATION COMPLETED")
print("=" * 70)

print(f"\nReport created at:")
print(report_file)

print("\nQuality Check Summary:")

print(
    f"Total Checks : {len(quality_df)}"
)

print(
    f"PASS         : "
    f"{(quality_df['Severity'] == 'PASS').sum()}"
)

print(
    f"HIGH         : "
    f"{(quality_df['Severity'] == 'HIGH').sum()}"
)

print(
    f"MEDIUM       : "
    f"{(quality_df['Severity'] == 'MEDIUM').sum()}"
)

print(
    f"REVIEW       : "
    f"{(quality_df['Severity'] == 'REVIEW').sum()}"
)

print("\nOriginal datasets were not modified.")