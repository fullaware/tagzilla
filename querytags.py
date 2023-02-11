from dbconn import db
import pprint
from bson.objectid import ObjectId

""" cursor = db.products.find({"tags":  {"$all": ["63e54024bf10b7a958ae37eb"] }})

for doc in cursor:
    pprint.pprint(doc) """


cursor2 = db.products.aggregate( [
  {"$match":{"_id":ObjectId("63e54261bf10b7a958ae37f3")}},
  {
    "$lookup": {
      "from": "tags",
      "localField": "tags",
      "foreignField": "_id",
      "as": "tagAssets",
    },
  },
  {
    "$unwind": "$tagAssets",
  },
  {
    "$project": {
      "_id":0,
      "tagLabel": "$tagAssets.tagLabel",
      "tagAssoc": "$tagAssets.tagAssoc",
    },
  },
] )

for doc2 in cursor2:
    pprint.pprint(doc2)