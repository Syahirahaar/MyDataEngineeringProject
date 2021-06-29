import json
import jsonschema
from jsonschema import validate

custSchema = {
    "type" : "object",
    "properties" : {
        "CustomerID" : {"type" : "string"},
        "timestamp" : {"type" : "string"},
        "flight_id" :{"type":"string"},
        "customer" : {"Names" : {"type":"string"},"Age" : {"type":"String"},"customer_type" : {"type": "string"},"type_of_travel":{"type": "string"},"class":{"type":"string"}},
        "review" : {"seat_comfort":{"type":"string"},
                    "deptarrive_time_convenient" :{"type":"string"},
                    "food_drink":{"type":"string"},
                    "gate_location":{"type":"string"},
                    "inflight_wifi":{"type":"string"},
                    "inflight_entertainment":{"type":"string"},
                    "online_support":{"type":"string"},
                    "ease_online_booking":{"type":"string"},
                    "onboard_service" : {"type":"string"},
                    "legroom_service":{"type":"string"},
                    "baggage_handling" : {"type":"string"},
                    "checkin_service":{"type":"string"},
                    "cleanliness" : {"type":"string"},
                    "online_boarding":{"type":"string"},
                    "destination" : {"type":"string"}},
        "flight" : {"flight_distance":{"type":"number"},
                    "dept_delay_min" :{"type":"number"},
                    "arrival_delat_min":{"type":"number"}}
    }
}


# # Describe what kind of json you expect.
# studentSchema = {
#     "type": "object",
#     "properties": {
#         "name": {"type": "string"},
#         "rollnumber": {"type": "number"},
#         "marks": {"type": "number"},
#         "customer" : {"Names" : {"type":"string"},"Age" : {"type":"String"},"customer_type" : {"type": "string"},"type_of_travel":{"type": "string"},"class":{"type":"string"}}
#     },
# }

def validateJson(jsonData):
    try:
        validate(instance=jsonData, schema=custSchema)
    except jsonschema.exceptions.ValidationError as err:
        return False
    return True

# Convert json to python object.
jsonData = json.loads('{"name": "jane doe", "rollnumber": 25, "marks": 72, "customer" : {"Names" :"Alfonso","Age" : "34","customer_type":"loyal cust","type_of_travel":"Work","class":"Business"}}')
# validate it
isValid = validateJson(jsonData)
if isValid:
    print(jsonData)
    print("Given JSON data is Valid")
else:
    print(jsonData)
    print("Given JSON data is InValid")

# # Convert json to python object.
# jsonData = json.loads('{"name": "jane doe", "rollnumber": 25, "marks": 72, "customer" : {"Names" :"Alfonso","Age" : "34","customer_type":"loyal cust","type_of_travel":"Work","class":"Business"}}')
# # validate it
# isValid = validateJson(jsonData)
# if isValid:
#     print(jsonData)
#     print("Given JSON data is Valid")
# else:
#     print(jsonData)
#     print("Given JSON data is InValid")
