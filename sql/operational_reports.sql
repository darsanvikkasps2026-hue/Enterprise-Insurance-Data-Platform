-- ============================================
-- OPERATIONAL REPORTING
-- Enterprise Insurance Data Platform
-- ============================================


-- 1. Total Claims

SELECT COUNT(*) AS total_claims
FROM dw.fact_claim;


-- 2. Claims by Incident Cause

SELECT
    incident_cause,
    COUNT(*) AS claim_count
FROM dw.fact_claim
GROUP BY incident_cause
ORDER BY claim_count DESC;


-- 3. Fraudulent vs Non-Fraudulent Claims

SELECT
    fraudulent,
    COUNT(*) AS claim_count
FROM dw.fact_claim
GROUP BY fraudulent
ORDER BY claim_count DESC;


-- 4. Claims by Claim Type

SELECT
    claim_type,
    COUNT(*) AS claim_count
FROM dw.fact_claim
GROUP BY claim_type
ORDER BY claim_count DESC;


-- 5. Claims by Claim Area

SELECT
    claim_area,
    COUNT(*) AS claim_count
FROM dw.fact_claim
GROUP BY claim_area
ORDER BY claim_count DESC;


-- 6. Total and Average Insurance Claim Amount

SELECT
    COUNT(*) AS total_insurance_claims,
    SUM(total_claim_amount) AS total_claim_amount,
    AVG(total_claim_amount) AS average_claim_amount
FROM dw.fact_insurance_claim;


-- 7. Claims by Incident Severity

SELECT
    incident_severity,
    COUNT(*) AS claim_count
FROM dw.fact_insurance_claim
GROUP BY incident_severity
ORDER BY claim_count DESC;