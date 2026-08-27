# Source Inventory

## Project: Enterprise Insurance Data Platform (EIDP)

## 1. Source Systems

| **Source System**          | **Data Domain** | **Source Format** | **Dataset**                      | **Target Layer** |
| -------------------------- | --------------- | ----------------- | -------------------------------- | ---------------- |
| Customer Profile System    | Customer        | CSV               | `dataset_1_customer_profile.csv` | Bronze           |
| Customer Management System | Customer        | CSV               | `dataset_2_customer_details.csv` | Bronze           |
| Claims Management System   | Claims          | CSV               | `dataset_3_claim_details.csv`    | Bronze           |
| Claims / Incident System   | Claims          | CSV               | `dataset_4_claim_additional.csv` | Bronze           |

---

## 2. Dataset 1 — Customer Profile

**Source:** Customer Profile System

**File Type:** CSV

**Dataset:** `dataset_1_customer_profile.csv`

**Target Layer:** Bronze

**Business Domain:** Customer

### Business Purpose

This dataset contains customer profile information used to maintain customer records and support customer-level insurance analytics.

### Expected Data

The dataset contains customer-related profile attributes such as customer identification and demographic information.

---

## 3. Dataset 2 — Customer Details

**Source:** Customer Management System

**File Type:** CSV

**Dataset:** `dataset_2_customer_details.csv`

**Target Layer:** Bronze

**Business Domain:** Customer

### Business Purpose

This dataset contains detailed customer information required to support customer management, customer segmentation, and integration with insurance-related datasets.

### Expected Data

The dataset contains detailed customer attributes that can be associated with customer records from the customer profile dataset.

---

## 4. Dataset 3 — Claim Details

**Source:** Claims Management System

**File Type:** CSV

**Dataset:** `dataset_3_claim_details.csv`

**Target Layer:** Bronze

**Business Domain:** Claims

### Business Purpose

This dataset contains insurance claim information required for claims processing, claims analysis, and integration with customer-related information.

### Expected Data

The dataset contains claim-related attributes such as claim identifiers, customer references, claim dates, claim types, claim amounts, and other claim processing information.

---

## 5. Dataset 4 — Claim Additional Information

**Source:** Claims / Incident System

**File Type:** CSV

**Dataset:** `dataset_4_claim_additional.csv`

**Target Layer:** Bronze

**Business Domain:** Claims

### Business Purpose

This dataset contains additional claim and incident-related information that complements the main claim details dataset and supports detailed claims and fraud analysis.

### Expected Data

The dataset contains additional attributes associated with claims, incidents, policies, customers, or fraud-related analysis.

---

## 6. Source-to-Domain Mapping

| **Dataset**                      | **Business Domain** | **Primary / Reference Identifier** | **Relationship**                                       |
| -------------------------------- | ------------------- | ---------------------------------- | ------------------------------------------------------ |
| `dataset_1_customer_profile.csv` | Customer            | Customer ID                        | Provides customer profile information                  |
| `dataset_2_customer_details.csv` | Customer            | Customer ID                        | Provides additional customer details                   |
| `dataset_3_claim_details.csv`    | Claims              | Claim ID                           | Contains main claim information and customer reference |
| `dataset_4_claim_additional.csv` | Claims              | Claim ID / Customer ID             | Provides additional claim and incident information     |

---

## 7. Dataset Integration

The four source datasets are logically grouped into two major business domains:

### Customer Domain

* `dataset_1_customer_profile.csv`
* `dataset_2_customer_details.csv`

These datasets provide customer profile and customer detail information.

### Claims Domain

* `dataset_3_claim_details.csv`
* `dataset_4_claim_additional.csv`

These datasets provide primary and additional information related to insurance claims.

The customer and claims datasets can be integrated using common customer identifiers where available. Claim-related datasets can be integrated using common claim identifiers and other applicable reference fields.

---

## 8. Ingestion Plan

The four source CSV datasets will be ingested into the **Bronze/Staging layer** using Pentaho Data Integration.

The ingestion process will:

1. Read the four source CSV datasets.
2. Validate the availability and structure of each source file.
3. Detect and process the source headers correctly.
4. Load the raw source data without applying business transformations.
5. Preserve the source fields and source values.
6. Perform basic ingestion and data-quality validation.
7. Store the ingested data in the Bronze/Staging area.
8. Maintain the ingestion transformations in Pentaho.
9. Execute the required transformations through the master ingestion job.
10. Record successful ingestion and handle ingestion exceptions.
11. Commit the completed ingestion work to Git.

---

## 9. Ingestion Transformations

| **Dataset**                      | **Format** | **Pentaho Transformation**        | **Target Layer** |
| -------------------------------- | ---------- | --------------------------------- | ---------------- |
| `dataset_1_customer_profile.csv` | CSV        | Customer ingestion transformation | Bronze/Staging   |
| `dataset_2_customer_details.csv` | CSV        | Customer ingestion transformation | Bronze/Staging   |
| `dataset_3_claim_details.csv`    | CSV        | Claims ingestion transformation   | Bronze/Staging   |
| `dataset_4_claim_additional.csv` | CSV        | Claims ingestion transformation   | Bronze/Staging   |

---

## 10. Source Inventory Summary

| **ID** | **Dataset**                      | **Domain** | **Format** | **Target Layer** | **Ingestion Status** |
| ------ | -------------------------------- | ---------- | ---------- | ---------------- | -------------------- |
| DS-01  | `dataset_1_customer_profile.csv` | Customer   | CSV        | Bronze           | Completed            |
| DS-02  | `dataset_2_customer_details.csv` | Customer   | CSV        | Bronze           | Completed            |
| DS-03  | `dataset_3_claim_details.csv`    | Claims     | CSV        | Bronze           | Completed            |
| DS-04  | `dataset_4_claim_additional.csv` | Claims     | CSV        | Bronze           | Completed            |

**Total Source Datasets: 4**

**Source Formats: CSV**

**Business Domains: Customer and Claims**

**Target Layer: Bronze/Staging**
