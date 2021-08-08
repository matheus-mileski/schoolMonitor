import enum
import paho.mqtt.client as mqtt
import json

from enum import Enum
from web.models import Bme280, Ccs811

class Topics(Enum):
    TEMP = "school-monitor/sensor/bme280-temperature/state"
    HUMIDITY = "school-monitor/sensor/bme280-humidity/state"
    PRESSURE = "school-monitor/sensor/bme280-pressure/state"
    CO2 = "school-monitor/sensor/ccs811-co2/state"
    TVOC = "school-monitor/sensor/ccs811-tvoc/state"

MQTT_TOPIC = [(Topics.TEMP, 0), (Topics.HUMIDITY, 0),
    (Topics.PRESSURE, 0), (Topics.CO2, 0),
    (Topics.TVOC, 0)]

def on_connect(client, userdata, flags, rc):  # The callback for when the client connects to the broker
    print("Connected with result code {0}".format(str(rc)))  # Print result of connection attempt
    client.subscribe(MQTT_TOPIC)  # Subscribe to the topics on MQTT_TOPIC

def on_message(client, userdata, msg):  # The callback for when a PUBLISH message is received from the server.
    message_dict = json.loads(msg.payload)

    if (message_dict[Topics.TEMP] and message_dict[Topics.HUMIDITY] and 
    message_dict[Topics.PRESSURE] and message_dict[Topics.CO2] and 
    message_dict[Topics.TVOC]):
        print("Message received-> " + msg.topic + " " + str(msg.payload))  # Print a received msg
        Bme280.objects.create(temperature = message_dict[Topics.TEMP], humidity = message_dict[Topics.HUMIDITY], 
        pressure = message_dict[Topics.PRESSURE])
        Ccs811.objects.create(co2 = message_dict[Topics.CO2], tvoc = message_dict[Topics.TVOC])


client = mqtt.Client("paho_mqtt_test")  # Create instance of client with client ID “digi_mqtt_test”
client.on_connect = on_connect  # Define callback function for successful connection
client.on_message = on_message  # Define callback function for receipt of a message
client.connect("test.mosquitto.org", 1883)  # Connect to (broker, port, keepalive-time)