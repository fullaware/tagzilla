from dbconn import db
import pprint

""" cursor = db.products.find({"tags":  {"$all": ["63e54024bf10b7a958ae37eb"] }})

for doc in cursor:
    pprint.pprint(doc) """


cursor2 = db.products.aggregate( [
   {
        "$unwind":"$tags"
   },{
      "$lookup":
         {
            "from": "tags",
            "localField": "tags",
            "foreignField": "_id",
            "as": "tagAssets"
        }
   },{
    "$project":{"_id":0,"tagAssoc":"$tagAssets.tagAssoc","tagLabel":"$tagAssets.tagLabel"}
   }
] )

for doc2 in cursor2:
    pprint.pprint(doc2)