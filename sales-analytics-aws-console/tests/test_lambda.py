import unittest
from unittest.mock import MagicMock, patch
import io
import json

# Import the lambda module (ensure path is correct when running tests)
import lambda.sales_etl_cleaner as handler_module

class TestLambdaHandler(unittest.TestCase):

    @patch('lambda.sales_etl_cleaner.s3')
    def test_lambda_handler_success(self, mock_s3):
        # Prepare a small CSV
        csv_content = 'order_id,product,quantity,price,date\n101,Mobile,2,15000,2024-01-01\n'
        mock_obj = {'Body': io.BytesIO(csv_content.encode('utf-8'))}
        mock_s3.get_object.return_value = mock_obj
        mock_s3.put_object.return_value = {}

        event = {
            "Records": [
                {"s3": {"bucket": {"name": "sales-raw-sivam01"}, "object": {"key": "sales.csv"}}}
            ]
        }

        resp = handler_module.lambda_handler(event, None)
        self.assertEqual(resp['status'], 'success')
        self.assertIn('rows_written', resp)

if __name__ == '__main__':
    unittest.main()
