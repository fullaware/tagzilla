import pymongo
import urllib.parse
from dotenv import dotenv_values

"""
Create .env file and set the following variables

DB_SERVER="LOCALHOST"
DB_USER="admin"
DB_PW="password123"
"""

config = dotenv_values(".env")

db_server = config['DB_SERVER']
db_username = config['DB_USER']
db_password = urllib.parse.quote_plus(config['DB_PW']) # Fix for passwords with non-alphanumeric symbols

# Replace the uri string with your MongoDB deployment's connection string.
# conn_str = "mongodb://localhost/tagzilla?retryWrites=true&w=majority"
conn_str = f"mongodb+srv://{db_username}:{db_password}@{db_server}/test"

# set a 5-second connection timeout
client = pymongo.MongoClient(conn_str, serverSelectionTimeoutMS=5000)
db = client.tagzilla