import boto3
import botocore
import os
import configparser
import json
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#config = configparser.ConfigParser()
#config.read('/home/me/.aws/credentials')
# config.read("dl.cfg")
#
# os.environ['AWS_ACCESS_KEY_ID']=config['AWS_ACCESS_KEY_ID']
# os.environ['AWS_SECRET_ACCESS_KEY']=config['AWS_SECRET_ACCESS_KEY']

st.markdown('hoho')

#@st.cache


#source video
access_key = os.environ.get('access_key')
secret_key = os.environ.get('secret_key')

#(aws_access_key_id=access_key, aws_secret_access_key = secret_key)

#def get_transactions():
    #client = boto3.client('dynamodb',region_name='ap-southeast-1')
    #dynamodb = boto3.resource('dynamodb', region_name='ap-southeast-1',aws_access_key_id=access_key, aws_secret_access_key = secret_key)
dynamodb = boto3.resource('dynamodb', region_name='ap-southeast-1',aws_access_key_id=access_key, aws_secret_access_key=secret_key)


    #, endpoint_url="http://localhost:8000"
    # Specify the table to read from
devices_table = dynamodb.Table('Customers')
response = devices_table.get_item(Key={'CustomerID': devices_table.CustomerID, 'timestamp': devices_table.timestamp})
print(response['Item'])



# if __name__ == '__main__':
#     device = get_transactions(response)
#     if device:
#         #print("Get Device Data Done:")
#         # Print the data read
#         #print(device)
#         st.write("Get Device Data Done:")
#         st.write(device)
#         a = pd.DataFrame(device.items(), columns=['header','Details'])
#         st.write(a)
#
#         new = pd.DataFrame.from_dict(device, orient='index')
#         st.write(new)


        #pd.DataFrame.from_dict(device)
        #
        #st.table(device)
        #st.text(device)


        #st.line_chart(a)
#source:https://stackoverflow.com/questions/18837262/convert-python-dict-into-a-dataframe/32344037
