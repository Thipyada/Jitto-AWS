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

## Utilities

- [Postman](https://www.postman.com/) - API Development Environment (Testing Documentation)
- [AWS](https://aws.amazon.com/) - Cloud Computing Services
- [DynamoDB](https://aws.amazon.com/dynamodb/) - NoSQL Database
- [Lambda](https://aws.amazon.com/lambda/) - Serverless Compute
- [API Gateway](https://aws.amazon.com/api-gateway/) - API Management
- [CloudWatch](https://aws.amazon.com/cloudwatch/) - Monitoring and Observability
- [Python](https://www.python.org/) - Programming Language
