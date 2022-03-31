 # How To Create Lambda for being intermediate to write to Kinesis/S3/DynamoDB/Redshift

### Configuring for Lambda Write To Kinesis 
   Here are the code page to see how to take data that has been sent through API to Kinesis : [WriteKinesis](https://github.com/Syahirahaar/MyDataEngineeringProject/blob/main/Stream%20Processing/3.Processing%20%26%20storage/WriteKinesis.py )
 During creation of Lambda function, we also need to configure event to enable the schema compatible, below are the screenshot for event that I configured suitable for my code. Here is the [event] (https://github.com/Syahirahaar/MyDataEngineeringProject/blob/main/Stream%20Processing/3.Processing%20%26%20storage/Event_JSON_lambdaWriteToKinesis.txt)
 
 
### Configuring for Lambda Write To Dynamo 

Steps to create Lambda :
1. Create Function > Choose Blueprint > type kinesis at the search box > choose kinesis-process-record-python > may write your own code 
2. Here is the [code](https://github.com/Syahirahaar/MyDataEngineeringProject/blob/main/Stream%20Processing/3.Processing%20%26%20storage/Write-to-dynamodb.py)
   
### Configuring for Lambda from Kinesis To S3 

Steps to create Lambda function :
1. Create Function > Choose Blueprint > type kinesis at the search box > choose kinesis-process-record-python > may write your own code
2. Here is the [code](https://github.com/Syahirahaar/MyDataEngineeringProject/blob/main/Stream%20Processing/3.Processing%20%26%20storage/Write-Kinesis-To-S3.py)




In this stage, processes that occurred here are creating S3 bucket, sending the raw data that accepted from API into S3 bucket, creating dynamoDB table,, configuring the Lambda file that enable the insertion into S3 and DynamoDB

# Create S3 bucket ( for sending records accepted into Kinesis )

1. Below are S3 bucket snapshot and example files that automatically created there

![image](https://user-images.githubusercontent.com/48470854/129829126-91332d4e-e810-491c-9585-ac08a7a5499c.png)

2. Create a Lambda function and put down the Lambda Code ([WriteToS3](https://github.com/Syahirahaar/MyDataEngineeringProject/blob/main/Stream%20Processing/processing%20%26%20storage/stream-to-s3.py))


3. Give the Lambda roles in IAM to read kinesis and write data to S3

![image](https://user-images.githubusercontent.com/48470854/129829661-1e72c01c-314a-4bff-813d-1b30d177133f.png)

4. Then, every time data are inserted. The file will ve created at S3 to show the successfully processed record are being recorded into S3 ( look in the orange box )

![image](https://user-images.githubusercontent.com/48470854/129829126-91332d4e-e810-491c-9585-ac08a7a5499c.png)


# Create DynamoDB table

Pick a suitable name for your table

1. Click CREATE icon. In this stage, you need to define the primary key for the table

![image](https://user-images.githubusercontent.com/48470854/129895403-642de866-fe11-4a39-a2e7-e5310d45e208.png)

2. This is the snapshot for existing tables in DynamoDB 
![image](https://user-images.githubusercontent.com/48470854/129895528-3e975772-d5c8-4077-8fa3-547cf6ce882c.png)

3. Steps to create table in dynamoDB including configuring PK, Sortkey, creating item 
   - PK and SK can be configured during creating the table 
   - creating item depends on data structure data. In my case, here is my data : <img width="685" alt="create_dynamo_table_2022" src="https://user-images.githubusercontent.com/48470854/161019047-8af38032-ee52-4509-990e-da47919aebbf.png">
   - When you create item, the data structure that need to be choose as list as above  



# Create Redshift table

1. Create Redshift and configure things below

![image](https://user-images.githubusercontent.com/48470854/130171600-6e88a9fe-987d-4cdf-ab95-7259c230ecde.png)

2. Set the configuration as below
   - Go to EC2 > Security Groups > your security groups > Edit inbound rules
   - Type - All TCP,
   - Protocol - TCP,
   - Port range - 0-65535,
   - Source - Choose the security groups

![image](https://user-images.githubusercontent.com/48470854/130172208-a856f24d-52a7-463f-ae6b-23b197ff91bd.png)

3. At Network and security settings, set Publicly accessible to 'Enabled'

![image](https://user-images.githubusercontent.com/48470854/130175138-72a0de4c-7478-405e-81cc-eb69bbfc44f0.png)

4. Create a table in the cluster in query editor

![image](https://user-images.githubusercontent.com/48470854/130176505-4851ab31-b766-430d-b803-3891c2762a4d.png)

   
5. Set Redshift roles in IAM to read/write data in S3 and read data in Kinesis



6. After table crated and configured as above. You may see the existing query 

![image](https://user-images.githubusercontent.com/48470854/130171465-494fa175-abbf-4ad4-b8d7-4aaf83d557fc.png)

7. After created the table, you can use below command to check the error if the data is not loaded

![image](https://user-images.githubusercontent.com/48470854/130178393-820ab5fa-2a79-4718-86a6-f6c328a08e23.png)

   - Below are the example queries that can be used to check if any errors arised

![image](https://user-images.githubusercontent.com/48470854/130178269-5a6264c0-1574-46e8-835e-6d91f5bc6853.png)





8. Create S3 bucket (Intermediate Storage)
Upload [jsonpaths.json](https://github.com/Syahirahaar/MyDataEngineeringProject/blob/main/Stream%20Processing/visualization/jsonpaths.json) file ( for mapping and detect json string object ) in the S3 bucket


8. Creating Kinesis Firehose and connections to the Redshift
     - Create a delivery stream
     - Set the source : Kinesis Data Stream
     - Destination : Redshift (Put down info,about the cluster)
     - Intermediate S3 destination : Choose S3 bucket created for intermediate storage
     - COPY command : Copy & paste [copy command](https://github.com/Syahirahaar/MyDataEngineeringProject/blob/main/Stream%20Processing/processing%20%26%20storage/copycommand.txt) into Intermediate bucket 


 










