import paho.mqtt.client as mqtt
from config import MQTT_BROKER, MQTT_PORT, MQTT_TOPIC, CLIENT_ID, MQTT_USERNAME, MQTT_PASSWORD
from db_factory import get_db
import json

image_storage = get_db()

def on_connect(client, userdata, flags, rc):
    """Handles connection to MQTT broker."""
    if rc == 0:
        print(f"Connected to MQTT broker as {CLIENT_ID}")
        client.subscribe(MQTT_TOPIC)
    else:
        print(f"Failed to connect, return code {rc}")




def on_message(client, userdata, msg):
    """Callback when a message is received"""
    try:
        # Parse MQTT message
        log_entry = json.loads(msg.payload.decode("utf-8"))
       
        # Store in MongoDB
        image_storage.store_log(log_entry)

        print(f"Stored log from topic {msg.topic}: {log_entry['jobId']}")
    
    except json.JSONDecodeError:
        print(f"Received non-JSON message on {msg.topic}: {msg.payload.decode('utf-8')}")
    except Exception as e:
        print(f"Error processing message: {e}")




def start_mqtt_client():
    """Initializes and starts the MQTT client."""
    client = mqtt.Client(client_id=CLIENT_ID)

    # Set username and password
    #client.username_pw_set(MQTT_USERNAME, MQTT_PASSWORD)

    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(MQTT_BROKER, MQTT_PORT, 60)
    client.loop_forever()  # Keep listening indefinitely
