import boto3

def lambda_handler(event, context):
    client = boto3.resource('dynamodb')
    table = client.Table('Transactions')

    #string number map datatype


    input = {'TransactionId' : '31', 'State' : 'PENDING', 'RelatedTransactions' : [32,33,34], 'CustomerDetails' : {'Name' :'John Doe', 'AccountBalance' : 50}}
    input = {'TransactionType_OriginCountry':'PURCHASE_USA', 'Date' : '2019-10-22'}
    response = table.put_item(Item=input)
