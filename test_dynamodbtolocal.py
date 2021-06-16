import boto3

access_key = 'AKIA6EBJ5GBWCVPKJ6VR'
secret_key = '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'

dynamodb = boto3.resource('dynamodb', region_name='ap-southeast-1',aws_access_key_id=access_key, aws_secret_access_key = secret_key)
list(dynamodb.tables.all())
