import requests
from requests import Request, Session
from pprint import pprint
import json
import boto3

s3_client = boto3.client('s3',
                         aws_access_key_id='AKIAUHPD7TBAD7OCKQFV',
                         aws_secret_access_key='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',
                         region_name="ap-south-1")

url = 'https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
    'start': '1',
    'limit': '5000',
    'convert': 'USD'
}
headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': '089eb87c-0a6c-458e-97b2-5ef0a948ba36',
}

session = Session()
session.headers.update(headers)

response = session.get(url, params=parameters)
data = json.loads(response.text)
# pprint(data)
json_string = json.dumps(data,
                         skipkeys=True,
                         allow_nan=True,
                         indent=6)
print(json_string)
s3_client.put_object(Body=json_string, Bucket='aws-s3-demo-afroz1234545454154544.basha', Key='new_file.txt')
