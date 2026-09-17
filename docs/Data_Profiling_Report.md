# Data Profiling Report

## Enterprise Insurance Data Platform

### Sprint 2 — Phase 1: Data Profiling

---

## 1. Objective

The objective of data profiling is to analyze the structure, completeness,
uniqueness, data types, and quality of the insurance datasets before loading
the data into the warehouse.

The profiling was performed using Python and Pandas.

---

## 2. Datasets Profiled

The following datasets were analyzed:

| Dataset | Format | Records | Columns |
|---|---|---:|---:|
| Customer Profile | JS/JSON | 1,085 | 4 |
| Customer Details | SQL | 1,100 | 5 |
| Claim Details | CSV | 1,100 | 5 |
| Claim Additional | CSV | 1,100 | 6 |
| Customer Additional | XML | 1,085 | 3 |

---

## 3. Customer Profile — JS/JSON

### Columns

- DateOfBirth
- gender
- State
- customer_id

### Profiling Results

| Metric | Result |
|---|---:|
| Records | 1,085 |
| Columns | 4 |
| Missing values | 0 |
| Duplicate complete rows | 0 |
| Unique customer IDs | 1,085 |
| Unique genders | 2 |
| Unique states | 50 |
| Unique DateOfBirth values | 1,085 |

### Observation

The customer profile dataset contains complete records with no missing
values or duplicate customer IDs.

---

## 4. Customer Details — SQL

### Columns

- customer_id
- claim_id
- incident_cause
- claim_date
- claim_area

### Profiling Results

| Metric | Result |
|---|---:|
| Records | 1,100 |
| Columns | 5 |
| Missing values | 0 |
| Duplicate complete rows | 0 |
| Unique customer IDs | 1,093 |
| Unique claim IDs | 1,100 |
| Unique incident causes | 5 |
| Unique claim dates | 100 |
| Unique claim areas | 2 |

### Observation

The dataset contains 1,100 claim records and 1,100 unique claim IDs.
There are 1,093 unique customer IDs because some customers have multiple
claims.

---

## 5. Claim Details — CSV

### Columns

- customer_id
- claim_id
- incident_cause
- claim_date
- claim_area

### Profiling Results

| Metric | Result |
|---|---:|
| Records | 1,100 |
| Columns | 5 |
| Missing values | 0 |
| Duplicate complete rows | 0 |
| Unique customer IDs | 1,093 |
| Unique claim IDs | 1,100 |
| Unique incident causes | 5 |
| Unique claim dates | 100 |
| Unique claim areas | 2 |

### Observation

The CSV claim details dataset is structurally consistent with the SQL
claim dataset.

---

## 6. Claim Additional — CSV

### Columns

- customer_id
- police_report
- claim_type
- claim_amount
- total_policy_claims
- fraudulent

### Profiling Results

| Metric | Result |
|---|---:|
| Records | 1,100 |
| Columns | 6 |
| Missing claim amounts | 65 |
| Missing total policy claims | 10 |
| Duplicate complete rows | 0 |
| Unique customer IDs | 1,093 |
| Unique claim amounts | 683 |
| Unique claim types | 3 |
| Unique police report values | 3 |
| Unique fraudulent values | 2 |

### Claim Type Distribution

| Claim Type | Records |
|---|---:|
| Material only | 663 |
| Material and injury | 241 |
| Injury only | 196 |

### Police Report Distribution

| Police Report | Records |
|---|---:|
| No | 630 |
| Unknown | 300 |
| Yes | 170 |

### Fraudulent Distribution

| Fraudulent | Records |
|---|---:|
| No | 846 |
| Yes | 254 |

---

## 7. Customer Additional — XML

### Columns

- customer_id
- Contact
- Segment

### Profiling Results

| Metric | Result |
|---|---:|
| Records | 1,085 |
| Columns | 3 |
| Missing values | 0 |
| Duplicate complete rows | 0 |
| Unique customer IDs | 1,085 |
| Unique Contact values | 1,085 |
| Unique Segment values | 3 |

### Segment Distribution

| Segment | Records |
|---|---:|
| Gold | 372 |
| Platinum | 364 |
| Silver | 349 |

### Observation

All XML customer IDs contain leading zeros and therefore require
standardization before joining with the other customer datasets.

---

## 8. Claim Date Analysis

The claim dates were validated using the expected format:

`MM/DD/YYYY`

The profiling identified:

- Invalid claim dates: 0
- Claim date range: 2017-01-01 to 2018-10-30

Therefore, the claim date field is suitable for transformation into the
warehouse date dimension.

---

## 9. Overall Profiling Summary

| Dataset | Records | Missing Values | Duplicate Rows |
|---|---:|---:|---:|
| Customer Profile | 1,085 | 0 | 0 |
| Customer Details SQL | 1,100 | 0 | 0 |
| Claim Details CSV | 1,100 | 0 | 0 |
| Claim Additional CSV | 1,100 | 75 | 0 |
| Customer Additional XML | 1,085 | 0 | 0 |

---

## 10. Key Findings

The profiling identified the following important findings:

1. Customer profile data contains no missing values or duplicate customer IDs.

2. Claim details contain 1,100 unique claim IDs.

3. Some customers have multiple claims, which is expected for claim-level
   data and should not be treated as duplicate customer records.

4. 65 claim amount values are missing.

5. 10 total policy claim values are missing.

6. Claim amounts are stored as strings containing currency symbols and
   require conversion to a numeric format.

7. XML customer IDs contain leading zeros and require standardization.

8. Claim dates contain no invalid values.

9. The claim additional dataset contains three claim types and three police
   report categories.

10. The fraudulent field contains two categories: Yes and No.

---

## 11. Output

The Python profiling process generated:

`profiling_output/profiling_summary.csv`

This file contains the high-level profiling summary for the analyzed
datasets.