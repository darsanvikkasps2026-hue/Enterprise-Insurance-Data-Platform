# Data Dictionary

## 1. Customer Demographics

| Column      | Description                        | Data Type | Example      |
| ----------- | ---------------------------------- | --------- | ------------ |
| CUST_ID     | Unique identifier for the customer | Integer   | 21868593     |
| gender      | Gender of the customer             | Text      | Female       |
| DateOfBirth | Date of birth of the customer      | Date      | 12-Jan-79    |
| State       | State associated with the customer | Text      | VT           |
| Contact     | Customer contact number            | Text      | 789-916-8172 |
| Segment     | Customer business segment          | Text      | Platinum     |

## 2. Claims

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

## 3. Customer Profile

| Column      | Description                        | Data Type | Example   |
| ----------- | ---------------------------------- | --------- | --------- |
| customer_id | Unique identifier for the customer | Integer   | 21868593  |
| gender      | Gender of the customer             | Text      | Female    |
| DateOfBirth | Date of birth of the customer      | Date      | 12-Jan-79 |
| State       | State associated with the customer | Text      | VT        |

## 4. Claims

| Column         | Description                                          | Data Type | Example      |
| -------------- | ---------------------------------------------------- | --------- | ------------ |
| customer_id    | Identifier of the customer associated with the claim | Integer   | 21868593     |
| claim_id       | Unique identifier for the claim                      | Integer   | 54004764     |
| incident_cause | Cause of the incident                                | Text      | Driver error |
| claim_date     | Date on which the claim was made                     | Date      | 11/27/2017   |
| claim_area     | Area/category associated with the claim              | Text      | Auto         |

## 5. Claim Additional Details

| Column      | Description                       | Data Type | Example      |
| ----------- | --------------------------------- | --------- | ------------ |
| customer_id | Unique identifier of the customer | Integer   | 21868593     |
| Contact     | Contact number of the customer    | Text      | 789-916-8172 |
| Segment     | Customer segment/category         | Text      | Platinum     |

## 6. Customer Details SQL

| Column         | Description                                          | Data Type | Example      |
| -------------- | ---------------------------------------------------- | --------- | ------------ |
| customer_id    | Identifier of the customer associated with the claim | Integer   | 21868593     |
| claim_id       | Unique identifier for the claim                      | Integer   | 54004764     |
| incident_cause | Cause of the incident                                | Text      | Driver error |
| claim_date     | Date on which the claim was made                     | Date      | 11/27/2017   |
| claim_area     | Area/category associated with the claim              | Text      | Auto         |
