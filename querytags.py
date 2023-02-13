from dbconn import db
import pprint
from bson.objectid import ObjectId

"""Find all labels by name *like*
cursor = db.tags.aggregate([
    {
    '$match': {"tagLabel": {"$regex": "jun",'$options': 'i'}}
    }
    ])

for doc in cursor:
    pprint.pprint(doc)
"""

cursor2 = db.products.aggregate([
    {
        '$match': {
            "$and": [
                #{'tag_ids': ObjectId('63e6bbe080bd7b7c45c330db')}, # Cisco
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

"""Returns the following

{'_id': ObjectId('63e54261bf10b7a958ae37f3'),
 'tagAssoc': 'OEM',
 'tagLabel': 'Cisco'}
{'_id': ObjectId('63e54261bf10b7a958ae37f3'),
 'tagAssoc': 'Infrastructure',
 'tagLabel': 'Network'}
{'_id': ObjectId('63e54261bf10b7a958ae37f3'),
 'tagAssoc': 'Infrastructure',
 'tagLabel': 'Router'}
"""