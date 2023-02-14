from dbconn import db
import pprint
from bson.objectid import ObjectId

# Delete multiple tags

db.assets.update_many(
    {
        '_id': {
            '$in': [
                ObjectId('63e54261bf10b7a958ae37f3'),
                ObjectId("63eaf6a102bc89078913759b")
            ]
        }
    },
    {"$pull": {
        "tagIds": {
            "$in":
            [ObjectId("63e6bbe080bd7b7c45c330e0"),
             ObjectId("63e6bbe080bd7b7c45c330e4")]}}})

cursor = db.assets.find({'_id': {
    '$in': [
        ObjectId('63e54261bf10b7a958ae37f3'),
        ObjectId("63eaf6a102bc89078913759b")
    ]
}})

for doc in cursor:
    pprint.pprint(doc)
