import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

## @params: [TempDir, JOB_NAME]
args = getResolvedOptions(sys.argv, ['TempDir','JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)
## @type: DataSource
## @args: [database = "gue-transactionsdb", table_name = "aws_bulkimport_sy", transformation_ctx = "datasource0"]
## @return: datasource0
## @inputs: []
datasource0 = glueContext.create_dynamic_frame.from_catalog(database = "gue-transactionsdb", table_name = "aws_bulkimport_sy", transformation_ctx = "datasource0")
## @type: ApplyMapping
## @args: [mapping = [("customerid", "string", "customerid", "string"), ("review_id", "long", "review_id", "string"), ("flight_id", "string", "flight_id", "string"), ("names", "string", "names", "string"), ("gender", "string", "gender", "string"), ("customer_type", "string", "customer_type", "string"), ("age", "long", "age", "int"), ("type_of_travel", "string", "type_of_travel", "string"), ("class", "string", "class", "string"), ("flight_distance", "long", "flight_distance", "int"), ("seat_comfort", "long", "seat_comfort", "int"), ("deptarrive_time_convenient", "long", "deptarrive_time_convenient", "int"), ("food_drink", "long", "food_drink", "int"), ("gate_location", "long", "gate_location", "int"), ("inflight_wifi", "long", "inflight_wifi", "int"), ("inflight_entertainment", "long", "inflight_entertainment", "int"), ("online_support", "long", "online_support", "int"), ("ease_online_booking", "long", "ease_online_booking", "int"), ("onboard_service", "long", "onboard_service", "int"), ("legroom_service", "long", "legroom_service", "int"), ("baggage_handling", "long", "baggage_handling", "int"), ("checkin_service", "long", "checkin_service", "int"), ("cleanliness", "long", "cleanliness", "int"), ("online_boarding", "long", "online_boarding", "int"), ("dept_delay_min", "long", "dept_delay_min", "int"), ("arrival_delay_min", "long", "arrival_delay_min", "int"), ("timestamp", "string", "timestamp", "string"), ("destination", "string", "destination", "string")], transformation_ctx = "applymapping1"]
## @return: applymapping1
## @inputs: [frame = datasource0]
applymapping1 = ApplyMapping.apply(frame = datasource0, mappings = [("customerid", "string", "customerid", "string"), ("review_id", "long", "review_id", "string"), ("flight_id", "string", "flight_id", "string"), ("names", "string", "names", "string"), ("gender", "string", "gender", "string"), ("customer_type", "string", "customer_type", "string"), ("age", "long", "age", "int"), ("type_of_travel", "string", "type_of_travel", "string"), ("class", "string", "class", "string"), ("flight_distance", "long", "flight_distance", "int"), ("seat_comfort", "long", "seat_comfort", "int"), ("deptarrive_time_convenient", "long", "deptarrive_time_convenient", "int"), ("food_drink", "long", "food_drink", "int"), ("gate_location", "long", "gate_location", "int"), ("inflight_wifi", "long", "inflight_wifi", "int"), ("inflight_entertainment", "long", "inflight_entertainment", "int"), ("online_support", "long", "online_support", "int"), ("ease_online_booking", "long", "ease_online_booking", "int"), ("onboard_service", "long", "onboard_service", "int"), ("legroom_service", "long", "legroom_service", "int"), ("baggage_handling", "long", "baggage_handling", "int"), ("checkin_service", "long", "checkin_service", "int"), ("cleanliness", "long", "cleanliness", "int"), ("online_boarding", "long", "online_boarding", "int"), ("dept_delay_min", "long", "dept_delay_min", "int"), ("arrival_delay_min", "long", "arrival_delay_min", "int"), ("timestamp", "string", "timestamp", "string"), ("destination", "string", "destination", "string")], transformation_ctx = "applymapping1")
## @type: SelectFields
## @args: [paths = ["customer_type", "review_id", "seat_comfort", "legroom_service", "gender", "destination", "online_boarding", "onboard_service", "class", "flight_distance", "timestamp", "dept_delay_min", "deptarrive_time_convenient", "food_drink", "online_support", "type_of_travel", "ease_online_booking", "checkin_service", "flight_id", "cleanliness", "arrival_delay_min", "names", "customerid", "inflight_entertainment", "inflight_wifi", "baggage_handling", "age", "gate_location"], transformation_ctx = "selectfields2"]
## @return: selectfields2
## @inputs: [frame = applymapping1]
selectfields2 = SelectFields.apply(frame = applymapping1, paths = ["customer_type", "review_id", "seat_comfort", "legroom_service", "gender", "destination", "online_boarding", "onboard_service", "class", "flight_distance", "timestamp", "dept_delay_min", "deptarrive_time_convenient", "food_drink", "online_support", "type_of_travel", "ease_online_booking", "checkin_service", "flight_id", "cleanliness", "arrival_delay_min", "names", "customerid", "inflight_entertainment", "inflight_wifi", "baggage_handling", "age", "gate_location"], transformation_ctx = "selectfields2")
## @type: ResolveChoice
## @args: [choice = "MATCH_CATALOG", database = "gue-transactionsdb", table_name = "dev_public_bulkimport", transformation_ctx = "resolvechoice3"]
## @return: resolvechoice3
## @inputs: [frame = selectfields2]
resolvechoice3 = ResolveChoice.apply(frame = selectfields2, choice = "MATCH_CATALOG", database = "gue-transactionsdb", table_name = "dev_public_bulkimport", transformation_ctx = "resolvechoice3")
## @type: ResolveChoice
## @args: [choice = "make_cols", transformation_ctx = "resolvechoice4"]
## @return: resolvechoice4
## @inputs: [frame = resolvechoice3]
resolvechoice4 = ResolveChoice.apply(frame = resolvechoice3, choice = "make_cols", transformation_ctx = "resolvechoice4")
## @type: DataSink
## @args: [database = "gue-transactionsdb", table_name = "dev_public_bulkimport", redshift_tmp_dir = TempDir, transformation_ctx = "datasink5"]
## @return: datasink5
## @inputs: [frame = resolvechoice4]
datasink5 = glueContext.write_dynamic_frame.from_catalog(frame = resolvechoice4, database = "gue-transactionsdb", table_name = "dev_public_bulkimport", redshift_tmp_dir = args["TempDir"], transformation_ctx = "datasink5")
job.commit()
