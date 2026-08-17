# Project Charter

## 1. Project Title

Enterprise Insurance Data Platform (EIDP)

## 2. Organization

ABC Insurance Ltd.

## 3. Business Problem

ABC Insurance Ltd. generates large volumes of insurance data from multiple
enterprise systems such as Policy Administration, Claims Management,
Customer Relationship Management, Underwriting, Billing and Premium
Collection, Agent Portals, Customer Service Applications, Regulatory
Reporting Systems, and Digital Insurance Platforms.

Since these systems operate independently, the organization faces
challenges in obtaining a unified customer view, accelerating claim
settlements, improving underwriting decisions, ensuring regulatory
compliance, and generating enterprise-wide business insights.

## 4. Project Objective

The objective of the Enterprise Insurance Data Platform is to build an
enterprise data platform that collects, cleans, validates, standardizes,
and stores insurance data.

The platform will support policy management, claims analytics,
underwriting, risk analysis, and executive reporting.

## 5. Project Scope

### In Scope

- Collection of insurance data from multiple enterprise systems
- Data cleaning and validation
- Customer, policy, claims, and premium data processing
- PostgreSQL data warehouse
- Star schema and dimensional modeling
- Data profiling using Python and Pandas
- ETL pipelines using Pentaho Data Integration
- Metadata and audit information
- Data lineage documentation
- Power BI reporting and dashboards
- Git and GitHub version control

### Out of Scope

- Replacement of existing insurance source systems
- Development of new insurance transaction systems
- Mobile application development
- Real-time insurance transaction processing

## 6. Key Stakeholders

- Claims Team
- Underwriting Team
- Policy Administration Team
- Finance Team
- Compliance Team
- Executive Management

## 7. Technology Stack

| Category | Technology |
|---|---|
| ETL | Pentaho Data Integration (Spoon) |
| Database | PostgreSQL |
| Programming | Python (Pandas) |
| Reporting | Power BI |
| Version Control | Git & GitHub |
| Documentation | Markdown / MS Word |
| Project Management | Agile Scrum |

## 8. Expected Outcomes

- Unified insurance data platform
- Clean and validated insurance datasets
- Enterprise PostgreSQL data warehouse
- Reliable ETL pipelines
- Data quality and profiling reports
- Data lineage and metadata documentation
- Business analytics dashboards
- Enterprise reporting capability

## 9. Architecture Approach

The project will follow the Bronze-Silver-Gold Medallion Architecture.

The Bronze layer will contain raw and staged insurance data.

The Silver layer will contain cleansed, validated, and transformed data.

The Gold layer will contain the enterprise data warehouse,
data marts, and analytics datasets.

## 10. Success Criteria

The project will be considered successful when:

- Insurance data is successfully ingested from multiple sources.
- ETL pipelines execute successfully.
- Data quality checks are documented.
- PostgreSQL tables are populated correctly.
- Source-to-target mappings are maintained.
- Data lineage is documented.
- Code is committed to Git with meaningful commit messages.
- Required documentation is completed.
- Power BI dashboards are developed.
- Sprint review and final project presentation are completed.