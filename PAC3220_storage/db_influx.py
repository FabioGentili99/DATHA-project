# db_influx.py

from influxdb_client import InfluxDBClient, Point, WritePrecision
from config import INFLUX_URL, INFLUX_TOKEN, INFLUX_ORG, INFLUX_BUCKET
from db_interface import DatabaseInterface

class InfluxDBHandler(DatabaseInterface):
    def __init__(self):
        self.client = InfluxDBClient(url=INFLUX_URL, token=INFLUX_TOKEN, org=INFLUX_ORG)
        self.write_api = self.client.write_api(write_options=WritePrecision.NS)

    def write_data(self, data):
        """Writes Modbus data to InfluxDB."""
        point = Point("PAC3220")
        for name, details in data.items():
            point.field(name, details["value"]).tag("unit", details["unit"])
        self.write_api.write(bucket=INFLUX_BUCKET, org=INFLUX_ORG, record=point)
        print(f"Data written to InfluxDB: {data}")

    def close(self):
        """Closes the InfluxDB connection."""
        self.client.close()
