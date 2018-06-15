import paho.mqtt.publish as publish
from time import sleep
i=0
while True:
	sleep(1)
	i=i+1
	publish.single(topic="class_data",
	payload="current counter is:"+str(1),
	hostname="broker.shiftr.io",
	auth={"username":"Divyam007","password":"divyamprem9001501111"})
