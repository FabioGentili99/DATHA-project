# db_mongo.py

import datetime
from pymongo import MongoClient
from config import MONGO_COLLECTION, MONGO_URI, MONGO_DB
from db_interface import DatabaseInterface
import json

class MongoDBHandler(DatabaseInterface):
    def __init__(self):
        self.client = MongoClient(MONGO_URI)
        self.db = self.client[MONGO_DB]
        self.collection = self.db[MONGO_COLLECTION]



    def write_data(self, log_entry):
        
        # Insert into MongoDB
        self.collection.insert_one(log_entry)



    def close(self):
        """Closes the MongoDB connection."""
        self.client.close()
