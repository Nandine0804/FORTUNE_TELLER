import json
import random

def random_integer():
    options=[1,2,3]
    return random.choice(options)
def lambda_handler(event,context):
    option=random_integer()
    if option == 1:
        value="yes"
        if option == 2:
            value="no"
    else:
        value="may be"
    message=f"{value}"
    return {
        'statusCode': 200,
        'body': json.dumps(message)
    }
