# FORTUNE_TELLER

This online application is a basic fortune teller that will help you make predictions about the future. The objective is to demonstrate the creation and deployment of an AWS Mini Project utilizing AWS Lambda and AWS API Gateway, followed by the public release of the fortune-telling web application via the API Gateway Gateway.

aws lambda - Amazon Web Services (AWS) Lambda is a serverless computing service that allows you to run your code without provisioning or managing servers. AWS Lambda lets you run your code in response to events and automatically manages the computing resources for you.
Amazon API Gateway - Amazon API Gateway, a fully managed service that makes it easy for developers to create, publish, maintain, monitor, and secure APIs at any scale.

STEP 1: SET UP AN AWS LAMBDA FUNCTION
• Open the AWS Management Console and navigate to the Lambda service. Click "Create function" and select "Author from scratch." Enter the name of your function. Select the runtime as Python. Under function code test the code first then write the code for choice yes or no using if statement and random import of python. Define a function that generates a random integer 1,2 or 3 responding to "yes", "no" and "maybe" respectively. Return the response as the output of the Lambda function

STEP 2: SET UP AN AWS API GATEWAY - Open the AWS API Gateway service in the AWS Console. Click "Create API" and choose "HTTP API" . Define the route method: GET with integrating Lambda . Add parameter mapping for the request query string which takes your question as the query string input.

STEP 3: DEPLOY YOUR CODE - In the API Gateway console, click "Deployments" and then "Create." Select the stage (e.g., "dev") and deploy the API. Copy the API endpoint URL, which users will use to access the Application.
