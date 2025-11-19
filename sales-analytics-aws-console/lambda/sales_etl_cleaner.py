import os
import boto3
import csv
import io
import traceback

s3 = boto3.client('s3')

def log(msg):
    print(msg)

def lambda_handler(event, context):
    '''
    Console-friendly Lambda handler.
    Expects environment variables:
      RAW_BUCKET - source bucket name
      CLEAN_BUCKET - destination bucket name

    Trigger: S3 PUT event (object created)
    '''
    try:
        log("EVENT RECEIVED:")
        log(event)

        raw_bucket = os.environ.get('RAW_BUCKET', 'sales-raw-sivam01')
        clean_bucket = os.environ.get('CLEAN_BUCKET', 'sales-clean-sivam01')

        # Validate event
        if 'Records' not in event or len(event['Records']) == 0:
            log("No Records in event. Exiting.")
            return {"status": "no_records"}

        key = event['Records'][0].get('s3', {}).get('object', {}).get('key')
        if not key:
            log("No object key found in event. Exiting.")
            return {"status": "no_key"}

        log(f"Processing key: {key} from bucket: {raw_bucket}")

        obj = s3.get_object(Bucket=raw_bucket, Key=key)
        data = obj['Body'].read().decode('utf-8').splitlines()
        reader = csv.reader(data)

        try:
            header = next(reader)
        except StopIteration:
            header = []

        cleaned_rows = []
        for i, row in enumerate(reader, start=1):
            # Simple cleaning: skip rows with any empty cell
            if any((cell is None) or (str(cell).strip() == '') for cell in row):
                log(f"Skipping row #{i} (empty cell): {row}")
                continue
            cleaned_rows.append(row)

        # Write cleaned CSV
        output = io.StringIO()
        writer = csv.writer(output)
        if header:
            writer.writerow(header)
        if cleaned_rows:
            writer.writerows(cleaned_rows)

        s3.put_object(Bucket=clean_bucket, Key=key, Body=output.getvalue())
        log(f"Uploaded cleaned file to s3://{clean_bucket}/{key} (rows_written={len(cleaned_rows)})")

        return {"status": "success", "input_key": key, "rows_written": len(cleaned_rows)}

    except Exception as e:
        log("Exception during processing:")
        traceback.print_exc()
        return {"status": "error", "message": str(e)}
