import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
#GPIO.setup(8, GPIO.OUT)

i=0

while True:
    input_state = GPIO.input(7)
    if input_state == True:
	#GPIO.output(8, True)
	print("yey", i)
	time.sleep(0.1)
	i+=1
    else:
	print("xxxxxxxx")
	time.sleep(0.000000011)
	#GPIO.output(8, False)


















































































































































































































