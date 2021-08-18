> Cleaning & Validation here involves process of including JSON validation code into WriteKinesis.py ( recap : this file will take data from API and pass it to Kinesis).
> In the same lambda Function, a set of validation code inserted to make sure only the right data woth the right format are accepted to go through it.

> Here, I showed you a snapshot of validation code

1. Start with defining the columns
![image](https://user-images.githubusercontent.com/48470854/129819433-5a0fa752-830b-4edd-9599-9293ae727c05.png)

2. Slide the code into Lambda handler and start comparing with the data that flowing into the stream. Throw error if the input cannot be accepted according to picture number(1)
![image](https://user-images.githubusercontent.com/48470854/129819852-5fc34410-0329-4d56-84ce-2cc7eeb6965e.png)

Expected Result :
> A set in database that have no null value or mixed value 


Reason Doing Validation
  - At first time I've done with my coach, I dod not include the validation process to because we focus just to make the pipeline works. However, after all finished. I were asked by my coach to insert the validation. It is for more efficient processing pipeline because at the end of the day, we only want quality data to be kept in the database that will be query by thousands of customer.

** future : insert comparison of output for with validation and w/o validation **





