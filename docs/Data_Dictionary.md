# Data Dictionary

## 1. Customer Demographics

Source File: `cust_demographics.csv`

| Column | Description | Data Type | Example |
|---|---|---|---|
| CUST_ID | Unique identifier for the customer | Integer | 21868593 |
| gender | Gender of the customer | Text | Female |
| DateOfBirth | Date of birth of the customer | Date | 12-Jan-79 |
| State | State associated with the customer | Text | VT |
| Contact | Customer contact number | Text | 789-916-8172 |
| Segment | Customer business segment | Text | Platinum |

## 2. Claims

Source File: `claims.csv`

| Column | Description | Data Type | Example |
|---|---|---|---|
| claim_id | Unique identifier for the claim | Integer | 54004764 |
| customer_id | Identifier of the customer associated with the claim | Integer | 21868593 |
| incident_cause | Cause of the incident | Text | Driver error |
| claim_date | Date on which the claim was made | Date | 11/27/2017 |
| claim_area | Area/category associated with the claim | Text | - |
| police_report | Indicates whether a police report exists | Text | - |
| claim_type | Type of insurance claim | Text | Material only |
| claim_amount | Amount associated with the claim | Currency/Text | $2980 |
| total_policy_claims | Total number of claims associated with the policy | Numeric | 1.0 |
| fraudulent | Indicates whether the claim was identified as fraudulent | Text | No |

## 3. Relationship Between Datasets

The customer and claims datasets can be related using:

`cust_demographics.CUST_ID`

and

`claims.customer_id`

### Relationship

Customer Demographics

    CUST_ID
       |
       | 1 : Many
       |
       v
Claims

    customer_id

One customer may have multiple claims.

## 4. Source Files

| Source File | Format | Records | Columns |
|---|---|---:|---:|
| cust_demographics.csv | CSV | To be calculated | 6 |
| claims.csv | CSV | 1100 | 10 |