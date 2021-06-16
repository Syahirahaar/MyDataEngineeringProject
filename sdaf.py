 # Create customer info Row
       #############################

       inventory1_key = dict()
       inventory1_key.update({'CustomerID': {"S": str(dict_record['CustomerID'])}})

       #create export dictionary
       ex_dynamoRecord1 = dict()

       #remove Invoice and Stock code from dynmodb record
       stock1_dict = dict(dict_record)
       stock1_dict.pop('flight_id',None)
       stock1_dict.pop('review_id',None)
       stock1_dict.pop('timestamp',None)
       stock1_dict.pop('review_id',None)
       stock1_dict.pop('flight_distance',None)
       stock1_dict.pop('departure_delay',None)
       stock1_dict.pop('arrival_delay',None)

       #turn the dict into a json
       stock_json1 = json.dumps(stock1_dict)

       #create a record (column) for the InvoiceNo
       #add the stock json to the column with the name of the stock number
       ex_dynamoRecord.update({str(dict_record['names']): {'Value':{"S":stock_json1},"Action":"PUT"}},'flight_id': {"S": str(dict_record['flight_id'])})
       

       #print(ex_dynamoRecord)
       response = client.update_item(TableName='Customers2', Key = inventory1_key, AttributeUpdates = ex_dynamoRecord1)

       response = client.update_item(TableName='string',Key={'string': {'S': 'string','N': 'string','B': b'bytes','SS': ['string',],'NS': [
                'string',
            ],
            'BS': [
                b'bytes',
            ],
            'M': {
                'string': {'... recursive ...'}
            },
            'L': [
                {'... recursive ...'},
            ],
            'NULL': True|False,
            'BOOL': True|False
        }
    },
    AttributeUpdates={'string': {'Value': {'S': 'string','N': 'string','B': b'bytes','SS': ['string',],'NS': ['string',],'BS': [b'bytes',],
            'M': {'string': {'... recursive ...'}},'L': [{'... recursive ...'},],'NULL': True|False,'BOOL': True|False},'Action': 'ADD'|'PUT'|'DELETE'}
    },
