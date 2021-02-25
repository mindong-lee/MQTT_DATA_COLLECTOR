import paho.mqtt.client as mqtt
import random, threading, json
from datetime import datetime

#====================================================
# FAKE SENSOR 
# Dummy code used as Fake Sensor to publish some random values
# to MQTT Broker

def publish_Fake_Sensor_Values_to_MQTT():
	threading.Timer(2.0, publish_Fake_Sensor_Values_to_MQTT).start()
	global toggle

	Waterflow_Fake_Value = float("{0:.2f}".format(random.uniform(0, 30)))

	Waterflow_Data = ""
	Waterflow_Data += "Waterflow/"
	Waterflow_Data += str((datetime.today()).strftime("%Y-%m-%d %H:%M:%S:%f"))+"/"
	Waterflow_Data += str(Waterflow_Fake_Value)

	print ("Publishing fake Waterflow Value: " + str(Waterflow_Fake_Value) + "...")
	publish_To_Topic ("udmt/waterflow", Waterflow_Data)

def publish_To_Topic(m_topic, message):
	mqttc.publish(m_topic,message)
	print ("Published:" + message + " on MQTT Topic: " + m_topic)
	print ("")

#====================================================
# MQTT Settings 
MQTT_Broker = "192.168.0.86"
MQTT_Port = 1883
Keep_Alive_Interval = 45
#====================================================
mqttc = mqtt.Client("md")
mqttc.connect(MQTT_Broker, int(MQTT_Port), int(Keep_Alive_Interval))		
publish_Fake_Sensor_Values_to_MQTT()
#====================================================