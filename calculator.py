import RPi.GPIO as GPIO
from time import sleep
from sys import stdout

GPIO.setmode (GPIO.BOARD)
GPIO.setwarnings(False)
value = "nothing"

MATRIX = [ [1,2,3,"A"],[4,5,6,"B"],[7,8,9,"C"],['*',0,'#',"D"] ]

ROW = [37,35,33,31]
COL = [29,23,21,12]


for j in range(4):
	GPIO.setup(COL[j],GPIO.OUT)
	GPIO.output(COL[j],1)

for i in range (4):
	GPIO.setup(ROW[i], GPIO.IN, pull_up_down = GPIO.PUD_UP)




def keypad():
	value = "nothing"
	for j in range (4):
		GPIO.output(COL[j],0)

		for i in range(4):
			if GPIO.input (ROW[i]) == 0:
				value = MATRIX[i][j]

		GPIO.output(COL[j],1)

	return value
try:
	while(True):
		pressed = keypad()
		if(pressed is not "nothing"):
			print pressed
except Exception as ex:
	print str(ex)
	GPIO.cleanup()
