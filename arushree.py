import paho.mqtt.subscribe as subscribe

#from time import sleep
#i=0
while True:
	msg=subscribe.simple("class", hostname="broker.shiftr.io",auth={"password":"avyas123",
	"username":"arushree"})
	print "message is : " + msg.payload
