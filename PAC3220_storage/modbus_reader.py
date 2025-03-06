# modbus_reader.py

from pymodbus.client import ModbusTcpClient
import struct
from config import MODBUS_IP, MODBUS_PORT, REGISTER_MAP

class ModbusReader:
    def __init__(self):
        self.client = ModbusTcpClient(MODBUS_IP, port=MODBUS_PORT)
        self.client.connect()

    def read_float32(self, address):
        """Reads a 32-bit floating point number from Modbus (2 registers)."""
        response = self.client.read_holding_registers(address, count=2)
        if response.isError():
            print(f"Error reading address {address}")
            return None
        raw = response.registers
        return struct.unpack(">f", struct.pack(">HH", raw[0], raw[1]))[0]

    def read_all(self):
        """Reads all defined registers from PAC3220."""
        data = {}
        for name, reg in REGISTER_MAP.items():
            value = self.read_float32(reg["address"])
            if value is not None:
                data[name] = {"value": value, "unit": reg["unit"]}
        return data

    def close(self):
        """Closes the Modbus connection."""
        self.client.close()
