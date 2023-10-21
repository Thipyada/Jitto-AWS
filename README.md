# Web-API-Design-with-AWS

Develop a RESTful web API using Amazon Web Services (AWS) that allows users to manage a collection of items with basic operations in a serverless architecture.

## Project Overview

In this project, you will develop a RESTful web API using AWS that allows users to manage a collection of items with basic operations in a serverless architecture. The items are stored in a DynamoDB table. You will create a DynamoDB table using AWS DynamoDB. You will also create a Lambda function that interacts with the DynamoDB table created. You will use API Gateway to create RESTful API endpoints that trigger the Lambda function. You will use Postman to test the API endpoints. CloudWatch will be used to log information (e.g., errors) about the API calls.

## Project Structure

```
JITTO-AWS/
├── README.md/
├── module/
│ ├── item/
│ │ ├── jittoController.py/
│ │ ├── jittoLogic.py/
│ │ ├── jittoRouter.py/

```

The RESTful API is implemented using the following files:

- jittoController.py: contains functions that interact with the DynamoDB table

  - getAll(): returns a list of items in the DynamoDB table
  - getById(id): returns the item with the specified id from the DynamoDB table
  - create(requestBody): creates a new item in the DynamoDB table

- jittoLogic.py: contains the business logic

  - generateId(): generates a unique id for the item
  - buildResponse(statusCode, body): builds the response object

- jittoRouter.py: contains the routing information
  - lambda_handler(event, context): handles the API request
    - GET /items
    - POST /items
    - GET /items/{id}

## AWS Setup

### DynamoDB

- a DynamoDB table is created with the following attributes:
  - Partition key: `itemId` (String)
  - Other attributes: `name`(String),`description` (String), `createdAt` (String)

### Roles

- named `jitto_aws_function`
- a role is created with the following policies:
  - `AmazonDynamoDBFullAccess`
  - `CloudWatchLogsFullAccess`

### Lambda

- a Lambda function is created with the following configurations:
  - Runtime: `Python 3.9`
  - Permissions: `jitto-role`
  - Trigger: `API Gateway`
  - Function code: `lambda_function.lambda_handler`

### API Gateway

```
- a RESTful API is created with the following configurations:
  - Protocol: `REST`
  - Endpoint Type: `Regional`
  - API name: `Jitto`
  - Resources:
    - /items
      - GET - Integration type: `Lambda Function Proxy` - Lambda function: `jitto-api`
      - POST - Integration type: `Lambda Function Proxy` - Lambda function: `jitto-api`
    - /items/{id}
      - GET - Integration type: `Lambda Function Proxy` - Lambda function: `jitto-api`
```

### API Gateway API key-based authentication and usage plans

- Implement Usage Plans and API Keys to secure the API endpoints.
- Create a usage plan with throttling and quota limits.
- Create an API key and associate it with the usage plan.

```
Usage Plan: Admin
  - Throttling: 100 requests per second
  - Burst: 500 requests
  - Quota: 10000 requests per day
  - API Stage: test (default stage)
Usage Plan: User
  - Throttling: 10 requests per second
  - Burst: 100 requests
  - Quota: 1000 requests per day
  - API Stage: test (default stage)

API Key: Jitto-Admin
  - API Key Name: Jitto_Admin
  - API Key Value: WmJNPDT9e99Ut05ulQnrG6GuIgElPP0s7SD2J72C
  - Enabled: true
  - Usage Plan: Admin
API Key: Jitto_User
  - API Key Name: Jitto_User
  - API Key Value: pFVkC9ALU19q0MhUNTAEU16fzNRQZZRX2GrBhm0U
  - Enabled: true
  - Usage Plan: User
```

### CloudWatch

- a log group is created with the following configurations:
  - Log group name: `/aws/lambda/jitto-api`

## API Endpoints

https://xyr4zso0ma.execute-api.ca-central-1.amazonaws.com/test

### GET /items

https://xyr4zso0ma.execute-api.ca-central-1.amazonaws.com/test/items

- Description: Returns a list of items in the DynamoDB table.

### POST /items

https://xyr4zso0ma.execute-api.ca-central-1.amazonaws.com/test/items

- Description: Creates a new item in the DynamoDB table.

### GET /items/{id}

https://xyr4zso0ma.execute-api.ca-central-1.amazonaws.com/test/items/{id}

- Description: Returns the item with the specified `id` from the DynamoDB table.

## Testing

### Postman

- Postman is used to test the API endpoints.
- The following tests are performed:
  - GET /items
  - POST /items
  - GET /items/{id}
- Headers
  - `x-api-key`: `Jitto_Admin` or `Jitto_User`
  - check the value of `x-api-key` from API Gateway API key-based authentication and usage plans section

#### format for POST /items

body: raw - JSON

```
{
  "name": "string",
  "description": "string"
}
```

- itemId is generated automatically by the Lambda function.
- createdAt is generated automatically by the Lambda function.

#### format for GET /items/{id}

url: https://xyr4zso0ma.execute-api.ca-central-1.amazonaws.com/test/items/1

output:

```
{
  "id": "1",
  "name": "string",
  "description": "string",
  "createdAt": "string"
}
```

## Utilities

- [Postman](https://www.postman.com/) - API Development Environment (Testing Documentation)
- [AWS](https://aws.amazon.com/) - Cloud Computing Services
- [DynamoDB](https://aws.amazon.com/dynamodb/) - NoSQL Database
- [Lambda](https://aws.amazon.com/lambda/) - Serverless Compute
- [API Gateway](https://aws.amazon.com/api-gateway/) - API Management
- [CloudWatch](https://aws.amazon.com/cloudwatch/) - Monitoring and Observability
- [Python](https://www.python.org/) - Programming Language
