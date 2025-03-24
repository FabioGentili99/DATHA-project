import uuid

# MQTT Broker Configuration
MQTT_BROKER = "192.168.42.103" 
MQTT_PORT = 1883
MQTT_TOPIC = "data/printer/s1/images/+"



# Generate a unique client ID
CLIENT_ID = f"fabio.gentili-{uuid.uuid4()}"

# MongoDB Configuration
MONGO_URI = "mongodb://localhost:27017/"
MONGO_DB = "sisma"
MONGO_COLLECTION = "sisma_images"


DB_TYPE = "mongo"

"""
data_dict = {
                "printerId": "s1",  # Printer Identifier
                "jobId": job_id,  # Job Identifier
                "jobName": job_name,  # Job name
                "sliceId": actual_layer,  # Slice Identifier
                "imgName": image_name_concat,  # File name of the image
                "imgType": image_type,  # Image Type (nakedTop, dxf, coated, ...
                "imgTimestamp": f"{recent_ts}",
                "imgData": image_content_base64
            }"
"""