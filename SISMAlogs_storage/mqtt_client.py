import paho.mqtt.client as mqtt
from config import MQTT_BROKER, MQTT_PORT, MQTT_TOPIC, CLIENT_ID, MQTT_USERNAME, MQTT_PASSWORD
from log_formatter import format_log
from db_factory import get_db

log_storage = get_db()

def on_connect(client, userdata, flags, rc):
    """Handles connection to MQTT broker."""
    if rc == 0:
        print(f"Connected to MQTT broker as {CLIENT_ID}")
        client.subscribe(MQTT_TOPIC)
    else:
        print(f"Failed to connect, return code {rc}")

def on_message(client, userdata, msg):
    """Processes incoming messages."""
    raw_log = msg.payload.decode('utf-8').strip()

    formatted_log = format_log(raw_log)
    print(formatted_log) 
    log_storage.write_data(formatted_log)
    #with open("data.txt", "a") as file:
        #file.write(formatted_log + "\n")

def start_mqtt_client():
    """Initializes and starts the MQTT client."""
    client = mqtt.Client(client_id=CLIENT_ID)

    # Set username and password
    client.username_pw_set(MQTT_USERNAME, MQTT_PASSWORD)

    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(MQTT_BROKER, MQTT_PORT, 60)
    client.loop_forever()  # Keep listening indefinitely
