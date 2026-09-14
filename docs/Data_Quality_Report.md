# Data Quality Report

## Enterprise Insurance Data Platform

### Sprint 2 — Data Quality Assessment

---

## 1. Objective

The objective of the data quality assessment is to identify missing,
duplicate, invalid, inconsistent, and non-standard values in the supplied
insurance datasets before loading them into the data warehouse.

---

## 2. Quality Dimensions

The following data quality dimensions were considered:

- Completeness
- Uniqueness
- Validity
- Consistency
- Standardization

---

## 3. Customer Data Quality

### Customer Profile

The customer profile dataset contains 1,085 records.

Quality results:

| Check | Result | Status |
|---|---:|---|
| Missing customer IDs | 0 | PASS |
| Duplicate customer IDs | 0 | PASS |
| Missing DateOfBirth | 0 | PASS |
| Invalid DateOfBirth values | 0 | PASS |
| Missing gender | 0 | PASS |
| Missing State | 0 | PASS |

The customer profile does not contain missing or duplicate customer IDs.

---

## 4. Claim Data Quality

### Claim Details

The claim details dataset contains 1,100 records.

| Check | Result | Status |
|---|---:|---|
| Missing customer IDs | 0 | PASS |
| Missing claim IDs | 0 | PASS |
| Duplicate claim IDs | 0 | PASS |
| Invalid claim dates | 0 | PASS |
| Duplicate complete rows | 0 | PASS |

The claim data has complete customer and claim identifiers.

---

## 5. Claim Amount Quality

The claim additional dataset contains 1,100 records.

### Missing Claim Amounts

There are:

**65 missing claim amounts**

These records require handling during the data standardization and warehouse
loading process.

Missing claim amounts should not automatically be converted to zero because
zero would represent an actual claim amount rather than missing information.

Recommended treatment:

- Preserve missing values as NULL.
- Document the missing-value rule.
- Allow the business layer to determine whether the values can be recovered
  from another source.

---

## 6. Total Policy Claims Quality

There are:

**10 missing `total_policy_claims` values.**

Recommended treatment:

- Preserve missing values as NULL.
- Do not replace missing values with zero without a confirmed business rule.
- Document the missing values in the data quality report.

---

## 7. Claim Amount Format Issue

The `claim_amount` field is stored as a string and contains currency symbols.

Example format:

`$2980`

Therefore, the field requires standardization before warehouse loading.

Target warehouse format:

`NUMERIC(12,2)`

The transformation should:

1. Remove the `$` symbol.
2. Remove unnecessary spaces.
3. Convert the value to a numeric data type.
4. Preserve missing values as NULL.

No negative claim amounts were identified.

---

## 8. Customer ID Standardization

The XML dataset contains customer IDs with leading zeros.

Example:

`000000021868593`

Other datasets represent the same business identifier without the
leading zeros.

Therefore, customer IDs must be standardized before joining the datasets.

The recommended warehouse representation is:

`VARCHAR(15)`

This preserves the business identifier and prevents loss of leading zeros.

---

## 9. Claim-Level Customer ID Repetition

The claim datasets contain:

- 1,100 claim records
- 1,093 unique customer IDs

This means some customers have multiple claims.

This is **not considered a duplicate customer error** because claims are
transaction-level records and one customer can have multiple claims.

---

## 10. Police Report Quality

The `police_report` field contains three categories:

| Value | Records |
|---|---:|
| No | 630 |
| Unknown | 300 |
| Yes | 170 |

`Unknown` should be retained as a valid source category unless a confirmed
business rule requires it to be transformed into NULL.

---

## 11. Fraudulent Claim Quality

The `fraudulent` field contains:

| Value | Records |
|---|---:|
| No | 846 |
| Yes | 254 |

The field contains two consistent categorical values.

---

## 12. Claim Type Quality

The `claim_type` field contains:

| Claim Type | Records |
|---|---:|
| Material only | 663 |
| Material and injury | 241 |
| Injury only | 196 |

The values are consistent categorical values suitable for standardization.

---

## 13. Date Quality

Claim dates were validated using the expected format:

`MM/DD/YYYY`

Results:

- Invalid claim dates: 0
- Minimum claim date: 2017-01-01
- Maximum claim date: 2018-10-30

Therefore, claim dates can be converted to a standard date format for the
warehouse date dimension.

---

## 14. XML Data Quality

The XML customer dataset contains:

- 1,085 records
- 0 missing customer IDs
- 0 duplicate customer IDs
- 1,085 customer IDs containing leading zeros

The primary quality issue is therefore identifier standardization.

---

## 15. Policy, Product, Agent and Premium Checks

The supplied Sprint 2 datasets do not contain sufficient fields for
comprehensive assessment of:

- Policy master data
- Product master data
- Agent master data
- Premium consistency

Therefore, these quality checks are recorded as:

**Not Assessable from Supplied Datasets**

No artificial or fabricated values have been introduced to perform these
checks.

These checks can be performed when the corresponding source datasets become
available.

---

## 16. Data Quality Issues Summary

| Issue | Records | Severity | Recommended Action |
|---|---:|---|---|
| Missing claim amount | 65 | High | Preserve as NULL and investigate |
| Missing total policy claims | 10 | Medium | Preserve as NULL and investigate |
| XML leading-zero customer IDs | 1,085 | Medium | Standardize customer ID |
| Claim amount stored as string | 1,100 | Medium | Convert to NUMERIC(12,2) |
| Multiple claims per customer | Expected | Low | No correction required |
| Policy data unavailable | N/A | Information gap | Assess when source is available |
| Product data unavailable | N/A | Information gap | Assess when source is available |
| Agent data unavailable | N/A | Information gap | Assess when source is available |
| Premium data unavailable | N/A | Information gap | Assess when source is available |

---

## 17. Data Quality Rules for Next Phase

The following rules should be applied during data standardization:

### Customer ID

- Must not be NULL.
- Must use a consistent VARCHAR representation.
- Leading-zero representation must be standardized.

### Claim ID

- Must not be NULL.
- Must be unique at the claim level.

### Claim Date

- Must be converted to a standard DATE format.
- Invalid dates must be rejected or sent to an exception process.

### Claim Amount

- Remove currency symbols.
- Convert to NUMERIC(12,2).
- Negative values should be rejected.
- Missing values should remain NULL unless a business rule is provided.

### Fraudulent

Allowed values:

- Yes
- No

### Police Report

Allowed source values:

- Yes
- No
- Unknown

### Claim Type

Allowed values:

- Material only
- Material and injury
- Injury only

---

## 18. Conclusion

The profiling and data quality assessment show that the supplied datasets
are generally structurally complete and contain no duplicate claim IDs or
duplicate customer IDs in the customer master data.

The main issues requiring attention are missing claim amounts, missing total
policy claim values, currency-format standardization, and customer ID
standardization across source formats.

These issues will be addressed during the data standardization and
warehouse-loading phases of Sprint 2.