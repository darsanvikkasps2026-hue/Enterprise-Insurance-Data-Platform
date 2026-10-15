
-- Gold Analytics: Health Insurance Analytics
-- Purpose: Summarize premiums, losses, and taxes
-- by year, state, and insurance company.

CREATE OR REPLACE VIEW gold.health_insurance_analytics AS
SELECT
    TRIM(BOTH FROM data_year) AS data_year,
    TRIM(BOTH FROM cstate) AS state,
    TRIM(BOTH FROM cname) AS insurance_company,
    COUNT(*) AS total_records,

    SUM(
        CASE
            WHEN REGEXP_REPLACE(
                TRIM(BOTH FROM premiums_written),
                '[$,[:space:]]', '', 'g'
            ) ~ '^[+-]?[0-9]+(\.[0-9]+)?$'
            THEN REGEXP_REPLACE(
                TRIM(BOTH FROM premiums_written),
                '[$,[:space:]]', '', 'g'
            )::NUMERIC
            ELSE 0::NUMERIC
        END
    ) AS total_premiums_written,

    SUM(
        CASE
            WHEN REGEXP_REPLACE(
                TRIM(BOTH FROM losses_paid),
                '[$,[:space:]]', '', 'g'
            ) ~ '^[+-]?[0-9]+(\.[0-9]+)?$'
            THEN REGEXP_REPLACE(
                TRIM(BOTH FROM losses_paid),
                '[$,[:space:]]', '', 'g'
            )::NUMERIC
            ELSE 0::NUMERIC
        END
    ) AS total_losses_paid,

    SUM(
        CASE
            WHEN REGEXP_REPLACE(
                TRIM(BOTH FROM taxes_paid),
                '[$,[:space:]]', '', 'g'
            ) ~ '^[+-]?[0-9]+(\.[0-9]+)?$'
            THEN REGEXP_REPLACE(
                TRIM(BOTH FROM taxes_paid),
                '[$,[:space:]]', '', 'g'
            )::NUMERIC
            ELSE 0::NUMERIC
        END
    ) AS total_taxes_paid

FROM silver.health_insurance_clean
GROUP BY
    TRIM(BOTH FROM data_year),
    TRIM(BOTH FROM cstate),
    TRIM(BOTH FROM cname);
