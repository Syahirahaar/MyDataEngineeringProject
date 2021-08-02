#source: https://www.youtube.com/watch?v=FKlubuXiLEc

import boto
import boto.s3.connection
from io import StringIO
import boto3
import pandas as pd
import sys
import os

access_key = 'AKIA6EBJ5GBWBDOYUFO4'
secret_key = '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'

conn = boto.connect_s3(aws_access_key_id=access_key, aws_secret_access_key = secret_key)

#listing all buckets
for bucket in conn.get_all_buckets():
    print("{name}\t(created)".format(name=bucket.name,created=bucket.creation_date,))

#createbucket
#bucket1 = conn.create_bucket('syahirah21') -- will be created in east virginia region

#loading csv into s3 bucket
# file = pd.read_csv('Invistico_Airline.csv')
#
# s3 = boto3.client('s3',aws_access_key_id = access_key, aws_secret_access_key=secret_key)
# csv_buf = StringIO()
#
# file.to_csv(csv_buf,header=True,index=False)
# csv_buf.seek(0)
# s3.put_object(Bucket='mydataengineeringbucket', Body=csv_buf.getvalue(), Key='airline.csv')

#Read data from s3 bucket
# if sys.version_info[0]<3:
#     from stringIO import stringIO
# else:
#     from io import StringIO
#
# client = boto3.client('s3',aws_access_key_id = access_key, aws_secret_access_key=secret_key)
#
# bucket_name = 'mydataengineeringbucket'
# object_key = 'airline.csv'
#
# csv_obj = client.get_object(Bucket=bucket_name, Key=object_key)
# body = csv_obj['Body']
# csv_string = body.read().decode('utf-8')
#
# df = pd.read_csv(StringIO(csv_string))
# print(df.head())

#delete bucket
# bucket2 = conn.get_bucket('mydataengineeringbucket')
# bucket2.delete_key('airline.csv')
