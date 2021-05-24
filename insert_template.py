import pandas as pd
import requests

#URL OF ENDPOINT
URL =

#read the local file
data = pd.read_cvs('airline.csv'), sep=','

for i in data.index:
    export = data.loc[i].to_json()

    response = requests.post(URL,data=export)

    print(response)
