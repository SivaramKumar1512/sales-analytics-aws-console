# Glue Crawler Instructions (Console)

1. Open AWS Console -> Glue -> Databases -> Create database
   - Name: sales_db

2. Create IAM role for Glue if needed:
   - IAM -> Roles -> Create role -> AWS service -> Glue
   - Attach AmazonS3ReadOnlyAccess and AWSGlueServiceRole (or similar)

3. Create Crawler:
   - Glue -> Crawlers -> Add crawler
   - Name: sales-clean-crawler
   - Data store: S3 -> s3://sales-clean-<yourname>/
   - IAM role: glue-crawler-role-sales (or auto-create)
   - Target database: sales_db
   - Run on demand

4. Run crawler and verify table under sales_db (table name like sales_clean_sivam01)
