import RPi.GPIO as GPIO
# from RPiSim import GPIO
import time


def rotate(round):
	seq = [ [1,0,0,0],
			[1,1,0,0],
			[0,1,0,0],
			[0,1,1,0],
			[0,0,1,0],
			[0,0,1,1],
			[0,0,0,1],
			[1,0,0,1] ]
	for i in range(round): 
		for halfstep in range (8):
			for pin in range (4):
				GPIO.output(ControlPin[pin], seq[halfstep][pin])
			time.sleep(0.001)


# GPIO SETUP
GPIO.setmode(GPIO.BCM)
ControlPin = [14, 17, 27, 22] #change as needed
for pin in ControlPin:
	GPIO.setup(pin,GPIO.OUT)
	GPIO.output(pin,0)

# ROTATE EXAMPLE
fullround = 512 # 512 step di motor = 1 lingkaran penuh
#rotate(fullround) # kalo mau rotate 1 lingkaran penuh
rotate(fullround/2) # kalo mau rotate 1/2 lingkaran

GPIO.cleanup()
