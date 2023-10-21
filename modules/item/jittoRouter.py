import logging
import json
from jittoLogic import buildResponse
from jittoController import getAll, getById, create

logger = logging.getLogger()
logger.setLevel(logging.INFO)

routes = {
    "GET": {
        "/items": getAll,
        "/items/{id}": getById
    },
    "POST": {
        "/items": create
    }
}


def lambda_handler(event, context):
    logger.info(event)
  
    httpMethod = event['httpMethod']
    resource = event['resource']
    
    if httpMethod in routes and resource in routes[httpMethod]:
        if httpMethod == 'GET':
            if '{id}' in resource:
                id = event['pathParameters']['id']
                return routes[httpMethod][resource](id)
            else:
                return routes[httpMethod][resource]()
        else:
            requestBody = json.loads(event['body'])
            return routes[httpMethod][resource](requestBody)
    else:
        return buildResponse(404, {'Message': 'Not Found'})
