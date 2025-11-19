# IAM Role Instructions (Console) - Lambda and Glue

## Lambda role (lambda-sales-role)
1. Console -> IAM -> Roles -> Create role
2. Trusted entity: AWS service -> Lambda
3. Attach policies:
   - AmazonS3FullAccess
   - CloudWatchLogsFullAccess (or CloudWatchFullAccess)
4. Role name: lambda-sales-role

## Glue role (glue-crawler-role-sales) - optional manual role
1. Console -> IAM -> Roles -> Create role
2. Trusted entity: AWS service -> Glue
3. Attach policies:
   - AmazonS3ReadOnlyAccess
   - AWSGlueServiceRole (if available)
4. Role name: glue-crawler-role-sales

Note: For production, restrict S3 permissions to specific buckets instead of full access.
