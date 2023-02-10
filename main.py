import pymongo

# Replace the uri string with your MongoDB deployment's connection string.
conn_str = "mongodb://localhost/tagzilla?retryWrites=true&w=majority"

# set a 5-second connection timeout
client = pymongo.MongoClient(conn_str, serverSelectionTimeoutMS=5000)
db = client.tagzilla

try:
    print(client.server_info())
except Exception:
    print("Unable to connect to the server.")

# Subdocument key order matters in a few of these examples so we have
# to use bson.son.SON instead of a Python dict.
