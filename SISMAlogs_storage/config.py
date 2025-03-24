import uuid

# MQTT Broker Configuration
MQTT_BROKER = "192.168.102.22" 
MQTT_PORT = 9883
MQTT_TOPIC = "sisma_lines"
MQTT_USERNAME = "sisma"
MQTT_PASSWORD = "password"


# Generate a unique client ID
CLIENT_ID = f"fabio.gentili-{uuid.uuid4()}"

# MongoDB Configuration
MONGO_URI = "mongodb://localhost:27017/"
MONGO_DB = "sisma"
MONGO_COLLECTION = "sisma_logs"


DB_TYPE = "mongo"