import os
import socket
import requests
import subprocess
import xml.etree.ElementTree as ET
from influxdb import InfluxDBClient
from datetime import datetime, timezone

# Metrics
sp = subprocess.Popen(['nvidia-smi', 'dmon', '-s', 'u', '-c', '1'], stdout=subprocess.PIPE)
output = sp.communicate()[0]
metrics = [int(char) for char in str(output) if char.isdigit()]

# Transcodes
sp = subprocess.Popen(['nvidia-smi', '-q', '-x'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output = sp.communicate()[0]
xmltree = ET.fromstring(output)
gpu_processes = xmltree.findall('./gpu/processes/process_info')

connection_count = len(requests.get('http://192.168.1.28:32400/connections?X-Plex-Token=xt4phVyiJphn6yQkXA3S').text.split('\n'))

influx_payload = [
    {
        "measurement": "Plex Info",
        "tags": {
            "host": socket.gethostname()
        },
        "time": datetime.now(timezone.utc).astimezone().isoformat(),
        "fields": {
            "HW Transcodes": len(gpu_processes),
            "GPU Overall Util": int(metrics[0]),
            "GPU SM Util": int(metrics[1]),
            "GPU Memory Util": int(metrics[2]),
            "GPU Encoder Util": int(metrics[3]),
            "GPU Decoder Util": int(metrics[4]),
            "Connection Count": connection_count
        }
    }
]

influx = InfluxDBClient('192.168.1.28', 8086, '', '', 'manual_stats')
influx.write_points(influx_payload)



#What to input in crontab -e
#* * * * * /usr/bin/python3 /home/devin/nvidia.py
