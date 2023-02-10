from dbconn import db
import pprint

cursor = db.products.find({"tags":  {"$all": ["63e54024bf10b7a958ae37eb"] }})

for doc in cursor:
    pprint.pprint(doc)


cursor2 = db.products.aggregate( [
   {
      "$lookup":
         {
            from: "tags",
            localField: "tags",
            foreignField: "name",
            as: "tagAssets"
        }
   }
] )