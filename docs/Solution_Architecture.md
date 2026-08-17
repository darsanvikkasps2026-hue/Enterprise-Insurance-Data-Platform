# Solution Architecture

## 1. Architecture Overview

The Enterprise Insurance Data Platform follows a Bronze-Silver-Gold
data architecture.

Data is collected from multiple insurance source systems and processed
through Pentaho Data Integration. The data is progressively cleaned,
validated, transformed, and stored for analytical use.

## 2. Data Flow

Source Systems
       |
       v
Pentaho Data Integration
       |
       v
Bronze Layer
(Raw / Staged Data)
       |
       v
Silver Layer
(Cleansed / Validated / Transformed Data)
       |
       v
Gold Layer
(Enterprise Data Warehouse / Data Marts)
       |
       v
PostgreSQL
       |
       v
Power BI
(Analytics and Dashboards)

## 3. Source Systems

The platform receives insurance data from multiple enterprise sources,
including:

- Policy Administration
- Claims Management
- Customer Relationship Management (CRM)
- Underwriting
- Premium Collection
- Agent Portal
- Customer Service
- Regulatory Reporting
- Digital Insurance Portal
- Fraud Investigation

## 4. Bronze Layer

The Bronze layer contains raw or staged data received from source
systems.

The data is stored without major business transformations so that
the original source information can be retained for further processing.

## 5. Silver Layer

The Silver layer contains cleansed and validated data.

Processing includes:

- Missing value handling
- Duplicate detection
- Data type validation
- Standardization
- Business rule validation
- Data transformation

## 6. Gold Layer

The Gold layer contains curated data prepared for business analytics.

It includes:

- Enterprise data warehouse
- Data marts
- Analytical datasets

## 7. ETL Layer

Pentaho Data Integration is used to build ETL pipelines.

The ETL process performs:

1. Data extraction
2. Data loading into staging
3. Data cleansing
4. Data validation
5. Data transformation
6. Loading into the analytical warehouse

## 8. Data Profiling

Python and Pandas are used for data profiling and quality analysis.

Profiling includes:

- Missing value analysis
- Duplicate analysis
- Data type analysis
- Value distribution
- Data quality checks

## 9. Data Warehouse

PostgreSQL is used to implement the enterprise data warehouse.

The warehouse will use dimensional modeling to support analytical
queries and reporting.

## 10. Analytics Layer

Power BI is used to create dashboards and reports using the curated
data from the Gold layer and data warehouse.

## 11. Version Control

Git and GitHub are used to maintain project source code,
ETL configurations, SQL scripts, documentation, and project history.