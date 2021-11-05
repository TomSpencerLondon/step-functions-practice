import json
import boto3
import uuid

client = boto3.client("stepfunctions")


def lambda_handler(event, context):
    print(event)
    response = client.start_execution(
        stateMachineArn="arn:aws:states:eu-west-1:706054169063:stateMachine:MyStateMachineWithChoice",
        input=event['body']
    )

    return {
        "isBase64Encoded": False,
        "statusCode": 200,
        "body": f"{{\"executionArn\": \"{response['executionArn']}\" }}",
        "headers": {
            "content-type": "application/json"
        }
    }
