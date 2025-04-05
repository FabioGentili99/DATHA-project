# config.py

# Modbus TCP Configuration
MODBUS_IP = "192.168.102.16"
MODBUS_PORT = 502
POLL_INTERVAL = 5  # Seconds between reads

# Database Selection
DB_TYPE = "mongodb"  # Change to "mongodb" as needed

# InfluxDB Configuration
INFLUX_URL = "http://localhost:8086"
INFLUX_TOKEN = "*"
INFLUX_ORG = "*"
INFLUX_BUCKET = "pac3220_data"

# MongoDB Configuration
MONGO_URI = "mongodb://localhost:27017/"
MONGO_DB = "pac3220"
MONGO_COLLECTION = "pac3220_data"



# PAC3220 Register Map
REGISTER_MAP = {
    "Voltage_L1-N": {"address": 1, "unit": "V"},
    "Voltage_L2-N": {"address": 3, "unit": "V"},
    "Voltage_L3-N": {"address": 5, "unit": "V"},
    "Voltage_L1-L2": {"address": 7, "unit": "V"},
    "Voltage_L2-L3": {"address": 9, "unit": "V"},
    "Voltage_L3-L1": {"address": 11, "unit": "V"},
    "Current_L1": {"address": 13, "unit": "A"},
    "Current_L2": {"address": 15, "unit": "A"},
    "Current_L3": {"address": 17, "unit": "A"},
    "Apparent_Power_L1": {"address": 19, "unit": "VA"},
    "Apparent_Power_L2": {"address": 21, "unit": "VA"},
    "Apparent_Power_L3": {"address": 23, "unit": "VA"},
    "Active_Power_L1": {"address": 25, "unit": "W"},
    "Active_Power_L2": {"address": 27, "unit": "W"},
    "Active_Power_L3": {"address": 29, "unit": "W"},
    "THD_Voltage_L1": {"address": 43, "unit": "%"},
    "THD_Voltage_L2": {"address": 45, "unit": "%"},
    "THD_Voltage_L3": {"address": 47, "unit": "%"},
    "THD_Current_L1": {"address": 49, "unit": "%"},
    "THD_Current_L2": {"address": 51, "unit": "%"},
    "THD_Current_L3": {"address": 53, "unit": "%"},
    "Frequency": {"address": 55, "unit": "Hz"},
    #"Timestamp": {"address": 799, "unit": ""}

}
