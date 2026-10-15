
CREATE OR REPLACE VIEW gold.customer_datamart AS
SELECT
    total_customer_records,
    unique_customers,
    total_claim_records,
    customers_with_claims,
    CASE
        WHEN unique_customers > 0
        THEN ROUND(
            customers_with_claims * 100.0
            / unique_customers,
            2
        )
        ELSE 0
    END AS customers_with_claims_percentage
FROM gold.customer_analytics;
