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


# Create Redshift table

1. Create Redshift and configure things below

![image](https://user-images.githubusercontent.com/48470854/130171600-6e88a9fe-987d-4cdf-ab95-7259c230ecde.png)

2. Set the configuration as below
   - Go to EC2 > Security Groups > your security groups > Edit inbound rules
   - Type - All TCP,
   - Protocol - TCP,
   - Port range - 0-65535,
   - Source - Choose the security groups

3. At Network and security settings, set Publicly accessible to 'Enabled'

![image](https://user-images.githubusercontent.com/48470854/130175138-72a0de4c-7478-405e-81cc-eb69bbfc44f0.png)
   

![image](https://user-images.githubusercontent.com/48470854/130172208-a856f24d-52a7-463f-ae6b-23b197ff91bd.png)

4.






2. After table crated and configured as above. You may see the 

![image](https://user-images.githubusercontent.com/48470854/130171465-494fa175-abbf-4ad4-b8d7-4aaf83d557fc.png)






