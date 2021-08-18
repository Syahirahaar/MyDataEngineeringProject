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




