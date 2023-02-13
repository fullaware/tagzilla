from dbconn import db
import pprint
from bson.objectid import ObjectId

""" cursor = db.products.find({"tags":  ObjectId("63e54024bf10b7a958ae37eb") }})

for doc in cursor:
    pprint.pprint(doc) """


cursor2 = db.products.aggregate([
    {
        '$match': {
            "$and": [
                {'tag_ids': ObjectId('63e6bbe080bd7b7c45c330db')}
            ]
        }
    }, {
        '$lookup': {
            'from': 'tags',
            'localField': 'tag_ids',
            'foreignField': '_id',
            'as': 'tagAssets'
        }
    }, {
        '$unwind': {
            'path': '$tagAssets'
        }
    }, {
        '$project': {
            'tagAssoc': '$tagAssets.tagAssoc',
            'tagLabel': '$tagAssets.tagLabel'
        }
    }
])

for doc2 in cursor2:
    pprint.pprint(doc2)
