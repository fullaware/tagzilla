import pymongo

# Replace the uri string with your MongoDB deployment's connection string.
conn_str = "mongodb://localhost/tagzilla?retryWrites=true&w=majority"

# set a 5-second connection timeout
client = pymongo.MongoClient(conn_str, serverSelectionTimeoutMS=5000)
db = client.tagzilla