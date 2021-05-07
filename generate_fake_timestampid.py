#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 18:55:19 2019

@author: krishnaparekh
"""

import csv
from faker import Faker
import datetime

def datagenerate(records, headers):
    fake = Faker('en_US')
    #fake1 = Faker('en_GB')   # To generate phone numbers
    with open("ts_id.csv", 'wt') as csvFile:
        writer = csv.DictWriter(csvFile, fieldnames=headers)
        writer.writeheader()
        for i in range(records):
            full_name = fake.name()
            FLname = full_name.split(" ")
            Fname = FLname[0]
            Lname = FLname[1]
            domain_name = "@testDomain.com"
            userId = Fname +"."+ Lname + domain_name

            writer.writerow({
                    # "Email Id" : userId,
                    "Prefix" : fake.prefix(),
                    "id" : fake.ssn(),
                    "Time": fake.time(),
                    "Timestamp" :fake.past_datetime()
                    #"Location" :fake.location_on_land()

                    })

if __name__ == '__main__':
    records = 129881
    headers = [ "Prefix", "id",
                "Time", "Timestamp"]
    datagenerate(records, headers)

    print("CSV generation complete!")
