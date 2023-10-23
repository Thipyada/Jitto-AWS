import boto3
import datetime
from jittoLogic import generateId, buildResponse

dynamodbTableName = 'items-collection'
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(dynamodbTableName)

def getAll():
    try:
        response = table.scan()
        if len(response) == 0:
            return buildResponse(404, {'Message': 'No items found'})
        
        return buildResponse(200, response['Items'])
    except Exception as e:
        return buildResponse(404, {'error': str(e)})


def getById(id):
    try:
        response = table.get_item(
            Key={
                'itemId': id
            }
        )
        if 'Item' not in response:
            return buildResponse(404, {'Message': 'Item not found'})

        return buildResponse(200, response['Item'])
    except Exception as e:
        return buildResponse(404, {'error': str(e)})



def create(requestBody):
    try:
        requiredFields = ['name', 'description']
        missingFields = [ field for field in requiredFields if field not in requestBody ]

        if len(missingFields) > 0:
            return buildResponse(404, {'Message': 'Missing fields: {}'.format(', '.join(missingFields))})
        
        requestBody['itemId'] = generateId()
        requestBody['createdAt'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        table.put_item(Item=requestBody)
        body = {
            'Message': 'Item created',
            'Item': requestBody
        }
        return buildResponse(200, body)
    except Exception as e:
        return buildResponse(404, {'error': str(e)})
