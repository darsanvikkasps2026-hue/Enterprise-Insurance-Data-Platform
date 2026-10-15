
CREATE SCHEMA IF NOT EXISTS gold;

CREATE OR REPLACE VIEW gold.premium_loss_analytics AS
SELECT
    data_year,
    cstate,
    cname,
    description,
    SUM(premiums_written) AS total_premiums_written,
    SUM(losses_paid) AS total_losses_paid,
    SUM(taxes_paid) AS total_taxes_paid,
    CASE
        WHEN SUM(premiums_written) > 0
        THEN ROUND(
            SUM(losses_paid) * 100.0
            / SUM(premiums_written),
            2
        )
        ELSE NULL
    END AS loss_ratio_percentage,
    COUNT(*) AS record_count
FROM dw.fact_premium_loss
GROUP BY
    data_year,
    cstate,
    cname,
    description;
