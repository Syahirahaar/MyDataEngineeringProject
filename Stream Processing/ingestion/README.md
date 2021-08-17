For a complete and smooth ingestion process, provided below are step-by-step process in creating Lambda function and API configuration

# Create Lambda function in AWS 
Step-by-step :

1. Create Lambda function : WriteKinesis file to enable the process of receiving the data from API Gateway and send to Kinesis

![image](https://user-images.githubusercontent.com/48470854/129696421-2ca006b5-a94b-4525-a2c3-de06c9882589.png)

Then, click CREATE 

2. Connect Lambda function to API Gateway

Click the API Gateway Icon. Bear in mind that initally are trigger . The Icon will show up after you chose what are the service that will be the trigger
  ![image](https://user-images.githubusercontent.com/48470854/129697085-4a9f226b-37be-461f-9b20-d107094d3c2e.png)

  At this button, you can choose API Gateway and choose the API name you created earlier. If you're not so sure. You may go to API Gateway services to check the API stream that you created.
  ![image](https://user-images.githubusercontent.com/48470854/129697349-8f33e448-24a3-494d-8138-7f9648c3a80f.png)
  
  
3. Attach policies to write/read data in Kinesiand to read data in DynamoDB in IAM

![image](https://user-images.githubusercontent.com/48470854/129723842-23d9f8c3-9b73-41c7-af2d-976b93bc85b7.png)

4. Insert python code in the lambda function ([WriteKinesis](https://github.com/Syahirahaar/MyDataEngineeringProject/blob/main/Stream%20Processing/ingestion/WriteKinesis.py) )

![image](https://user-images.githubusercontent.com/48470854/129724164-dadb53f3-72bc-4d34-ab14-1aff86f33d06.png)

5. In the Lambda Function : Deploy and Test with dummy data to makesure data goes from API to Kinesis

Imagine that this is for checking whether the code you write function properly. You may refer to execution results tab to see whether the records successfully processed
  ![image](https://user-images.githubusercontent.com/48470854/129698014-b5ed7f88-c3a4-4cfd-b746-13bc07a40b88.png)



# Create API Gateway

1. Build new REST API in API Gateway 

![image](https://user-images.githubusercontent.com/48470854/129722534-3f9ddcef-1020-4f99-9ed8-c42057eb76f4.png)

2. Create resource and method (POST and GET)

![image](https://user-images.githubusercontent.com/48470854/129722607-80d8162f-67cb-4311-a1f1-e65e464c15c9.png)

3. In order to create connections to lambda functions, click at INTEGRATION Request and do the settings
   - Lambda Region
   - Lambda Function ( choose from above created Lambda function)

4. Create new stage to get the URL for POST

![image](https://user-images.githubusercontent.com/48470854/129722775-3d7687f8-d643-4068-a515-c63e03a22980.png)

![image](https://user-images.githubusercontent.com/48470854/129722852-2f11091f-b09e-4a22-84b1-910460a03baa.png)

![image](https://user-images.githubusercontent.com/48470854/129722979-b8a72e51-48f9-4924-b8c6-bf24332f8939.png)

![image](https://user-images.githubusercontent.com/48470854/129723185-0a6a07f3-23c6-47cb-991f-bd30b2f689d3.png)




# Create Kinesis in AWS 

1. Create data stream in Kinesis 
 ![image](https://user-images.githubusercontent.com/48470854/129725262-447319a6-8524-439c-bba2-7600418028bc.png)
 
2. Configure the number of shard
 ![image](https://user-images.githubusercontent.com/48470854/129725342-0b4b62f2-7fd5-4258-ada3-ba1c69ac443b.png)

3. The data stream are readily accessible 
 ![image](https://user-images.githubusercontent.com/48470854/129725494-d20d77b4-617a-4edd-ac2b-8cf75a155baf.png)


# Start the ingestion process by running the insert_template.py
The link to the file [insert_template.py](https://github.com/Syahirahaar/MyDataEngineeringProject/blob/main/Stream%20Processing/ingestion/insert_template.py)

# Check data insertion in cloudwatch & Kinesis


  






