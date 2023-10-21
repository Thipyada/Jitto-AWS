import json
import random
import string
from decimal import Decimal

def buildResponse(statusCode, body=None):
    response = {
        'statusCode': statusCode,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        }
    }
    if body is not None:
        response['body'] = json.dumps(body)
    
    return response
    

def generateId():
  possible_characters = string.ascii_letters + string.digits
  random_id = ''.join(random.choice(possible_characters) for _ in range(20))
  return random_id