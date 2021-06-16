import pandas as pd
import requests

#URL OF ENDPOINT
URL = 'https://p6pq7a2yf5.execute-api.ap-southeast-1.amazonaws.com/test/getdata'


#read the local file
data = pd.read_csv('sample_data.csv', sep=',')


for i in data.index:
    try:
        # convert the row to json
        export = data.loc[i].to_json()

        #send it to the api
        response = requests.post(URL, data = export)

        # print the returncode
        print(export)
        print(response)
    except:
        print(data.loc[i])
