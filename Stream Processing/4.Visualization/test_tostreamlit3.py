import boto3
import botocore
import os
import configparser
import json
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re

# st.markdown('hoho')
# @st.cache
access_key = os.environ.get('access_key')
secret_key = os.environ.get('secret_key')






#collect_numbers = lambda x : [int(i) for i in re.split("[^0-9]", x) if i != ""]

cust_id = st.text_input("PLease enter customer ID")
#st.write(collect_numbers(numbers))
#st.write(cust_id)

ts = st.text_input("Please enter Timestamp")
#st.write(ts)


# fixed_numbers = st.multiselect("Please select numbers", [1, 2, 3, 4, 5])
# st.write(fixed_numbers)



#Function to connect & fetch data from database
def get_transactions(CustomerID,timestamp,dynamodb=None):
    #client = boto3.client('dynamodb',region_name='ap-southeast-1')
    #dynamodb = boto3.resource('dynamodb', region_name='ap-southeast-1',aws_access_key_id=access_key, aws_secret_access_key = secret_key)
    dynamodb = boto3.resource('dynamodb', region_name='ap-southeast-1',aws_access_key_id=access_key, aws_secret_access_key=secret_key)


    #, endpoint_url="http://localhost:8000"
    # Specify the table to read from
    devices_table = dynamodb.Table('Customers')

    try:
        response = devices_table.get_item(Key={'CustomerID': CustomerID, 'timestamp': timestamp})
    except botocore.exceptions.ClientError as e:
        print(e.response['Error']['Message'])
    else:
        return response['Item']



if __name__ == '__main__':
    #device = get_transactions("096-40-9828", "25/4/2021 16:39",)
    device = get_transactions(cust_id, ts,)
    if device:
        #print("Get Device Data Done:")
        # Print the data read
        #print(device)
        #st.write("Get Device Data Done:")
        # st.write(device)
        # a = pd.DataFrame(device.items(), columns=['header','Details'])
        # st.write(a)

        new = pd.DataFrame.from_dict(device, orient='index')
        st.write(new)


        #pd.DataFrame.from_dict(device)
        #
        #st.table(device)
        #st.text(device)


        #st.line_chart(a)
#source:https://stackoverflow.com/questions/18837262/convert-python-dict-into-a-dataframe/32344037
