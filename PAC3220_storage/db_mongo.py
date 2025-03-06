# db_mongo.py

import datetime
from pymongo import MongoClient
from config import MONGO_URI, MONGO_DB
from db_interface import DatabaseInterface

class MongoDBHandler(DatabaseInterface):
    def __init__(self):
        self.client = MongoClient(MONGO_URI)
        self.db = self.client[MONGO_DB]
        self.collection = self.db["pac3220_data"]

    def write_data(self, data):
        """Inserts Modbus data into MongoDB."""
        formatted_data = {"timestamp": datetime.utcnow()}
        for name, details in data.items():
            formatted_data[name] = {"value": details["value"], "unit": details["unit"]}
        self.collection.insert_one(formatted_data)
        print(f"Data written to MongoDB: {formatted_data}")

    def close(self):
        """Closes the MongoDB connection."""
        self.client.close()
