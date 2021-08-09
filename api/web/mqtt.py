import paho.mqtt.client as mqtt
import json

from enum import Enum
from .models import Bme280, Ccs811

class Topics(Enum):
    TEMP = "school-monitor/sensor/bme280-temperature/state"
    HUMIDITY = "school-monitor/sensor/bme280-humidity/state"
    PRESSURE = "school-monitor/sensor/bme280-pressure/state"
    CO2 = "school-monitor/sensor/ccs811-co2/state"
    TVOC = "school-monitor/sensor/ccs811-tvoc/state"

MQTT_TOPIC = [(Topics.TEMP, 0), (Topics.HUMIDITY, 0),
    (Topics.PRESSURE, 0), (Topics.CO2, 0),
    (Topics.TVOC, 0)]

def on_connect(client, userdata, flags, rc):
    client.subscribe(MQTT_TOPIC)

def on_message(client, userdata, msg):
    message_dict = json.loads(msg.payload)

    if (message_dict[Topics.TEMP] and message_dict[Topics.HUMIDITY] and message_dict[Topics.PRESSURE] and 
    message_dict[Topics.CO2] and message_dict[Topics.TVOC]):
        Bme280.objects.create(temperature = message_dict[Topics.TEMP], humidity = message_dict[Topics.HUMIDITY], 
        pressure = message_dict[Topics.PRESSURE])
        Ccs811.objects.create(co2 = message_dict[Topics.CO2], tvoc = message_dict[Topics.TVOC])

client = mqtt.Client("django_paho_mqtt_subscriber")
client.on_connect = on_connect
client.on_message = on_message
client.connect("test.mosquitto.org", 1883)

client.loop_forever()