import boto3
import botocore
import json
import streamlit as st
import pandas as pd

st.markdown('hoho')

df = pd.read_csv('C:/Users/Syahirahar/Documents/GitHub/MyDataEngineeringProject/Invistico_Airline.csv').head(5)
st.write(df)

ack = 'AKIA6EBJ5GBWCVPKJ6VR'
ps = '62bOhhyH31R8PpApiNFGZWwKVePwzA9z+cyfNPg8'


def get_transactions(TransactionType_OriginCountry,Date,dynamodb=None):
    #client = boto3.client('dynamodb',region_name='ap-southeast-1')
    dynamodb = boto3.resource('dynamodb', region_name='ap-southeast-1')

    #, endpoint_url="http://localhost:8000"
    # Specify the table to read from
    devices_table = dynamodb.Table('Transactions')

    try:
        response = devices_table.get_item(
            Key={'TransactionType_OriginCountry': TransactionType_OriginCountry, 'Date': Date})
    except botocore.exceptions.ClientError as e:
        print(e.response['Error']['Message'])
    else:
        return response['Item']


if __name__ == '__main__':
    device = get_transactions("PURCHASE_USA", 2019-11-21,)
    if device:
        print("Get Device Data Done:")
        # Print the data read
        print(device)
