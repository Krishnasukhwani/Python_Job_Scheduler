from pymongo import MongoClient
from bson import ObjectId

# MongoDB connection settings
MONGO_DETAILS = "mongodb://localhost:27017"  # Update this with your MongoDB URI
client = MongoClient(MONGO_DETAILS)
database = client.jobs_db  
jobs_collection = database.jobs  