import json
import base64
import boto3

from datetime import datetime

def lambda_handler(event, context):

    client = boto3.client('dynamodb')

    # This function will take the record from kinesis, decode the data and convert it into string, then dictionary
    for record in event['Records']:
        # Kinesis data is base64 encoded so decode here
        t_record = base64.b64decode(record['kinesis']['data'])

        # decode the bytes into a string
        str_record = str(t_record,'utf-8')

        #transform the json string into a dictionary
        dict_record = json.loads(str_record)

       #Update customer & timestamp key
        customer_key = dict()
        customer_key.update({'CustomerID': {"S": str(dict_record['CustomerID'])},'timestamp' : {"S": str(dict_record['timestamp'])}})

       # Clean data for customer row, as per taken all the data and remove attributes not needed for customer column
        c_dict = dict(dict_record)
        c_dict.pop('Unnamed: 0',None)
        c_dict.pop('flight_id',None)
        c_dict.pop('review_id',None)
        c_dict.pop('CustomerID',None)
        c_dict.pop('timestamp',None)
        c_dict.pop('seat_comfort',None)
        c_dict.pop('online_boarding',None)
        c_dict.pop('checkin_service',None)
        c_dict.pop('legroom_service',None)
        c_dict.pop('ease_online_booking',None)
        c_dict.pop('online_support',None)
        c_dict.pop('inflight_entertainment',None)
        c_dict.pop('inflight_wifi',None)
        c_dict.pop('gate_location',None)
        c_dict.pop('food_drink',None)
        c_dict.pop('departure_arrival',None)
        c_dict.pop('deptarrive_time_convenient',None)
        c_dict.pop('onboard_service',None)
        c_dict.pop('baggage_handling',None)
        c_dict.pop('cleanliness',None)
        c_dict.pop('destination',None)

        #turn the dict into a json
        cust_json = json.dumps(c_dict)

        #update customer column
        #response = client.update_item(TableName='Customers2', Key = customer_key)

        #clean data to be feed into flight column
        f_dict = dict(dict_record)
        f_dict.pop('flight_id',None)
        f_dict.pop('Unnamed: 0',None)
        f_dict.pop('review_id',None)
        f_dict.pop('CustomerID',None)
        f_dict.pop('timestamp',None)
        f_dict.pop('names',None)
        f_dict.pop('age',None)
        f_dict.pop('gender',None)
        f_dict.pop('customer_type',None)
        f_dict.pop('type_of_travel',None)
        f_dict.pop('class',None)
        f_dict.pop('seat_comfort',None)
        f_dict.pop('online_boarding',None)
        f_dict.pop('checkin_service',None)
        f_dict.pop('legroom_service',None)
        f_dict.pop('ease_online_booking',None)
        f_dict.pop('online_support',None)
        f_dict.pop('inflight_entertainment',None)
        f_dict.pop('inflight_wifi',None)
        f_dict.pop('gate_location',None)
        f_dict.pop('food_drink',None)
        f_dict.pop('departure_arrival',None)
        f_dict.pop('deptarrive_time_convenient',None)
        f_dict.pop('onboard_service',None)
        f_dict.pop('baggage_handling',None)
        f_dict.pop('cleanliness',None)
        f_dict.pop('destination',None)

        #turn the dict into a json
        flight_json = json.dumps(f_dict)


        #remove Invoice and Stock code from dynmodb record
        rv_dict = dict(dict_record)
        rv_dict.pop('flight_id',None)
        rv_dict.pop('Unnamed: 0',None)
        rv_dict.pop('review_id',None)
        rv_dict.pop('CustomerID',None)
        rv_dict.pop('timestamp',None)
        rv_dict.pop('names',None)
        rv_dict.pop('age',None)
        rv_dict.pop('gender',None)
        rv_dict.pop('customer_type',None)
        rv_dict.pop('type_of_travel',None)
        rv_dict.pop('class',None)
        rv_dict.pop('review_id',None)
        rv_dict.pop('flight_distance',None)
        rv_dict.pop('dept_delay_min',None)
        rv_dict.pop('arrival_delay_min',None)

        #turn the dict into a json
        rv_json = json.dumps(rv_dict)


       #update table customers
        response = client.update_item(TableName='Customers', Key = customer_key,AttributeUpdates={'flight':{'Value':{"S": flight_json}},'reviews':{'Value':{"S":rv_json}},'customer':{'Value':{"S":cust_json}},'flight_id':{'Value':{"S": str(dict_record['flight_id'])}}})




    return 'Successfully processed {} records.'.format(len(event['Records']))
