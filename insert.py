import pymongo
from bson.son import SON

# Replace the uri string with your MongoDB deployment's connection string.
conn_str = "mongodb://localhost/tagzilla?retryWrites=true&w=majority"

# set a 5-second connection timeout
client = pymongo.MongoClient(conn_str, serverSelectionTimeoutMS=5000)
db = client.tagzilla

"""
db.assets.insert_many(
    [
        {
            "item": "journal",
            "instock": [
                SON([("warehouse", "A"), ("qty", 5)]),
                SON([("warehouse", "C"), ("qty", 15)]),
            ],
        },
        {
            "item": "paper",
            "instock": [
                SON([("warehouse", "A"), ("qty", 60)]),
                SON([("warehouse", "B"), ("qty", 15)]),
            ],
        },
    ]
)
"""
db.tags.insert_many(
    [
                {
            "tagLabel": "Cisco",
            "tagAssoc": "OEM",
        },
                {
            "tagLabel": "Dell",
            "tagAssoc": "OEM",
        },
                {
            "tagLabel": "IBM",
            "tagAssoc": "OEM",
        },
                        {
            "tagLabel": "Juniper",
            "tagAssoc": "OEM",
        },
        {
            "tagLabel": "HPE",
            "tagAssoc": "OEM",
        },
        {
            "tagLabel": "Network",
            "tagAssoc": "Infrastructure",
        },
          {
            "tagLabel": "Server",
            "tagAssoc": "Infrastructure" ,
        },
                  {
            "tagLabel": "Firewall",
            "tagAssoc": "Infrastructure" ,
        },
                  {
            "tagLabel": "Switch",
            "tagAssoc": "Infrastructure" ,
        },
                  {
            "tagLabel": "Router",
            "tagAssoc": "Infrastructure" ,
        },
          {
            "tagLabel": "SAS",
            "tagAssoc": "Subscription",
        },
          {
            "tagLabel": "Perpetual",
            "tagAssoc": "License",
        },
                  {
            "tagLabel": "Term",
            "tagAssoc": "License",
        },
                  {
            "tagLabel": "Software",
            "tagAssoc": "Subscription" ,
        },
                          {
            "tagLabel": "Managed Service",
            "tagAssoc": "Subscription" ,
        },
    ]
)
