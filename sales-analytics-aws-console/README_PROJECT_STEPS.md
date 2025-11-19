# Quick runbook (what we did)

1. Create S3 buckets (raw and clean)
2. Upload sample_data/sales.csv to raw bucket
3. Create IAM role lambda-sales-role
4. Create Lambda function sales-etl-cleaner, set env vars and paste lambda/sales_etl_cleaner.py
5. Add S3 PUT trigger from raw bucket to Lambda
6. Verify clean file appears in clean bucket
7. Create Glue database & crawler (see glue/crawler_instructions.md)
8. Run Athena queries from athena/queries.sql and download CSV results
9. Use Excel to create revenue column, pivot tables and charts (dashboard)
