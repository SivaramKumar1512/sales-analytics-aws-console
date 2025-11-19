Project Overview — Sales Analytics Data Pipeline (AWS Console Project)

This project implements an end-to-end serverless data pipeline built entirely through the AWS Console, designed to simulate real-world data engineering work using only free-tier services.

The pipeline processes sales data from raw ingestion to analytics, using AWS native tools.

🚀 Architecture Flow

S3 (Raw Zone)
     ↓ Trigger
AWS Lambda (ETL Cleanup)
     ↓
S3 (Clean Zone)
     ↓
AWS Glue Crawler → Glue Data Catalog
     ↓
Amazon Athena (Query Engine)
     ↓
Excel Dashboard (Visualization)

📂 Project Features

✔ Raw → Clean ETL using Lambda

Removes empty rows

Validates data

Writes clean CSV to S3

✔ Metadata Automation

Glue Crawler automatically creates Athena table for cleaned dataset.

✔ Analytics Layer

Athena SQL queries generate insights:

Total revenue by product

Daily revenue trend

Basic data quality checks

✔ Dashboard

Excel pivot tables + charts:

Revenue by product (Bar chart)

Revenue over time (Line chart)

🧪 Included in Repository

sales_etl_cleaner.py → Lambda ETL

queries.sql → Athena SQL

sales.csv → Sample ingest data

crawler_instructions.md

iam_role_instructions.md

Test file for Lambda using unittest.mock

🎯 Skills Demonstrated

AWS data lake design (Raw → Clean → Query layers)

Event-driven pipeline using S3 triggers

Writing & deploying Lambda ETL code

Glue Catalog + Crawler setup

SQL analytics with Athena

Data visualization fundamentals

IAM role-based access control

Real-world debugging & cloud engineering practices

