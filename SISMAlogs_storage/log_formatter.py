import json
import re

def format_log(raw_message):
    """
    Converts raw log messages into a standardized JSON format.
    """
    # Dictionary to store parsed data
    parsed_data = []

    # Regular expression to extract timestamp, section, and values
    log_pattern = re.compile(r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{3}) - >>\|(.*?)\|<<(.*)")

    # Regular expressions to separate key-value pairs (including unit extraction)
    measurement_pattern_1 = re.compile(r"([\w\s.]+):\s*([\d.]+)([^\d\s]*)")
    measurement_pattern_2 = re.compile(r"([\w\s\.]+):\s*(NaN|[-+]?\d*\.?\d+)\s*([\S]*)")
    measurement_pattern_3 = re.compile(r"([\w\s().]+):\s*([\d.-]+)([^\d\s]*)")
    measurement_pattern_4 = re.compile(r"([\w\s.]+)\s*=\s*([-+]?\d*\.\d+|\d+|NaN)\s*([\S]*)")
    measurement_pattern_5 = re.compile(r"(O2\[\d\])\s*=\s*([\d.-]+)\s*([^\d\s]*)")
    measurement_pattern_6 = re.compile(r"([\w\s\[\].]+)[:=]\s*([\d.-]+|NaN)\s*([^\d\s]*)")
    measurement_pattern_7 = re.compile(r"([\w\s\/.]+)[:=]\s*([\d.-]+|No|Yes)\s*([^\d\s]*)")
    measurement_pattern_8 = re.compile(r"([\w\s\/.]+)[:=]\s*([\d.-]+)\s*([^\d\s]*)")
    measurement_pattern_9 = re.compile(r"([\w\s\/.]+)[:=]\s*([\d.-]+)\s*([^\d\s]*)")
    measurement_pattern_10 = re.compile(r"([\w\s\/.]+)[:=]\s*([\d.-]+)\s*([^\d\s]*)")
    measurement_pattern_11 = re.compile(r"([\w\s\/.]+)[:=]\s*([\d.-]+)\s*([^\d\s]*)")
    measurement_pattern_12 = re.compile(r"([\w\s\/.]+)\s*[:=]\s*([\D]+|[\d.-]+)\s*([^\d\s]*)")
    measurement_pattern_13 = re.compile(r"([\w\s\/%<]+)\s*[:=]\s*([\D]+|[\d.-]+)\s*([^\d\s]*)")
    measurement_pattern_14 = re.compile(r"([\w\s\/%<\(\)-]+)\s*[:=]\s*([\d.-]+)\s*([^\d\s]*)")
    measurement_patterns = [
        measurement_pattern_1, measurement_pattern_2, measurement_pattern_3,
        measurement_pattern_4, measurement_pattern_5, measurement_pattern_6,
        measurement_pattern_7, measurement_pattern_8, measurement_pattern_9,
        measurement_pattern_10, measurement_pattern_11, measurement_pattern_12,
        measurement_pattern_13, measurement_pattern_14
    ]


    ts = None
    # Parse each line
    lines = raw_message.split("\n")
    #print (lines)
    for i in range(len(lines)):
        match = log_pattern.search(lines[i])
        if match:
            timestamp, section, values = match.groups()
            values = values.strip()
            x = None
            match section:
                case "IODIAG_ENV":
                    x = 0;
                case "IODIAG_SENSORS":
                    x = 1;
                case "IODIAG_AIR":
                    x = 2;
                case "IODIAG_GAS":
                    x = 3;
                case "IODIAG_O2MANAGER":
                    x = 4;
                case "IODIAG_FILTER":
                    x = 5;
                case "IODIAG_PREHEATING":
                    x = 6;
                case "MOTORDIAG_WORK_CHAMBER":
                    x = 7;
                case "MOTORDIAG_SUPPLY1_CHAMBER":
                    x = 8;
                case "MOTORDIAG_SUPPLY2_CHAMBER":
                    x = 9;
                case "MOTORDIAG_COATER":
                    x = 10;
                case "MEM_USAGE":
                    x = 11;
                case "IODIAG_OVERFLOWBIN":
                    x = 12;
                case "IODIAG_LASER":
                    x = 13;
            
            # Extract measurements
            measurements = []
            for item in re.split(r' - ', values):
                print(item + "\n")
                item = item.strip()

                measurement_match = measurement_patterns[x].search(item)
                print(measurement_match)

                if measurement_match:
                    key, value, unit = measurement_match.groups()
                    parsed_value = float(value) if value.replace('.', '', 1).replace('-', '', 1).isdigit() else value  # Convert to float if numeric
                    measurements.append({
                        "parameter": key.strip(),
                        "value": parsed_value,
                        "unit": unit.strip() if unit else None
                    })

            # Format as structured JSON
            data = {
                #"timestamp": timestamp,
                "section": section,
                "measurements": measurements
            }

            # Convert to JSON format
            json_output = json.dumps(data)
            #print(json_output)
            parsed_data.append(json_output)
            ts = timestamp
    json_data = {
        "timestamp":  ts,
        "data": parsed_data
    }
    return json.dumps(json_data, indent=4)
