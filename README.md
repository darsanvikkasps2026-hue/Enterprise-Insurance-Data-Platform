# Enterprise-Insurance-Data-Platform
Enterprise Insurance Data Platform (EIDP) - Data Engineering Capstone Project

## 1. Customer Profile

Source File: `dataset_1_customer_profile.js`

| Column        | Description                        | Data Type | Example     |
| ------------- | ---------------------------------- | --------- | ----------- |
| `customer_id` | Unique identifier for the customer | Integer   | `21868593`  |
| `gender`      | Gender of the customer             | Text      | `Female`    |
| `DateOfBirth` | Date of birth of the customer      | Date      | `12-Jan-79` |
| `State`       | State associated with the customer | Text      | `VT`        |

Dataset Description:
The file contains customer profile records with customer_id, gender, DateOfBirth, and State.

## 2. Claims

Source File: dataset_3_claim_details.csv

| Column           | Description                                          | Data Type | Example        |
| ---------------- | ---------------------------------------------------- | --------- | -------------- |
| `customer_id`    | Identifier of the customer associated with the claim | Integer   | `21868593`     |
| `claim_id`       | Unique identifier for the claim                      | Integer   | `54004764`     |
| `incident_cause` | Cause of the incident                                | Text      | `Driver error` |
| `claim_date`     | Date on which the claim was made                     | Date      | `11/27/2017`   |
| `claim_area`     | Area/category associated with the claim              | Text      | `Auto`         |

Dataset Description:
The CSV file contains claim-related records with customer_id, claim_id, incident_cause, claim_date, and claim_area.

## 3. Claim Additional Details

Source File: dataset_4_claim_additional.xml

| Column        | Description                       | Data Type | Example        |
| ------------- | --------------------------------- | --------- | -------------- |
| `customer_id` | Unique identifier of the customer | Integer   | `21868593`     |
| `Contact`     | Contact number of the customer    | Text      | `789-916-8172` |
| `Segment`     | Customer segment/category         | Text      | `Platinum`     |

Dataset Description:
The XML file contains additional customer/claim information with customer_id, Contact, and Segment.

## 4. Customer Details SQL

Source File: customer_details.txt.sql

| Column           | Description                                          | Data Type | Example        |
| ---------------- | ---------------------------------------------------- | --------- | -------------- |
| `customer_id`    | Identifier of the customer associated with the claim | Integer   | `21868593`     |
| `claim_id`       | Unique identifier for the claim                      | Integer   | `54004764`     |
| `incident_cause` | Cause of the incident                                | Text      | `Driver error` |
| `claim_date`     | Date on which the claim was made                     | Date      | `11/27/2017`   |
| `claim_area`     | Area/category associated with the claim              | Text      | `Auto`         |

Dataset Description:
The SQL file contains INSERT statements for the dw.customer_details table, containing the five columns customer_id, claim_id, incident_cause, claim_date, and claim_area.
