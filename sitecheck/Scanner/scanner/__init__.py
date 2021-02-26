"""
    Geo-Instruments
    Sitecheck Scanner
"""
import logging
import os
import paho.mqtt.client as mqtt

logger = logging.getLogger('log')

# Mqtt CLient
client = mqtt.Client(os.environ.get('SCANNER_AMPUSER', 'Scanner'))
hostname = os.environ.get('SCANNER_IP', 'localhost')
port = int(os.environ.get('SCANNER_PORT', 1884))
client.connect(hostname, port)

