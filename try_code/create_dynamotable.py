#code will be written in json style

#source:https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/SQLtoNoSQL.CreateTable.html
{
    TableName : 'flight_id'
    KeySchema :[
        {
            AttributeName : "customer_id",
            KeyType : "HASH", //PartitionKey
        },
        {
            AttributeName : "timestamp",
            KeyType : "RANGE" //sort key
        }

        ],

    AttributeDefinitions: [
        {
            AttributeName : "customer_id",
            AttributeType : "S"

        }
    ]



        }
    ]



}
