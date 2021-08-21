# Configuring AWS Glue

## ETL Process with Glue 

1. Create a table in Redshift 

 ![image](https://user-images.githubusercontent.com/48470854/130252068-5f8b099e-ce36-48b3-8f33-247fcdb00170.png)


2. Create Crawlers for data in S3 to create Data Catalog
    - Crawler name : create your crawler name
    - Crawler source type : S3 and its path
    - IAM : Acess in S3 and Redshift, and Glue service role
    - Frequency : Set Up frequency
    - Database : Create your database name 

3. Create Crawlers for the table in Redshift to create Data Catalog
    - Crawler name : create your crawler name
    - Crawler source type : JDBC and Redshift path
    - IAM : Access in S3 and Redshift, and Glue service role
    - Frequency : Set up frequencey
    - Database : create your database name 

![image](https://user-images.githubusercontent.com/48470854/130251234-897c8351-5b51-4bb7-b61b-11940ad07788.png)


4. Run Crawlers
   - You can check here whether the mapping process's status
  
6. Add jobs in ETL  
    - Name : Give ETL name 
    - IAM : Access in S3 and Redshift, and Glue service role
    - Type : Spark
    - Number of worker : increase workers in case of data has a big size
    - Worker type : Higher version of type depends on data size
    - Set source as S3 data catalog while target is Redshift catalog
    - Edit Schema
    - Create Endpoint in VPC to connect VPC to S3
    - Run the job
    - The job fle can be found [here](https://github.com/Syahirahaar/MyDataEngineeringProject/blob/main/Batch%20Processing/ingestion-to-redshift/gluejob_script.py)

![image](https://user-images.githubusercontent.com/48470854/130250510-d2851f5d-f294-4ea1-8e0c-5874863d58d1.png)

6. Check ETL result in the Redshift

![image](https://user-images.githubusercontent.com/48470854/130251955-12e5da73-bafe-45ef-a389-ca3f155010f5.png)


