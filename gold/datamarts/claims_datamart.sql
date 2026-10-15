
CREATE SCHEMA IF NOT EXISTS gold;

CREATE OR REPLACE VIEW gold.claims_datamart AS
SELECT
    claim_type,
    fraudulent,
    SUM(total_claim_records) AS total_claim_records,
    SUM(unique_customers) AS unique_customers,
    SUM(total_claim_amount) AS total_claim_amount,
    CASE
        WHEN SUM(total_claim_records) > 0
        THEN ROUND(
            SUM(total_claim_amount)
            / SUM(total_claim_records),
            2
        )
        ELSE 0
    END AS average_claim_amount
FROM gold.claims_analytics
GROUP BY
    claim_type,
    fraudulent;
