1. Introduction

SQL Operational Reporting is used to retrieve meaningful business information from the Enterprise Insurance Data Warehouse.

The reports created in this phase use SQL queries to analyze customer claims, insurance claims, fraud information, claim types, claim areas, insurance claim amounts, and premium and loss information.

The operational reports are generated from the fact and dimension tables available in the dw schema.

2. Data Warehouse Tables Used
Table	Type	Purpose
dw.dim_customer	Dimension	Stores customer information
dw.dim_policy	Dimension	Stores policy information
dw.dim_vehicle	Dimension	Stores vehicle information
dw.fact_claim	Fact	Stores claim details
dw.fact_insurance_claim	Fact	Stores detailed insurance claim information
dw.fact_premium_loss	Fact	Stores premium, loss, and tax information

3. SQL Operational Reports
3.1 Total Number of Claims
Operation

The total number of records in the dw.fact_claim table is counted.

Purpose

This report provides the total number of claims available in the claim fact table.

SQL Query
SELECT COUNT(*) AS total_claims
FROM dw.fact_claim;
Output
Total Claims
1100
Result Description

The database contains 1,100 claims in the dw.fact_claim table.

3.2 Claims by Incident Cause
Operation

The claims are grouped according to their incident cause and counted.

Purpose

This report identifies the number of claims associated with each incident cause.

SQL Query
SELECT incident_cause,
       COUNT(*) AS claim_count
FROM dw.fact_claim
GROUP BY incident_cause
ORDER BY claim_count DESC;
Output
Incident Cause	Claim Count
Other causes	290
Driver error	262
Other driver error	249
Natural causes	189
Crime	110
Result Description

The highest number of claims is associated with Other causes, with 290 claims. Driver error accounts for 262 claims, while crime accounts for 110 claims.

3.3 Fraudulent and Non-Fraudulent Claims
Operation

Claims are grouped according to the fraudulent field.

Purpose

This report identifies the number of fraudulent and non-fraudulent claims.

SQL Query
SELECT fraudulent,
       COUNT(*) AS claim_count
FROM dw.fact_claim
GROUP BY fraudulent
ORDER BY claim_count DESC;
Output
Fraudulent	Claim Count
No	844
Yes	256
Result Description

There are 844 non-fraudulent claims and 256 fraudulent claims in the claim dataset.

3.4 Claims by Claim Type
Operation

Claims are grouped according to their claim type and counted.

Purpose

This report shows the distribution of claims across different claim types.

SQL Query
SELECT claim_type,
       COUNT(*) AS claim_count
FROM dw.fact_claim
GROUP BY claim_type
ORDER BY claim_count DESC;
Output
Claim Type	Claim Count
Material only	665
Material and injury	240
Injury only	195
Result Description

The majority of claims are Material only, with 665 claims. Material and injury claims account for 240 claims, while injury-only claims account for 195 claims.

3.5 Claims by Claim Area
Operation

Claims are grouped according to the claim area.

Purpose

This report identifies the number of claims associated with each claim area.

SQL Query
SELECT claim_area,
       COUNT(*) AS claim_count
FROM dw.fact_claim
GROUP BY claim_area
ORDER BY claim_count DESC;
Output
Claim Area	Claim Count
Auto	985
Home	115
Result Description

The claim data contains 985 Auto claims and 115 Home claims.

3.6 Total and Average Insurance Claim Amount
Operation

The total number of insurance claims, total claim amount, and average claim amount are calculated.

Purpose

This report provides an overview of the monetary value of insurance claims.

SQL Query
SELECT COUNT(*) AS total_insurance_claims,
       SUM(total_claim_amount) AS total_claim_amount,
       AVG(total_claim_amount) AS average_claim_amount
FROM dw.fact_insurance_claim;
Output
Total Insurance Claims	Total Claim Amount	Average Claim Amount
1000	52,761,940.00	52,761.94
Result Description

There are 1,000 insurance claims with a total claim amount of 52,761,940.00. The average insurance claim amount is approximately 52,761.94.

3.7 Claims by Incident Severity
Operation

Insurance claims are grouped according to incident severity and counted.

Purpose

This report identifies the distribution of insurance claims according to the severity of the incident.

SQL Query
SELECT incident_severity,
       COUNT(*) AS claim_count
FROM dw.fact_insurance_claim
GROUP BY incident_severity
ORDER BY claim_count DESC;
Output
Incident Severity	Claim Count
Minor Damage	354
Total Loss	280
Major Damage	276
Trivial Damage	90
Result Description

Minor Damage has the highest number of claims with 354 records. Total Loss has 280 claims, Major Damage has 276 claims, and Trivial Damage has 90 claims.

3.8 Fraudulent Insurance Claims
Operation

Insurance claims are grouped according to the fraud_reported field.

Purpose

This report identifies the distribution of reported fraudulent and non-fraudulent insurance claims.

SQL Query
SELECT fraud_reported,
       COUNT(*) AS claim_count
FROM dw.fact_insurance_claim
GROUP BY fraud_reported
ORDER BY claim_count DESC;
Output

PostgreSQL execution result should be added here after running the query.

Result Description

This report will show the number of insurance claims where fraud was reported and the number where fraud was not reported.

3.9 Premiums Written, Losses Paid and Taxes Paid
Operation

The total premiums written, losses paid, and taxes paid are calculated from the premium and loss fact table.

Purpose

This report provides an overall financial summary of premium, loss, and tax amounts.

SQL Query
SELECT SUM(premiums_written) AS total_premiums_written,
       SUM(losses_paid) AS total_losses_paid,
       SUM(taxes_paid) AS total_taxes_paid
FROM dw.fact_premium_loss;
Output

PostgreSQL execution result should be added here after running the query.

Result Description

This report will provide the total premium amount written, total losses paid, and total taxes paid in the warehouse.

3.10 Customer-Wise Claim Summary
Operation

Claims are grouped according to customer_key and the number of claims associated with each key is counted.

Purpose

This report can be used to analyze the number of claims associated with customers.

SQL Query
SELECT customer_key,
       COUNT(*) AS claim_count
FROM dw.fact_claim
GROUP BY customer_key
ORDER BY claim_count DESC;
Output

PostgreSQL execution result should be added here after validating the customer-key relationship.

Result Description

The report groups claims according to the customer key and displays the number of claims associated with each key.

Data quality note: The customer_key relationship in dw.fact_claim should be validated before using this report as a customer-level business report.

4. SQL Operations Used

The following SQL operations were used to generate the operational reports:

SQL Operation	Usage
SELECT	Retrieves data from warehouse tables
COUNT()	Counts records and claims
SUM()	Calculates total monetary values
AVG()	Calculates average claim amounts
GROUP BY	Groups records according to business attributes
ORDER BY	Sorts the reporting results
AS	Provides meaningful names for calculated columns

5. SQL Operational Reporting Summary
Report	Warehouse Table	Main Operation
Total Number of Claims	dw.fact_claim	COUNT()
Claims by Incident Cause	dw.fact_claim	GROUP BY, COUNT()
Fraudulent and Non-Fraudulent Claims	dw.fact_claim	GROUP BY, COUNT()
Claims by Claim Type	dw.fact_claim	GROUP BY, COUNT()
Claims by Claim Area	dw.fact_claim	GROUP BY, COUNT()
Total and Average Insurance Claim Amount	dw.fact_insurance_claim	COUNT(), SUM(), AVG()
Claims by Incident Severity	dw.fact_insurance_claim	GROUP BY, COUNT()
Fraudulent Insurance Claims	dw.fact_insurance_claim	GROUP BY, COUNT()
Premiums, Losses and Taxes	dw.fact_premium_loss	SUM()
Customer-Wise Claim Summary	dw.fact_claim	GROUP BY, COUNT()

6. Operational Reporting Outcome

The SQL operational reporting phase provides structured information from the Enterprise Insurance Data Warehouse.

The implemented queries provide information about:

Total number of claims
Incident causes
Fraudulent and non-fraudulent claims
Claim types
Claim areas
Total insurance claim amounts
Average insurance claim amounts
Incident severity
Premiums written
Losses paid
Taxes paid
Customer-level claim information

These reports demonstrate the use of SQL for retrieving and analyzing insurance data stored in the PostgreSQL data warehouse.

7. Conclusion

SQL operational reporting provides a way to retrieve useful business information from the Enterprise Insurance Data Warehouse.

The reports created in this phase use aggregation, grouping, sorting, and calculation operations to analyze claims, insurance amounts, fraud information, and financial information.

The completed SQL reports form part of the Sprint 2 – Data Profiling & Database / Data Warehouse deliverables.