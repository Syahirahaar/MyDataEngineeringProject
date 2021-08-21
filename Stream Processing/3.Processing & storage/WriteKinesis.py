import json
#import custom_func as cf
import boto3
import jsonschema
from jsonschema import validate
from datetime import datetime

s3_client = boto3.client('s3')
dateTimeObj = datetime.now()

#format the string
timestampStr = dateTimeObj.strftime("%d-%b-%Y-%H%M%S")



custSchema = {
    'type' : 'object',
    'properties' : {
        'customerid' : {'type' : 'string'},
        'review_id' : {'type':'number'},
        'flight_id' :{'type':'string'},
        'names' : {'type':'string'},
        'gender' : {'type':'string'},
        'customer_type' : {'type': 'string'},
        'age' : {'type':'number'},
        'type_of_travel':{'type': 'string'},
        'class':{'type':'string'},
        'flight_distance':{'type':'number'},
        'seat_comfort':{'type':'number'},
        'deptarrive_time_convenient' :{'type':'number'},
        'food_drink':{'type':'number'},
        'gate_location':{'type':'number'},
        'inflight_wifi':{'type':'number'},
        'inflight_entertainment':{'type':'number'},
        'online_support':{'type':'number'},
        'ease_online_booking':{'type':'number'},
        'onboard_service' : {'type':'number'},
        'legroom_service':{'type':'number'},
        'baggage_handling' : {'type':'number'},
        'checkin_service':{'type':'number'},
        'cleanliness' : {'type':'number'},
        'online_boarding':{'type':'number'},
        'dept_delay_min' :{'type':'number'},
        'arrival_delay_min':{'type':'number'},
        'timestamp' : {'type' : 'string'},
        'destination' : {'type':'string'}

    }
}

def validateJson(jsonData):
    try:
        validate(instance=jsonData, schema=custSchema)
    except jsonschema.exceptions.ValidationError as err:
        print("well-formed but invalid JSON:", err)
        # mykey1 = 'error message' + timestampStr + '.txt'
        # response = s3_client.put_object(Body=err, Bucket='test1sy', Key= mykey1)
        return False
    return True

# Convert json to python object.
#jsonData = json.loads('{'name': 'jane doe', 'rollnumber': 25, 'marks': 72, 'customer' : {'Names' :'Alfonso','Age' : '34','customer_type':'loyal cust','type_of_travel':'Work','class':'Business'}}')
# jsonData = json.loads(ak)

# # validate it
# isValid = validateJson(jsonData)
# if isValid:
#     print(jsonData)
#     print('Given JSON data is Valid')
# else:
#     print(jsonData)
#     print('Given JSON data is InValid')


def lambda_handler(event, context):

    print('MyEvent:')
    print(event)

#    mycontext = event.get('context')
#    method = mycontext.get('http-method')
    method = event['context']['http-method']

    if method == 'GET':
        # TODO: write code...
        dynamo_client = boto3.client('dynamodb')

        im_customerid = event['params']['querystring']['customer_id']
        print(im_customerid)
        response = dynamo_client.get_item(TableName = 'Customers', Key = {'customer_id':{'N': im_customerid}})
        print(response['Item'])

        #myreturn = 'This is the return of the get'

        return {
            'statusCode': 200,
            'body': json.dumps(response['Item'])
           }

    elif method == 'POST':



#       mystring = event['params']['querystring']['param1']
        p_record = event['body-json']
        recordstring = json.dumps(p_record)

        client = boto3.client('kinesis')
        response = client.put_record(
        StreamName='APIData',
        Data=recordstring,
        PartitionKey='string'




            )

        jsonData = json.loads(recordstring)
        isValid = validateJson(jsonData)
        if isValid:
            # print(jsonData)
            # print('Given JSON data is Valid')
            return {
                'statusCode': 200,
                'body': json.dumps(p_record)
             }
        else:
            print('Given JSON is invalid',jsonData)

            #error = validateJson.err(recordstring)


            mykey1 = 'error message' + timestampStr + '.txt'
            response = s3_client.put_object(Body=recordstring, Bucket='test1sy', Key= mykey1)

            # print (err.schema['error_msg'])
            return {

                'body': json.dumps(p_record)


             }
    else:
        return {
            'statusCode': 501,
            'body': json.dumps('Server Error')
        }
