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
