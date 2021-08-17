
# Customer Satisfaction level towards AirWorld Airline services
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

Original Dataset

Data Source : https://www.kaggle.com/sjleshrac/airlines-customer-satisfaction
This is original dataset which contain 23 columns
  ![image](https://user-images.githubusercontent.com/48470854/129648458-1eb7117f-a850-43db-b819-7228687b0b22.png)
  
Column List
| Column | Description |
| --- | --- |
| customer_type | Consist of value of Loyal Customer / disloyal Customer |
| satisfaction | Consist of value of satisfied/dissatified |
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
| online_boarding | Factors that influence level of customer’s satisfaction Customer may rate from 0 to 5 Integer |
| dept_delay_mean | Minutes delay during arrival Unit : minutes |
| arrival_delay_min | Minutes delay during arrival Unit : minutes|


 Enriched Dataset
 
After Data Enrichment process applied upon the dataset. These are the snapshot of dataset after treated :
Details : I used Python Faker library to complete enrichment process. You may refer to [PLEASE LINK THE FILE HERE]
  1. Generating fake data 
  2. Cleaning & Merging Process using Jupyter Notebook
  3. File involved ( generate_fake_data.csv & Invistico_Airline.csv )

Column List

| Column | Description |
| --- | --- |
| CustomerID | Uniquely assigned 11 character combined with ‘-’ symbol, No negative number exist, Own by each customer |
| review_id | Uniquely assigned, Own by each customer that create review for the flight |
| flight_id | Uniquely assigned, It comes with letter ‘S’ and append by flight number, It will comes with customer id and review id |
| names | Characters |
| gender | Consist of character of  F: female and M: male |
| customer_type | Consist of value of Loyal Customer / disloyal Customer |
| satisfaction | Consist of value of satisfied/dissatified |
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
| online_boarding | Factors that influence level of customer’s satisfaction Customer may rate from 0 to 5 Integer |
| dept_delay_mean | Minutes delay during arrival, Unit : minutes |
| arrival_delay_min | Minutes delay during arrival, Unit : minutes|
| timestamp | Time recorded during passenger creating the review |
| destination | Destination of passengers that belong to the review |

  ![colummn](https://user-images.githubusercontent.com/48470854/125216516-fe375680-e2f0-11eb-931f-211a418af95b.jpg)
  


# Used Tools

## Connect
- API Gateway :
      - POST ( Take data to API url),  GET ( send data to Lambda Function for validation process)

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

## Others
- IAM roles & policy
- AWS Cloudwatch


# Pipelines


## Stream Processing
1. The layout of streaming process
![image](https://user-images.githubusercontent.com/48470854/129534131-34d256d7-2bc5-4fbf-94e8-1e15df22c723.png)

2.The flow for Streaming Process
    a.  CSV will be pulled into the pipeline by uploading it to API post link through atom
    b. The data that go through API and load it into lambda function will be processed by going through validation to make sure data inserted are in accepted format
    c. After going through the validation process, the data are readily go to Kinesis under stream name APIData
    d. The data will go through two separate flows. First it will go to S3 and will be saved there.Second, it will go to a buffer called Kinesis for further process.
   e. When the data is readily on the stream, it will go to DynamoDB(storage) and distributed into a format set using Lambda function.
   f. All the data that is already parked into dynamoDB, it can be connected to Visualization/ Bi tools. In this case, I’m using Streamlit.
   g. End User may use flight Id to query the data that need to be used. 


3. Details of process :
   1. Preparing Data
   2. Data Ingestion
   3. Data Cleaning
   4. Data Processing & Storage
   5. Visualization
  




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
