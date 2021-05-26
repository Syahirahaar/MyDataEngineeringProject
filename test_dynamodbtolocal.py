import boto3

dynamodb = boto3.resource('dynamodb')
list(dynamodb.tables.all())
