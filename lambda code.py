import json
import boto3
from datetime import datetime

s3 = boto3.client('s3')

def lambda_handler(event, context):
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    file_name = event['Records'][0]['s3']['object']['key']

    response = s3.get_object(Bucket=bucket_name, Key=file_name)
    file_content = response['Body'].read().decode('utf-8')
    records = json.loads(file_content)

    total_sales = 0
    total_quantity = 0

    for item in records:
        total_sales += item['quantity'] * item['price']
        total_quantity += item['quantity']

    today = datetime.now().strftime("%Y-%m-%d")

    report = "date,total_sales,total_quantity\n"
    report += f"{today},{total_sales},{total_quantity}"

    s3.put_object(
        Bucket="processed-event-data-sakshi",
        Key=f"large_report_{today}.csv",
        Body=report
    )

    print("Large report generated")

    return {
        'statusCode': 200,
        'body': 'Large data processed'
    }
