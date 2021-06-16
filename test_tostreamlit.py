import boto3
import botocore
import json
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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


access_key = 'AKIA6EBJ5GBWCVPKJ6VR'
secret_key = '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'

#(aws_access_key_id=access_key, aws_secret_access_key = secret_key)

def get_transactions(CustomerID,timestamp,dynamodb=None):
    #client = boto3.client('dynamodb',region_name='ap-southeast-1')
    dynamodb = boto3.resource('dynamodb', region_name='ap-southeast-1',aws_access_key_id=access_key, aws_secret_access_key = secret_key)

    # Specify the table to read from
    devices_table = dynamodb.Table('Customers')
    response = devices_table.get_item(Key={CustomerID,timestamp})
    return response
