
-- Gold Analytics: Claims Analytics
-- Purpose: Summarize claims by type and fraud status.

CREATE OR REPLACE VIEW gold.claims_analytics AS
SELECT
    TRIM(BOTH FROM claim_type) AS claim_type,
    TRIM(BOTH FROM fraudulent) AS fraudulent,
    COUNT(*) AS total_claim_records,
    COUNT(DISTINCT customer_id) AS unique_customers,
    SUM(
        CASE
            WHEN REGEXP_REPLACE(
                TRIM(BOTH FROM claim_amount),
                '[$,[:space:]]', '', 'g'
            ) ~ '^[+-]?[0-9]+(\.[0-9]+)?$'
            THEN REGEXP_REPLACE(
                TRIM(BOTH FROM claim_amount),
                '[$,[:space:]]', '', 'g'
            )::NUMERIC
            ELSE 0::NUMERIC
        END
    ) AS total_claim_amount,
    AVG(
        CASE
            WHEN REGEXP_REPLACE(
                TRIM(BOTH FROM claim_amount),
                '[$,[:space:]]', '', 'g'
            ) ~ '^[+-]?[0-9]+(\.[0-9]+)?$'
            THEN REGEXP_REPLACE(
                TRIM(BOTH FROM claim_amount),
                '[$,[:space:]]', '', 'g'
            )::NUMERIC
            ELSE NULL::NUMERIC
        END
    ) AS average_claim_amount
FROM silver.claim_details_clean
GROUP BY
    TRIM(BOTH FROM claim_type),
    TRIM(BOTH FROM fraudulent);
