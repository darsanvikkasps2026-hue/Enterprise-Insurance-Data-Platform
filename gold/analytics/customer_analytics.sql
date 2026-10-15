
-- Gold Analytics: Customer Analytics
-- Purpose: Summarize customer and claim statistics.

CREATE OR REPLACE VIEW gold.customer_analytics AS

WITH customer_counts AS (
    SELECT
        COUNT(*) AS total_customer_records,
        COUNT(DISTINCT customer_id) AS unique_customers
    FROM silver.customer_profile_clean
),
claim_counts AS (
    SELECT
        COUNT(*) AS total_claim_records,
        COUNT(DISTINCT customer_id) AS customers_with_claims
    FROM silver.claim_details_clean
)
SELECT
    c.total_customer_records,
    c.unique_customers,
    cl.total_claim_records,
    cl.customers_with_claims
FROM customer_counts c
CROSS JOIN claim_counts cl;
