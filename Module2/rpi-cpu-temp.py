import paho.mqtt.client as mqtt

f = open("/sys/class/thermal/thermal_zone0/temp", "r")
temp = int(f.readline())/1000
print(temp)

client = mqtt.Client()
client.connect("mqtt.eclipseprojects.io", 1883, 60)
client.publish("cpu/temp", temp)
client.disconnect()