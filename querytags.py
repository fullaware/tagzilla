from dbconn import db
import pprint
from bson.objectid import ObjectId

# Find all labels by name *like*


def findTagId(tagLabel="Unicorn"):
    """Find document in tags that match tagLabel
    """

    doc = db.tags.find_one({"tagLabel": {"$regex": tagLabel, '$options': 'i'}})

    pprint.pprint(doc["_id"])


def findAssetsMultipleTagIds():
    """Return all documents that match ALL ObjectIds within $all array
    """
    cursor2 = db.assets.aggregate([
        {
            '$match': {
                'tagIds': {
                    '$all': [
                        ObjectId('63e6bbe080bd7b7c45c330e4')
                    ]
                }
            }
        }, {
            '$lookup': {
                'from': 'tags',
                'localField': 'tagIds',
                'foreignField': '_id',
                'as': 'tags'
            }
        }, {
            # Don't show these fields
            '$project': {'originFields': 0, 'tagIds': 0}
        }
    ])

    for doc2 in cursor2:
        pprint.pprint(doc2)


# Search by tags.tagLabel

def findAssetsLabel(tagLabel="rout"):
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
            }, {
                # Don't show these fields
                '$project': {'result.originFields': 0, 'result.tagIds': 0}
            }
        ]
    )

    for doc3 in cursor3:
        pprint.pprint(doc3)


# findTagId("rout")
findAssetsMultipleTagIds()

# findAssetsLabel()
