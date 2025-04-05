# db_mongo.py

import datetime
from pymongo import MongoClient
from config import MONGO_COLLECTION, MONGO_URI, MONGO_DB
from db_interface import DatabaseInterface

class MongoDBHandler(DatabaseInterface):
    def __init__(self):
        self.client = MongoClient(MONGO_URI)
        self.db = self.client[MONGO_DB]
        self.collection = self.db[MONGO_COLLECTION]

    def write_data(self, data):
        """Inserts Modbus data into MongoDB."""
        #formatted_data = {"timestamp": datetime.utcnow()}
        formatted_data = {}
        for name, details in data.items():
            if name == "Timestamp":
                formatted_data[name] = details
                continue
            formatted_data[name] = {"value": details["value"], "unit": details["unit"]}
        self.collection.insert_one(formatted_data)
        print(f"Data written to MongoDB: {formatted_data}")

    def close(self):
        """Closes the MongoDB connection."""
        self.client.close()
