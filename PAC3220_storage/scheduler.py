# scheduler.py

import schedule
import time
from modbus_reader import ModbusReader
from config import DB_TYPE
from db_influx import InfluxDBHandler
from db_mongo import MongoDBHandler

# Select database dynamically
def get_db_handler():
    if DB_TYPE == "influxdb":
        return InfluxDBHandler()
    elif DB_TYPE == "mongodb":
        return MongoDBHandler()
    else:
        raise ValueError(f"Unsupported database type: {DB_TYPE}")

def read_and_store():
    """Reads data from PAC3220 and stores it in the selected database."""
    modbus = ModbusReader()
    #db = get_db_handler()

    data = modbus.read_all()
    if data:
        #db.write_data(data)
        print(data)

    modbus.close()
    #db.close()

# Schedule the function to run every POLL_INTERVAL seconds
schedule.every(5).seconds.do(read_and_store)

def start_scheduler():
    """Starts the scheduled task loop."""
    print(f"Starting data collection every 5 seconds...")
    while True:
        schedule.run_pending()
        time.sleep(1)
