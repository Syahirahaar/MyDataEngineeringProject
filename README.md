
# Customer Satisfaction level towards A Airline services
This Project will show how satisfied the customer towards services provided by airline company. We can see what are the customer's concern when they took flight and how it will impact their journey. However, before giving such an insightful view to the users. We need to makesure the input since the data ingested must go through a good journey so that it can be visualized nicely. Here, I will demonstrate what are the method to make a way or path for the data to travel before it can visualized to the end customer.

# Introduction & Goals
- In order for you to understanding how it works, you need to go through the process by yourself. Here, I challenged myself to create data processing pipeline in both   method which are Batch and Stream Processing.
- Orient this section on the Table of contents
- Objective of the project :
1 . Study and understand data nature and how it can be process to make useful for the data engineer.
2 . Build Storage pipeline and use batch and Stream processing method pipeline.
3 . Experience real-life reality situation
4 . Knowing what happened behind the beautiful graphs/chart

First Header | Second Header
------------ | -------------
Content from cell 1 | Content from cell 2
Content in the first column | Content in the second columnFirst Header | Second Header
------------ | -------------
Content from cell 1 | Content from cell 2
Content in the first column | Content in the second column

- Write this like an executive summary
  - Passenger's rating of services provided by airline
  - The tools that will be used for this project are Python,AWS (S3,Lambda,RDS,API gateway) on atom platform
  - Tools stated above will be including along the way in the pipeline including preprocessing the data, uploading data into database, triggered lambda to run jobs.
  - Once you are finished add the conclusion here as well

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
- Explain the data set
  The dataset chosen is about Passenger's satisfaction based on services provided. Here are the snapshot for the original verison of data, it is quite complete but stll need enrichment for further analysis. The dataset is accessed from kaggle, here is the link https://www.kaggle.com/sjleshrac/airlines-customer-satisfaction. I've attached the airline.csv in my Github folders.
  
  ![colummn](https://user-images.githubusercontent.com/48470854/125216516-fe375680-e2f0-11eb-931f-211a418af95b.jpg)
  
  ![colummn](https://user-images.githubusercontent.com/48470854/125216522-068f9180-e2f1-11eb-8da2-80926f3ef6ac.jpg)


- Why did you choose it?
- I'm interested to explore airline's related data. In my upcoming project, I might working with airline project. Thus, I think this is a good start for me.
- What do you like about it?
- The data is a lot, and has meaningful columns for analysis

- What is problematic?
  The data has no features that makes it unique, thus an enrichment process needed to make it self-explained. I'm using FakerLibrary to add columns that will add value to the dataset. 


# Used Tools
- Explain which tools do you use and why
- I've decided to proceed the project using AWS for both streaming & batch processing pipeline. The services used for orchestrating the pipelines are API Gateway,S3,Lambda,Kinesis,DynamoDB,Redshift,AWS Glue,Cloudwatch,IAM
- As beginner, I found help by asking my coach and collegue, googling all over interent and reading AWS Documentation that are really helpful for my project.

## Connect
In the scenario of stream processing, a data pipeline will pull data from an API and send data to the buffer.AWS API Gateway POST method is used to pull data from the client.
Every time data reach to the API endpoint, it will trigger the lambda function and send data to AWS Kinesis.

## Buffer
In buffer stage, the services that being used are AWS Kinesis & Firehose. For Streaming processing, Kinesis stream being used to allow data that has been triggered from lambda to go sit in kinesis stream ro queue the data, The data will lineup in Kinesis every time the API endpoint trigger the lambda function in the AWS.The Kinesis firehose is used to send the data inside the warehouse.

## Processing
AWS Lambda is used to perform stream processing at different stages.The lambda is used to send data from API to Kinesis, Kinesis to S3 bucket, Kinesis to DynamoDB, Kinesis to Redshift

## Storage
For storage,we need a place to put data so that it can be accessible for reference or even to re-use back the data. It can be holding raw/processed data. What are being used are S3,DynamoDB and Redshift. S3 stands for simple storage service, it is like data lake in AWS environment.The method I'm using is keeping the data in JSON format.Secondly, DynamoDB is a NoSQL database and saving the data in wide column format. AWS Redshift is datawarehouse that allowing us to create schema inside its cluster and saved streamed data in a table.   

## Visualization
I have been using different visualization tool for both streaming & batch processing. For streaming, I used streamlit app to visualize and fetch from DynamoDB. Batch Processing is using PowerBI to visualize data from Redshift. 


# Pipelines


## Stream Processing
For ease of implementation and testing, we will build the data pipeline in stages. There are 5 stages and these stages shown below  
![image](https://user-images.githubusercontent.com/48470854/122516888-e813de80-d041-11eb-9b91-1098ab88895c.png)

- Explain the pipelines for processing that you are building

<img width="353" alt="pipeline" src="https://user-images.githubusercontent.com/48470854/117396308-3fe00580-af2c-11eb-8bd5-e6f04acc5c85.png">


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
