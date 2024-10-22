import boto3
import botocore
access_key = 'AKIA6EBJ5GBWCVPKJ6VR'
secret_key = '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'
#
# def create_customer_table(dynamodb=None):
#     if not dynamodb:
#         dynamodb = boto3.resource('dynamodb', region_name='ap-southeast-1',aws_access_key_id=access_key, aws_secret_access_key = secret_key)
#
#     table = dynamodb.create_table(
#         TableName='customer',
#         KeySchema=[
#             {
#                 'AttributeName': 'cust_id',
#                 'KeyType': 'HASH'  # Partition key
#             },
#             {
#                 'AttributeName': 'timestamp',
#                 'KeyType': 'RANGE'  # Sort key
#             }
#         ],
#         AttributeDefinitions=[
#             {
#                 'AttributeName': 'Names',
#                 'AttributeType': 'S'
#             },
#             {
#                 'AttributeName': 'Age',
#                 'AttributeType': 'N'
#             },
#             {
#                 'AttributeName': 'customer_type',
#                 'AttributeType': 'S'
#             },
#             {
#                 'AttributeName': 'type_of_travel',
#                 'AttributeType': 'S'
#             },
#             {
#                 'AttributeName': 'class',
#                 'AttributeType': 'S'
#             },
#
#         ],
#         ProvisionedThroughput={
#             'ReadCapacityUnits': 1,
#             'WriteCapacityUnits': 1
#         }
#     )
# #     return table
# #
# #
# # if __name__ == '__main__':
# #     movie_table = create_customer_table()
# #     print("Table status:", movie_table.table_status)
#
#
#     # Wait until the table exists.
# table.meta.client.get_waiter('table_exists').wait(TableName='customer')
#
#     # Print out some data about the table.
# print(table.item_count)



import boto3

# Get the service resource.
dynamodb = boto3.resource('dynamodb', region_name='ap-southeast-1',aws_access_key_id=access_key, aws_secret_access_key = secret_key)


# Create the DynamoDB table.
table = dynamodb.create_table(
    TableName='users',
    KeySchema=[
        {
            'AttributeName': 'username',
            'KeyType': 'HASH'
        },
        {
            'AttributeName': 'last_name',
            'KeyType': 'RANGE'
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'username',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'last_name',
            'AttributeType': 'S'
        },
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }
)

# Wait until the table exists.
table.meta.client.get_waiter('table_exists').wait(TableName='users')

# Print out some data about the table.
print(table.item_count)
