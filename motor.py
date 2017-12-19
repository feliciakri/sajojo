import RPi.GPIO as GPIO
# from RPiSim import GPIO
import time


def rotate(round):
	for i in range(round): 
		for halfstep in range (8):
			for pin in range (4):
				GPIO.output(ControlPin[pin], seq[halfstep][pin])
			time.sleep(0.001)

fullround = 512

GPIO.setmode(GPIO.BCM)

ControlPin = [7,11,13,15] #change as needed

for pin in ControlPin:
	GPIO.setup(pin,GPIO.OUT)
	GPIO.output(pin,0)

seq = [ [1,0,0,0],
		[1,1,0,0],
		[0,1,0,0],
		[0,1,1,0],
		[0,0,1,0],
		[0,0,1,1],
		[0,0,0,1],
		[1,0,0,1] ]

rotate(fullround) # kalo mau rotate 1 lingkaran penuh
rotate(fullround/2) # kalo mau rotate 1/2 lingkaran

GPIO.cleanup()
