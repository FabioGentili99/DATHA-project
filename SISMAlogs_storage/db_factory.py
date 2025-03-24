from db_mongo import MongoDBHandler
from config import DB_TYPE

def get_db():
    if DB_TYPE == "mongo":
        return MongoDBHandler()
    else:
        raise ValueError(f"Unsupported database type: {DB_TYPE}")
    
