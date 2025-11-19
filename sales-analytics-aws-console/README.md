# Sales Analytics — AWS Console Project

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


This repository contains the files and instructions for the **Sales Analytics Pipeline** you built using the AWS Console.
It is designed to be a documentation + code bundle you can upload to GitHub or use in interviews.

## Project Overview
**Flow:** S3 (raw) → Lambda (ETL) → S3 (clean) → Glue Crawler → Athena → Excel dashboard

This repo includes:
- Lambda ETL code (console-deployable)
- Sample data
- Athena queries
- Glue crawler & IAM instructions (console steps)
- Unit test for the Lambda (uses `unittest.mock`)
- README with step-by-step Console instructions

## Quick contents
- `lambda/sales_etl_cleaner.py` — Lambda function code (Python)
- `sample_data/sales.csv` — sample CSV to upload to raw S3 bucket
- `athena/queries.sql` — useful Athena queries & sample view
- `glue/crawler_instructions.md` — how to create Glue DB & Crawler via Console
- `infra/iam_role_instructions.md` — IAM role instructions for Lambda & Glue
- `tests/test_lambda.py` — unit tests (mocking boto3)
- `LICENSE` — MIT

## How to use
1. Open the AWS Console (region: **ap-south-1** recommended).
2. Create two S3 buckets:
   - `sales-raw-<yourname>`
   - `sales-clean-<yourname>`
3. Create IAM role for Lambda (see `infra/iam_role_instructions.md`)
4. Create Lambda function and paste `lambda/sales_etl_cleaner.py` into the inline editor (or zip and upload).
   - Set environment variables: `RAW_BUCKET` and `CLEAN_BUCKET`.
5. Add an S3 PUT trigger for the raw bucket to invoke the Lambda.
6. Upload `sample_data/sales.csv` to the raw bucket and confirm cleaned file appears in the clean bucket.
7. Create Glue database and crawler (see `glue/crawler_instructions.md`).
8. Run queries in Athena (see `athena/queries.sql`).
9. Download Athena results and create Excel dashboard (as we did).

## Notes
- This repo is intentionally console-focused (no Terraform/CloudFormation) so it matches your project built via AWS Console.
- All operations shown are free-tier friendly for small datasets.

