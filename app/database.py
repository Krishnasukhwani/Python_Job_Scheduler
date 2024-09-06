from pymongo import MongoClient
from bson import ObjectId

# MongoDB connection settings
MONGO_DETAILS = "mongodb+srv://krishnasukhwani64:<db_password>@cluster0.om8gr.mongodb.net/"  # Update this with your MongoDB URI
client = MongoClient(MONGO_DETAILS)
database = client.jobs_db  
jobs_collection = database.jobs  
