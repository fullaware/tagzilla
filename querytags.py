from dbconn import db
import pprint
from bson.objectid import ObjectId

"""Find all labels by name *like*
"""
cursor = db.tags.aggregate([
    {
    '$match': {"tagAssoc": {"$regex": "oem",'$options': 'i'}}
    }
    ])

for doc in cursor:
    pprint.pprint(doc)


cursor2 = db.assets.aggregate([
    {
        '$match': {
            "$and": [
                {'tag_ids': ObjectId('63e6bbe080bd7b7c45c330db')}, # Cisco
                #{'tag_ids': ObjectId('63e6bbe080bd7b7c45c330de')}, # Juniper
                {'tag_ids': ObjectId('63e9528ad3f4e89fd26e07f1')} # Unicorn
                
            ]
        }
    }, {
        '$lookup': {
            'from': 'tags',
            'localField': 'tag_ids',
            'foreignField': '_id',
            'as': 'tagAssets'
        }
    }
])

for doc2 in cursor2:
    pprint.pprint(doc2)


# Search by tagLabel 
tagLabel = "cis"
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
            'foreignField': 'tag_ids', 
            'as': 'result'
        }
    }
]
)

for doc3 in cursor3:
    pprint.pprint(doc3)