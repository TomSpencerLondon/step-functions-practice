import json
import boto3

client = boto3.client("stepfunctions")


def lambda_handler(event, context):
    executionArn = event['queryStringParameters']['executionArn']
    response = client.describe_execution(executionArn=executionArn)
    status = response['status']
    output = response['output'] if status == 'SUCCEEDED' else ''
    payload = {
        'status': status,
        'output': output
    }
    return {
        'statusCode': 200,
        'body': json.dumps(payload)
    }

