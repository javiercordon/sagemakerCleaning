# sagemakerCleaning
AWS Lambda function that deletes active Sagemaker resources

## Background
Removing resources on AWS console for Sagemaker may be a long process if you have many resources. To relieve such task, this Lambda function is capable of removing it, or by using the resources.py

## Description
This project contains a lambda function and its helper (resources.py) to help deleting aws sagemaker resources.

## Usage
Create a Lambda fucntion with the code in the app, attaching the resources.py which contains the functions for deleting in aws.
