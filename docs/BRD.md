# Business Requirements Document (BRD)

## 1. Project Title

Enterprise Insurance Data Platform (EIDP)

## 2. Business Problem

ABC Insurance Ltd. generates insurance data from multiple independent
enterprise systems. These systems include Policy Administration,
Claims Management, CRM, Underwriting, Premium Collection, Agent
Portals, Customer Service Applications, Regulatory Reporting Systems,
and Digital Insurance Platforms.

Because the data is distributed across different systems and formats,
it is difficult to obtain a unified customer view, accelerate claim
settlements, improve underwriting decisions, ensure regulatory
compliance, and generate enterprise-wide business insights.

## 3. Business Objectives

The Enterprise Insurance Data Platform shall:

1. Integrate insurance data from multiple source systems.
2. Provide a unified and consistent view of enterprise insurance data.
3. Improve the quality and reliability of insurance data.
4. Support faster claims analysis and settlement.
5. Support underwriting and risk analysis.
6. Provide reliable data for regulatory reporting.
7. Provide analytical data for management decision-making.
8. Enable enterprise-wide reporting and dashboards.

## 4. Business Requirements

### BR-01: Data Integration

The platform shall collect insurance data from heterogeneous sources
such as CSV, Excel, JSON, XML, and SQL-based sources.

### BR-02: Data Staging

The platform shall store raw and staged data in the Bronze layer
before further processing.

### BR-03: Data Cleansing

The platform shall identify and correct data quality issues including
missing values, duplicate records, invalid values, inconsistent formats,
and incorrect data types.

### BR-04: Data Validation

The platform shall validate insurance data before it is moved to
analytical layers.

### BR-05: Data Transformation

The platform shall standardize and transform data into consistent
business formats.

### BR-06: Data Warehouse

The platform shall provide a PostgreSQL-based enterprise data warehouse
using dimensional modeling.

### BR-07: Claims Analytics

The platform shall provide reliable data to support claims analysis
and claim settlement reporting.

### BR-08: Underwriting and Risk Analysis

The platform shall provide data required for underwriting analysis,
risk assessment, and fraud-related analysis.

### BR-09: Regulatory Reporting

The platform shall maintain reliable and traceable data for
regulatory and compliance reporting.

### BR-10: Business Intelligence

The platform shall provide curated data for Power BI dashboards and
management reporting.

### BR-11: Metadata and Lineage

The platform shall maintain metadata, source-to-target mappings,
and data lineage information.

### BR-12: Auditability

The platform shall maintain sufficient processing and audit information
to trace data through the platform.

## 5. Functional Requirements

### Data Ingestion

- Ingest data from CSV files.
- Ingest data from Excel files.
- Ingest data from JSON files.
- Ingest data from XML files.
- Ingest data from SQL sources.
- Store ingested data in staging tables.

### Data Processing

- Profile incoming datasets.
- Detect missing values.
- Detect duplicate records.
- Validate data types.
- Standardize values.
- Apply business validation rules.
- Transform data into analytical structures.

### Data Warehouse

The warehouse shall contain dimensions and fact tables supporting
insurance analytics.

Major business areas include:

- Customers
- Policies
- Claims
- Premiums
- Agents
- Dates

### Analytics

The platform shall provide data for:

- Policy analysis
- Premium analysis
- Claims analysis
- Customer analysis
- Risk analysis
- Management reporting

## 6. Non-Functional Requirements

### Data Quality

Data should be accurate, complete, consistent, and valid.

### Performance

ETL pipelines should process the available datasets efficiently.

### Security

Access to data and project resources should be controlled according
to organizational requirements.

### Scalability

The architecture should allow additional insurance data sources to
be integrated in the future.

### Maintainability

ETL pipelines, SQL scripts, Python programs, and documentation should
be organized and maintained through Git.

### Traceability

Data transformations should be traceable through metadata and lineage.

## 7. Stakeholders

| Stakeholder | Requirement / Interest |
|---|---|
| Claims Team | Claims processing and analytics |
| Underwriting Team | Risk and underwriting analysis |
| Policy Administration Team | Policy data management |
| Finance Team | Premium and financial reporting |
| Compliance Team | Regulatory reporting |
| Executive Management | Enterprise-level insights and dashboards |

## 8. Data Requirements

The platform shall work with insurance-related data including:

- Customer information
- Policy information
- Claims information
- Premium information
- Agent information
- Transaction information
- Regulatory reporting information

## 9. Reporting Requirements

The platform should support reports and dashboards for:

- Policy performance
- Claims performance
- Premium collections
- Customer analysis
- Underwriting and risk
- Enterprise management reporting

## 10. Technology Requirements

| Component | Technology |
|---|---|
| ETL | Pentaho Data Integration |
| Database | PostgreSQL |
| Data Profiling | Python / Pandas |
| Visualization | Power BI |
| Version Control | Git / GitHub |

## 11. Success Criteria

The project will meet its business requirements when:

- Required source data can be ingested successfully.
- Data quality issues can be identified and documented.
- Clean and validated data is available for analytics.
- PostgreSQL warehouse tables are populated successfully.
- Required business areas are represented in the warehouse.
- Data lineage and metadata are documented.
- Power BI dashboards can use the curated data.
- Project artifacts are maintained in GitHub.

## 12. Assumptions

- Required source datasets will be available for the project.
- PostgreSQL will be available for warehouse implementation.
- Pentaho Data Integration will be used for ETL development.
- Python and Pandas will be available for data profiling.
- Power BI will be available for analytics and visualization.

## 13. Out of Scope

The following are outside the scope of this project:

- Replacing existing insurance transaction systems.
- Developing a new insurance policy administration system.
- Developing a mobile application.
- Real-time transaction processing.