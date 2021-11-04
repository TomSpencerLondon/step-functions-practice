import json
import random

def lambda_handler(event, context):
    classification = 'Unknown'
    if event['age'] >= 18:
        classification = 'Major'
    return {
        'classification': classification
    }

