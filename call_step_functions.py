# arn:aws:states:eu-west-1:706054169063:stateMachine:MyStateMachineWithChoice

import json
import boto3
import uuid

client = boto3.client("stepfunctions")

def lambda_handler(event, context):
    # Input -> { "TransactionId": "Foo", "Type": "PURCHASE" }
    transactionId = str(uuid.uuid1())

    input = { "TransactionId": transactionId, "Type": "PURCHASE" }

    response = client.start_execution(
        stateMachineArn="arn:aws:states:eu-west-1:706054169063:stateMachine:MyStateMachineWithChoice",
        name=transactionId,
        input=json.dumps(input)
    )