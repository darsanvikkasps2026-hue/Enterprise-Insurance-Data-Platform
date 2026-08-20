# Source Inventory

## Project: Enterprise Insurance Data Platform (EIDP)

## 1. Source Systems

| Source System            | Data Domain | Source Format | Current Dataset  | Target Layer |
| ------------------------ | ----------- | ------------- | ---------------- | ------------ |
| Claims Management System | Claims      | CSV           | Claims dataset   | Bronze       |
| Customer / CRM System    | Customer    | CSV           | Customer dataset | Bronze       |

## 2. Claims Dataset

**Source:** Claims Management System

**File Type:** CSV

**Record Count:** 1,100

**Columns:** 10

### Fields

* `claim_id`
* `customer_id`
* `incident_cause`
* `claim_date`
* `claim_area`
* `police_report`
* `claim_type`
* `claim_amount`
* `total_policy_claims`
* `fraudulent`

### Business Purpose

The dataset contains insurance claim information required for claims processing, claims analysis, and fraud-related analysis.

---

## 3. Customer Dataset

**Source:** Customer / CRM System

**File Type:** CSV

**Record Count:** 1,085

**Columns:** 6

### Fields

* `CUST_ID`
* `gender`
* `DateOfBirth`
* `State`
* `Contact`
* `Segment`

### Business Purpose

The dataset contains customer information required to support a unified customer view and customer-related insurance analytics.

---

## 4. Source-to-Domain Mapping

| Dataset  | Business Domain | Primary Identifier | Relationship                              |
| -------- | --------------- | ------------------ | ----------------------------------------- |
| Claims   | Claims          | `claim_id`         | `customer_id` links to customer `CUST_ID` |
| Customer | Customer        | `CUST_ID`          | Referenced by Claims                      |

## 5. Ingestion Plan

The source CSV datasets will first be ingested into the Bronze layer.

The ingestion process will:

1. Read the source CSV files.
2. Load the raw data without business transformations.
3. Preserve the source fields and values.
4. Perform basic ingestion validation.
5. Store the ingested data in the Bronze/Staging area.
6. Maintain the ETL process in Pentaho.
7. Commit the successful ingestion work to Git.
**## 5. Policy Administration Dataset**

****Source:**** Policy Administration System

****File Type:**** CSV

****Dataset:**** `insurance_dataset.csv`

****Transformation:**** `policy_administration_csv_ingestion.ktr`

**### Business Purpose**

The dataset contains customer and policy information required for policy administration and insurance-related processing.

---

**## 6. Underwriting Dataset**

****Source:**** Underwriting System

****File Type:**** JSON

****Dataset:**** `underwriting.json`

****Transformation:**** `underwriting_json_ingestion.ktr`

**### Business Purpose**

The dataset contains customer, policy, risk, financial, and underwriting-related information required for underwriting processing.

---

**## 7. Fraud Investigation Dataset**

****Source:**** Fraud Investigation System

****File Type:**** SQL

****Dataset:**** `fraud_investigation.sql`

****Transformation:**** `fraud_investigation.ktr`

****Target Table:**** `stg.fraud_investigation`

**### Business Purpose**

The dataset contains transaction, customer, policy, claim, incident, authority, agent, and vendor information required for fraud investigation and analysis.

---

**## 8. Customer Service Application Dataset**

****Source:**** Customer Service Application

****File Type:**** JSON

****Dataset:**** `customer_service_application.json`

****Transformation:**** `customer_service_ingestion.ktr`

****Target Table:**** `stg.customer_service_application`

**### Business Purpose**

The dataset contains customer reviews, ratings, sentiment information, and generated customer service tasks used for customer service processing and analysis.

---

**## 9. Auto Insurance Claims Dataset**

****Source:**** Digital Insurance Portal

****File Type:**** Excel

****Dataset:**** `AutoInsuranceClaims2024.xlsx`

****Transformation:**** `auto_insurance_excel_ingestion.ktr`

**### Business Purpose**

The dataset contains automobile insurance customer, policy, premium, claim, vehicle, and customer profile information used for insurance processing and analytics.

---

**## 10. Source-to-Domain Mapping**

| Dataset                                 | Business Domain          | Primary Identifier | Transformation                               |

| -------------------------------------- | ------------------------ | ------------------ | --------------------------------------------- |

| Claims                                 | Claims                   | `claim_id`       | `claims_ingestion.ktr`                     |

| Customer                               | Customer                 | `CUST_ID`        | `customer_ingestion.ktr`                   |

| `insurance_dataset.csv`             | Policy Administration    | Customer ID        | `policy_administration_csv_ingestion.ktr` |

| `underwriting.json`                  | Underwriting             | `customer_id`    | `underwriting_json_ingestion.ktr`         |

| `fraud_investigation.sql`           | Fraud Investigation      | `transaction_id` | `fraud_investigation.ktr`                   |

| `customer_service_application.json` | Customer Service       | `review_id`      | `customer_service_ingestion.ktr`          |

| `AutoInsuranceClaims2024.xlsx`       | Auto Insurance           | Customer           | `auto_insurance_excel_ingestion.ktr`     |

---

**## 11. Ingestion Plan**

The source datasets will be ingested into the Bronze/Staging layer using Pentaho Data Integration.

The ingestion process will:

1. Read the source datasets using the appropriate Pentaho input step.

2. Load CSV, JSON, SQL, and Excel source data into the database.

3. Preserve the required source fields and values.

4. Perform basic ingestion validation.

5. Store the ingested data in the Bronze/Staging area.

6. Maintain the ETL transformations in Pentaho.

7. Execute the transformations through the master ingestion job.

8. Commit the successful ingestion work to Git.
## 12. Ingestion Plan

The source CSV datasets will first be ingested into the Bronze layer.

The ingestion process will:

1. Read the source CSV files.
2. Load the raw data without business transformations.
3. Preserve the source fields and values.
4. Perform basic ingestion validation.
5. Store the ingested data in the Bronze/Staging area.
6. Maintain the ETL process in Pentaho.
7. Commit the successful ingestion work to Git.

