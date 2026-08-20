# Data Dictionary

## 1. Customer Demographics

Source File: `cust_demographics.csv`

| Column      | Description                        | Data Type | Example      |
| ----------- | ---------------------------------- | --------- | ------------ |
| CUST_ID     | Unique identifier for the customer | Integer   | 21868593     |
| gender      | Gender of the customer             | Text      | Female       |
| DateOfBirth | Date of birth of the customer      | Date      | 12-Jan-79    |
| State       | State associated with the customer | Text      | VT           |
| Contact     | Customer contact number            | Text      | 789-916-8172 |
| Segment     | Customer business segment          | Text      | Platinum     |

## 2. Claims

Source File: `claims.csv`

| Column              | Description                                              | Data Type | Example       |
| ------------------- | -------------------------------------------------------- | --------- | ------------- |
| claim_id            | Unique identifier for the claim                          | Integer   | 54004764      |
| customer_id         | Identifier of the customer associated with the claim     | Integer   | 21868593      |
| incident_cause      | Cause of the incident                                    | Text      | Driver error  |
| claim_date          | Date on which the claim was made                         | Text      | 11/27/2017    |
| claim_area          | Area/category associated with the claim                  | Text      | -             |
| police_report       | Indicates whether a police report exists                 | Text      | -             |
| claim_type          | Type of insurance claim                                  | Text      | Material only |
| claim_amount        | Amount associated with the claim                         | Text      | $2980         |
| total_policy_claims | Total number of claims associated with the policy        | Float     | 1.0           |
| fraudulent          | Indicates whether the claim was identified as fraudulent | Text      | No            |

## 3. Relationship Between Datasets

The customer and claims datasets can be related using:

`cust_demographics.CUST_ID`

and

`claims.customer_id`

### Relationship

Customer Demographics

```
CUST_ID
   |
   | 1 : Many
   |
   v
```

Claims

```
customer_id
```

One customer may have multiple claims.

## 4. Source Files

| Source File           | Format | Records | Columns |
| --------------------- | ------ | ------: | ------: |
| cust_demographics.csv | CSV    |    1085 |       6 |
| claims.csv            | CSV    |    1100 |      10 |
**## 5. Policy Administration**

Source File: `insurance_dataset.csv`

| Column                         | Description                                             | Data Type |
| ----------------------------- | -------------------------------------------------------- | --------- |
| Customer ID                   | Unique identifier for the customer                       | Text      |
| Age                           | Age of the customer                                      | Integer   |
| Gender                        | Gender of the customer                                   | Text      |
| Marital Status                | Customer marital status                                  | Text      |
| Occupation                    | Customer occupation                                     | Text      |
| Income Level                  | Customer income category                                | Text      |
| Education Level               | Customer education level                                | Text      |
| Geographic Information        | Geographic information of the customer                  | Text      |
| Location                      | Customer location                                        | Text      |
| Behavioral Data               | Customer behavioural information                        | Text      |
| Purchase History              | Customer purchase history                               | Text      |
| Policy Start Date             | Date on which the policy started                        | Date      |
| Policy Renewal Date           | Date on which the policy is scheduled for renewal       | Date      |
| Claim History                 | Historical claim information                            | Text      |
| Insurance Products Owned      | Insurance products owned by the customer                | Text      |
| Coverage Amount               | Amount of insurance coverage                            | Decimal   |
| Premium Amount                | Insurance premium amount                                | Decimal   |
| Deductible                    | Deductible amount associated with the policy            | Decimal   |
| Policy Type                   | Type of insurance policy                                | Text      |
| Customer Preferences          | Customer insurance preferences                          | Text      |
| Preferred Communication Channel | Preferred communication channel                     | Text      |
| Preferred Contact Time        | Preferred contact time                                   | Text      |
| Preferred Language            | Preferred language of the customer                      | Text      |
| Risk Profile                  | Risk classification of the customer                    | Text      |
| Previous Claims History       | Previous claims information                             | Text      |
| Credit Score                  | Customer credit score                                   | Integer   |
| Driving Record                | Customer driving history                                | Text      |
| Life Events                   | Relevant customer life-event information                | Text      |

**## 6. Underwriting**

Source File: `underwriting.json`

| Column                        | Description                                             | Data Type |
| ----------------------------- | ------------------------------------------------------ | --------- |
| customer_id                   | Unique identifier for the customer                     | Text      |
| policy_number                  | Unique identifier for the policy                       | Text      |
| age                            | Age of the customer                                    | Integer   |
| gender                         | Gender of the customer                                 | Text      |
| risk_profile                  | Customer risk classification                           | Text      |
| previous_claims_history       | Previous claims information                            | Text      |
| credit_score                  | Customer credit score                                  | Integer   |
| driving_record                | Customer driving history                               | Text      |
| occupation                    | Customer occupation                                    | Text      |
| income_level                  | Customer income category                               | Text      |
| education_level               | Customer education level                               | Text      |
| policy_type                   | Type of insurance policy                               | Text      |
| coverage_amount               | Amount of insurance coverage                           | Decimal   |
| premium_amount                | Insurance premium amount                               | Decimal   |
| deductible                    | Deductible amount associated with the policy           | Decimal   |

**## 7. Fraud Investigation**

Source File: `fraud_investigation.sql`

| Column                        | Description                                             | Data Type |
| ----------------------------- | ------------------------------------------------------ | --------- |
| transaction_id                | Unique identifier for the investigation transaction    | Text      |
| customer_id                   | Customer associated with the transaction               | Text      |
| policy_number                 | Policy associated with the transaction                 | Text      |
| loss_date                     | Date on which the loss occurred                        | Date      |
| report_date                   | Date on which the incident was reported                | Date      |
| insurance_type                | Type of insurance                                       | Text      |
| claim_amount                  | Amount claimed for the incident                        | Decimal   |
| claim_status                  | Status of the claim                                     | Text      |
| incident_severity             | Severity of the incident                               | Text      |
| authority_contacted           | Authority contacted regarding the incident             | Text      |
| any_injury                     | Indicates whether an injury occurred                   | Integer   |
| police_report_available       | Indicates whether a police report is available         | Integer   |
| incident_state                | State where the incident occurred                      | Text      |
| incident_city                 | City where the incident occurred                       | Text      |
| incident_hour                 | Hour at which the incident occurred                    | Integer   |
| agent_id                      | Identifier of the insurance agent                       | Text      |
| vendor_id                     | Identifier of the vendor                               | Text      |

**## 8. Customer Service Application**

Source File: `customer_service_application.json`

| Column             | Description                                             | Data Type |
| ------------------ | ------------------------------------------------------ | --------- |
| review_id          | Unique identifier for the customer review              | Integer   |
| customer_id        | Identifier of the customer                             | Integer   |
| review_date        | Date and time when the review was submitted            | Timestamp |
| rating             | Customer rating                                        | Integer   |
| review_text        | Text content of the customer review                    | Text      |
| sentiment          | Sentiment classification of the review                 | Text      |
| generated_task     | Task generated from the customer feedback             | Text      |
| ai_generated       | Indicates whether the task was AI generated           | Boolean   |

**## 9. Auto Insurance Claims**

Source File: `AutoInsuranceClaims2024.xlsx`

| Column                         | Description                                             | Data Type |
| ------------------------------ | ------------------------------------------------------ | --------- |
| index                           | Source row identifier                                   | Integer   |
| Customer                        | Unique customer identifier                             | Text      |
| State                           | Customer state                                         | Text      |
| Customer Lifetime Value        | Estimated lifetime value of the customer              | Decimal   |
| Response                       | Customer response indicator                            | Text      |
| Coverage                       | Insurance coverage level                               | Text      |
| Education                      | Customer education level                               | Text      |
| Effective To Date             | Effective date of the record                          | Date      |
| Employment Status             | Customer employment status                            | Text      |
| Gender                         | Customer gender                                        | Text      |
| Income                         | Customer income                                        | Numeric   |
| Location                      | Customer location type                                | Text      |
| Marital Status                 | Customer marital status                               | Text      |
| Monthly Premium Auto          | Monthly automobile insurance premium                  | Decimal   |
| Months Since Last Claim       | Number of months since the last claim                 | Integer   |
| Months Since Policy Inception | Number of months since the policy started             | Integer   |
| Number of Open Complaints     | Number of unresolved complaints                       | Integer   |
| Number of Policies            | Number of policies owned by the customer               | Integer   |
| Policy Type                   | Type of insurance policy                               | Text      |
| Policy                        | Specific insurance policy product                      | Text      |
| Renew Offer Type              | Type of renewal offer                                  | Integer   |
| Sales Channel                 | Channel through which the policy was sold             | Text      |
| Total Claim Amount            | Total claim amount associated with the customer       | Decimal   |
| Vehicle Class                 | Classification of the insured vehicle                 | Text      |
| Vehicle Size                  | Size category of the insured vehicle                  | Text      |

**## 10. Transformation and Source Mapping**

| Transformation                               | Source File                                 | Format |
| ------------------------------------------- | ------------------------------------------- | ------ |
| customer_ingestion.ktr                      | cust_demographics.csv                       | CSV    |
| claims_ingestion.ktr                         | claims.csv                                 | CSV    |
| policy_administration_csv_ingestion.ktr     | insurance_dataset.csv                       | CSV    |
| underwriting_json_ingestion.ktr             | underwriting.json                           | JSON   |
| fraud_investigation.ktr                     | fraud_investigation.sql                     | SQL    |
| customer_service_ingestion.ktr              | customer_service_application.json          | JSON   |
| auto_insurance_excel_ingestion.ktr          | AutoInsuranceClaims2024.xlsx               | Excel  |
