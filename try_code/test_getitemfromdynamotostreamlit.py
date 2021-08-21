import boto3
import botocore
import os
import configparser
import json
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

config = configparser.ConfigParser()
#config.read('/home/me/.aws/credentials')
# config.read("dl.cfg")
#
# os.environ['AWS_ACCESS_KEY_ID']=config['AWS_ACCESS_KEY_ID']
# os.environ['AWS_SECRET_ACCESS_KEY']=config['AWS_SECRET_ACCESS_KEY']

st.markdown('hoho')

@st.cache

def load_data(nrows):
    df = pd.read_csv('C:/Users/Syahirahar/Documents/GitHub/MyDataEngineeringProject/Invistico_Airline.csv', nrows=nrows).head(5)
    return df

data_load_state = st.text('Loading data...')
df = load_data(100)
data_load_state.text('Done! (using st.cache)')

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(df)

st.subheader('Gender')
#np.histogram(df['Gender'],bins=[0,20])
#hist_value,bins = np.histogram(df['Gender'],bins)
st.text(df['Gender'])
hist_values = plt.hist(df['Gender'])
st.text(hist_values)

st.bar_chart(hist_values)
# np_array = np.histogram([10, 3, 8, 9, 7], bins=[2, 4, 6, 8, 10])[0]
#
# st.bar_chart(np_array)
#st.bar_chart(hist_values)
#st.write(df)

df1 = df[['Gender']]

st.bar_chart(df1)

cols = ["name", "host_name", "neighbourhood", "room_type", "price"]

# Create histogram dataset
# hist_array, bin_array = np.histogram([4, 10, 3, 13, 8, 9, 7], bins=[2, 4, 6, 8, 10, 12, 14])

# # Set some configurations for the chart
# plt.figure(figsize=[10, 5])
# plt.xlim(min(bin_array), max(bin_array))
# plt.grid(axis='y', alpha=0.75)
# plt.xlabel('Edge Values', fontsize=20)
# plt.ylabel('Histogram Values', fontsize=20)
# plt.title('Histogram Chart', fontsize=25)
#
# # Create the chart
# plt.bar(bin_array[:-1], hist_array, width=0.5, color='blue')
# # Display the chart
# plt.show()

# access_key = 'AKIA6EBJ5GBWCVPKJ6VR'
# secret_key = '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'

#(aws_access_key_id=access_key, aws_secret_access_key = secret_key)

def get_transactions(CustomerID,timestamp,dynamodb=None):
    #client = boto3.client('dynamodb',region_name='ap-southeast-1')
    #dynamodb = boto3.resource('dynamodb', region_name='ap-southeast-1',aws_access_key_id=access_key, aws_secret_access_key = secret_key)
    dynamodb = boto3.resource('dynamodb', region_name='ap-southeast-1',aws_access_key_id=ACCESS_KEY, aws_secret_access_key= SECRET_KEY)


    #, endpoint_url="http://localhost:8000"
    # Specify the table to read from
    devices_table = dynamodb.Table('Customers')

    try:
        response = devices_table.get_item(
            Key={'CustomerID': CustomerID, 'timestamp': timestamp})
    except botocore.exceptions.ClientError as e:
        print(e.response['Error']['Message'])
    else:
        return response['Item']
        #
        # try:
        #     response = devices_table.get_item(
        #         Key={'TransactionType_OriginCountry': TransactionType_OriginCountry, 'Date': Date})
        # except botocore.exceptions.ClientError as e:
        #     print(e.response['Error']['Message'])
        # else:
        #     return response['Item']


if __name__ == '__main__':
    device = get_transactions("096-40-9828", "25/4/2021 16:39")
    if device:
        #print("Get Device Data Done:")
        # Print the data read
        #print(device)
        st.write("Get Device Data Done:")
        st.write(device)
        #pd.DataFrame.from_dict(device)
        #
        #st.table(device)
        #st.text(device)


        #st.line_chart(a)
