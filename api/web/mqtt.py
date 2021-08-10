import json

import paho.mqtt.client as mqtt

TEMP = "school-monitor/sensor/bme280-temperature/state"
HUMIDITY = "school-monitor/sensor/bme280-humidity/state"
PRESSURE = "school-monitor/sensor/bme280-pressure/state"
CO2 = "school-monitor/sensor/ccs811-co2/state"
TVOC = "school-monitor/sensor/ccs811-tvoc/state"

MQTT_TOPIC = [(TEMP, 0), (HUMIDITY, 0),
              (PRESSURE, 0), (CO2, 0),
              (TVOC, 0)]


def on_connect(client, userdata, flags, rc):
    client.subscribe(MQTT_TOPIC)


def on_message(client, userdata, msg):
    message_dict = json.loads(msg.payload)
    from .models import Temperature, Humidity, Pressure, Tvoc, Co2
    if msg.topic == TEMP:
        Temperature(value=message_dict, topic=msg.topic).save()
    elif msg.topic == HUMIDITY:
        Humidity(value=message_dict, topic=msg.topic).save()
    elif msg.topic == PRESSURE:
        Pressure(value=message_dict, topic=msg.topic).save()
    elif msg.topic == CO2:
        Co2(value=message_dict, topic=msg.topic).save()
    elif msg.topic == TVOC:
        Tvoc(value=message_dict, topic=msg.topic).save()


client = mqtt.Client("django_paho_mqtt_subscriber")
client.on_connect = on_connect
client.on_message = on_message
client.connect("test.mosquitto.org", 1883)
