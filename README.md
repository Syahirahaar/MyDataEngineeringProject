
# Customer Satisfaction level towards A Airline services
This Project will show how satisfied the customer towards services provided by airline company. We can see what are the customer's concern when they took flight and how it will impact their journey. However, before giving such an insightful view to the users. We need to makesure the input since the data ingested must go through a good journey so that it can be visualized nicely. Here, I will demonstrate what are the method to make a way or path for the data to travel before it can visualized to the end customer.

# Introduction & Goals
- In order for you to understanding how it works, you need to go through the process by yourself. Here, I challenged myself to create data processing pipeline in both   method which are Batch and Stream Processing.

### Objective of the project :
1 . Study and understand data nature and how it can be process to make useful for the data engineer.
2 . Build Storage pipeline and use batch and Stream processing method pipeline.
3 . Experience real-life handling data using Amazon Services
4 . Knowing what happened behind the beautiful graphs/chart

### The expected outcome from this project :
- Complete pipeline for stream processing
- Complete pipeline for batch processing
- Passenger's rating of services provided by airline
- The tools that will be used for this project are Python,AWS (S3,Lambda,RDS,API gateway) on atom platform
- Tools stated above will be including along the way in the pipeline including preprocessing the data, uploading data into database, triggered lambda to run jobs.
- Visualization are being shown through streamlit for stream processing, and powerBI for batch processing.

# Contents

- [The Data Set](#the-data-set)
- [Used Tools](#used-tools)
  - [Connect](#connect)
  - [Buffer](#buffer)
  - [Processing](#processing)
  - [Storage](#storage)
  - [Visualization](#visualization)
- [Pipelines](#pipelines)
  - [Stream Processing](#stream-processing)
    - [Storing Data Stream](#storing-data-stream)
    - [Processing Data Stream](#processing-data-stream)
  - [Batch Processing](#batch-processing)
  - [Visualizations](#visualizations)
- [Demo](#demo)
- [Conclusion](#conclusion)
- [Follow Me On](#follow-me-on)
- [Appendix](#appendix)


# The Data Set

- The dataset chosen is about Passenger's satisfaction based on services provided. Here are the snapshot for the original verison of data, it is quite complete but still need enrichment for further analysis. The dataset is accessed from kaggle.

Data Source : https://www.kaggle.com/sjleshrac/airlines-customer-satisfaction
This is original dataset which contain 23 columns
  ![image](https://user-images.githubusercontent.com/48470854/129648458-1eb7117f-a850-43db-b819-7228687b0b22.png)
  
After Data Enrichment process applied upon the dataset. These are the snapshot of dataset after treated :
Details : I used Python Faker library to complete enrichment process. You may refer to [PLEASE LINK THE FILE HERE]
  1. Generating fake data 
  2. Cleaning & Merging Process using Jupyter Notebook
  3. File involved ( generate_fake_data.csv & Invistico_Airline.csv )z

| Column | Description |
| --- | --- |
| CustomerID | Uniquely assigned 11 character combined with ‘-’ symbol No negative number exist Own by each customer |
| review_id | Uniquely assigned Own by each customer that create review for the flight |
| flight_id | Uniquely assigned It comes with letter ‘S’ and append by flight number It will comes with customer id and review id |
| names | Characters |
| gender | Consist of character of  F: female and M: male |
| customer_type | Consist of value of Loyal Customer / disloyal Customer |
| age | Only consist of Integer |
| type_of_travel | Consist of value Personal/Business |
| class | Consist of value Business/Eco Determine type of class passengers choose |
| flight_distance | Consist of integer value The unit is miles |
| seat_comfort | Factors that influence level of customer’s satisfaction Customer may rate from 0 to 5 Integer |
| deptarrive_time_convenient | Factors that influence level of customer’s satisfaction Customer may rate from 0 to 5 Integer |
| food_drink | Factors that influence level of customer’s satisfaction Customer may rate from 0 to 5 Integer |
| gate_location | Factors that influence level of customer’s satisfaction Customer may rate from 0 to 5 Integer |
| inflight_wifi | Factors that influence level of customer’s satisfaction Customer may rate from 0 to 5 Integer |
| inflight_entertainment | Factors that influence level of customer’s satisfaction Customer may rate from 0 to 5 Integer |
| online_support | Factors that influence level of customer’s satisfaction Customer may rate from 0 to 5 Integer |
| ease_online_booking | Factors that influence level of customer’s satisfaction Customer may rate from 0 to 5 Integer |
| onboard_service | Factors that influence level of customer’s satisfaction Customer may rate from 0 to 5 Integer |
| legroom_service | Factors that influence level of customer’s satisfaction Customer may rate from 0 to 5 Integer |
| baggage_handling | Factors that influence level of customer’s satisfaction Customer may rate from 0 to 5 Integer |
| checkin_service | Factors that influence level of customer’s satisfaction Customer may rate from 0 to 5 Integer|
| cleanliness | Factors that influence level of customer’s satisfaction Customer may rate from 0 to 5 Integer|
| online_boarding | Show file differences that **haven't been** staged |
| dept_delay_mean | Minutes delay during arrival Unit : minutes |
| arrival_delay_min | Minutes delay during arrival Unit : minutes|
| timestamp | Time recorded during passenger creating the review |
| destination | Destination of passengers that belong to the review |

  ![colummn](https://user-images.githubusercontent.com/48470854/125216516-fe375680-e2f0-11eb-931f-211a418af95b.jpg)
  


# Used Tools
- Explain which tools do you use and why
- I've decided to proceed the project using AWS for both streaming & batch processing pipeline. The services used for orchestrating the pipelines are API Gateway,S3,Lambda,Kinesis,DynamoDB,Redshift,AWS Glue,Cloudwatch,IAM
- As beginner, I found help by asking my coach and collegue, googling all over interent and reading AWS Documentation that are really helpful for my project.

## Connect
- API Gateway :
      - POST ( Take data to API url)
      - GET ( send data to Lambda Function for validation process)

## Buffer
- AWS Kinesis Data Streams
- AWS Kinesis Firehose

## Processing
- AWS Lambda functions
- boto3
- Python3 used in Lambda functions
- AWS Glue -> establish data catalog in Streaming process, also performing ETL between S3 and Redshift


## Storage
- AWS S3 bucket 
- AWS Redshift
- AWS DynamoDB

## Visualization
- Streamlit -> an application used to visualize data from database. Specifically connected to DynamoDB
-  Microsoft PowerBI -> Connected to Redshift


# Pipelines


## Stream Processing
For ease of implementation and testing, we will build the data pipeline in stages. There are 5 stages and these stages shown below  

![image](https://user-images.githubusercontent.com/48470854/129534131-34d256d7-2bc5-4fbf-94e8-1e15df22c723.png)


Pre-connect function
Before the data being processed, data need to be confirmed in what form before proceed to the next stage. In this stage, I'm using Atom platform writing
the code to send the data into API using AWS API Gateway.

Before we send the data into API,there are few things need to be done in order to makesure that can be used optimizely.
1) I used faker library to complete the data.



### Connect Data Stream
In this stages, an API has been initiated and ready to receive data from local csv file. REST API GET method has been initiated to send the response based on the users's request while POST method is for collecting user's data.In the ingestion process, JSON validation is included in Lambda function (WriteKinesis) before the data flowed to Kinesis Stream.
The validation will makesure that only non-Null data can pass.
In this step, while using Lambda function. I have added Lambda Layer consist of python Library to support python's package use for JSON validation.

### Buffer Data Stream 
First, why Buffer needed?. Buffer needed as middleman that hold your data and arrange traffic of data so no data collision can happen.

When the data is ready in kinesis, the following data stream is configured to send the data into different services.

Kinesis - DynamoDB stream: In this data stream, the data is flowing from Kinesis to DynamoDB. Lambda function gets trigger whenever the data is ready inside the kinesis, based on the table partition key and sort key defined in the dynamo DB table and lambda function the data ends up inside the DynamoDB table.

Kinesis - S3 stream: In this data stream, the data is flowing from Kinesis to the S3 bucket. Once the data ends up in the S3 bucket, it is saved inside the s3 bucket in a JSON format. Later the data can be used for different purposes. Again lambda is used here, for the processing of data before saving it inside the S3 bucket.

Kinesis- Kinesis firehose - Redshift stream: This stream pipeline is used to send the data from Kinesis to the Redshift data warehouse. To send the data to Redshift in AWS, a Kinesis firehose is used to send the data into redshift.




### Processing Data Stream

Using lambda, I prepared the code to clean data into 5 columns that has been defined in dynamodb for airline customer. Among the activities done here are pemoving unrelated data from certain columns. By the way, the data are in dictionary form.

In order to makesure that only qualified data inserted into the database. I have included counter measure of validating in in the early stage as early as before the data goes into Kinesis Stream. 

### Storing Data Stream

After data has been processed, it is streamed to different data store.The data store could be S3,DynamoDB,Redshift and others like RDS or medium of storage.

In S3, data format that can be stored are various including CSV,JSON or Parquet.

In this project, medium storage that being used are S3, DynamoDB and Redshift. 

## Visualizations

For Stream Processing, the viualizations can be achieved through fetching data from DynamoDB to Streamlit. It needs some configuration from IAM too. While for batch processing, the data took from Redshift to PowerBI using JDBC.

## Batch Processing


## store
Let's assume that the S3 bucket define below are th place where user will insert the file here. The file will be in .csv format. 
Once the data available in this bucket,initial processing is performed by AWS Lambda everyday 
![image](https://user-images.githubusercontent.com/48470854/125758392-5c3e805d-bb27-497a-8f56-dd279e3aedfc.png)

## Processing
In the processing stage, aws glue has been used to process 
![image](https://user-images.githubusercontent.com/48470854/127276722-0b549435-e10d-4764-bec4-719235ddcb7b.png)


## Visualizations

# Demo
- You could add a demo video here
- Or link to your presentation video of the project

# Conclusion
Write a comprehensive conclusion.
- How did this project turn out
- What major things have you learned
- What were the biggest challenges

# Follow Me On
Add the link to your LinkedIn Profile

# Appendix

[Markdown Cheat Sheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)
