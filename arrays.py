from dbconn import db
import pprint
from bson.objectid import ObjectId


db.products.update_one(
    {"_id": ObjectId("63e54261bf10b7a958ae37f3")},
    {"$push": {"tags": {"$each": [ObjectId("63e6bbe080bd7b7c45c330e0"), ObjectId(
        "63e6bbe080bd7b7c45c330db"), ObjectId("63e6bbe080bd7b7c45c330e4")]}}}
)

cursor = db.products.find({"_id": ObjectId("63e54261bf10b7a958ae37f3")})

for doc in cursor:
    pprint.pprint(doc)
