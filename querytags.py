from dbconn import db
import pprint
from bson.objectid import ObjectId

# Find all labels by name *like*

def findTagId (tagLabel = "Unicorn"):
   """Find document in tags that match tagLabel
   """
   
   doc = db.tags.find_one({"tagLabel": {"$regex": tagLabel,'$options': 'i'}})

   pprint.pprint(doc["_id"])


def findAssetsMultipleTagIds ():
   """Return all documents that match ALL ObjectIds within $and array
   """
   cursor2 = db.assets.aggregate([
      {
         '$match': {
               "$and": [
                  # Add Objects Here
                  {'tagIds': ObjectId('63e9528ad3f4e89fd26e07f1')} # Unicorn
                  
               ]
         }
      }, {
         '$lookup': {
               'from': 'tags',
               'localField': 'tagIds',
               'foreignField': '_id',
               'as': 'tags'
         }
      },{
         '$project': {'originFields': 0 , 'tagIds': 0}  # Don't show these fields
      }
   ])

   for doc2 in cursor2:
      pprint.pprint(doc2)


# Search by tags.tagLabel 

def findAssetsLabel (tagLabel="rout"):
   """Return all documents that match tags.tagLabel
   """
   cursor3 = db.tags.aggregate(
      [
      {
         '$match': {
               'tagLabel': {
                  '$regex': tagLabel, 
                  '$options': 'i'
               }
         }
      }, {
         '$lookup': {
               'from': 'assets', 
               'localField': '_id', 
               'foreignField': 'tagIds', 
               'as': 'result'
         }
      },{
         '$project': {'result.originFields': 0 , 'result.tagIds': 0}  # Don't show these fields
      }
   ]
   )

   for doc3 in cursor3:
      pprint.pprint(doc3)


# findTagId("rout")

# findAssetsMultipleTagIds()

findAssetsLabel()