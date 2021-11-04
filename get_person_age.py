import json
import random

def lambda_handler(event, context):
    age = random.randint(1, 100);
    return {
        'age': age
    }

