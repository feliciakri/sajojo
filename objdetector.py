import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

TRIG = 23
ECHO = 24
LED = 7
FULLROUND = 512 # 512 step di motor = 1 lingkaran penuh
#rotate(fullround) # kalo mau rotate 1 lingkaran penuhs


ControlPin = [14, 17, 27, 22] #change as needed
DETECTED = False
# stepper rotation pattern
SEQ = [ [1,0,0,0],
			[1,1,0,0],
			[0,1,0,0],
			[0,1,1,0],
			[0,0,1,0],
			[0,0,1,1],
			[0,0,0,1],
			[1,0,0,1] ]

print("Distance Measurement In Progress")

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
GPIO.setup(LED, GPIO.OUT)
for pin in ControlPin:
	GPIO.setup(pin,GPIO.OUT)
	GPIO.output(pin,0)

def distance():
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    pulse_start = 0
    pulse_end = 0
    
    while GPIO.input(ECHO) == 0:
        pulse_start = time.time()

    while GPIO.input(ECHO) == 1:
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start

    distance = pulse_duration * 17150

    distance = round(distance, 2)

    return distance

def turnon():
    GPIO.output(LED, 1)
    time.sleep(1)
def turnoff():
    GPIO.output(LED, 0)

def rotate(round, backward = False):
    if backward:
        for i in range(round): 
		for halfstep in range (8):
			for pin in range (4):
				GPIO.output(ControlPin[pin], SEQ[halfstep][pin])
			time.sleep(0.001)
    else:
        for i in range(round): 
		for halfstep in range (7, -1, -1):
			for pin in range (3, -1, -1):
				GPIO.output(ControlPin[pin], SEQ[halfstep][pin])
			time.sleep(0.001)
        


if __name__ == '__main__':
    try:
        while True:
            dist = distance()
            print ("Measured distance = %.1f cm" % dist)
	    if dist < 30 and DETECTED == False:
                DETECTED = True
		rotate(FULLROUND / 3)
		time.sleep(3)
	    elif dist > 30 and DETECTED == True:
		rotate(FULLROUND / 3, True)
		DETECTED = False
		time.sleep(2)
            time.sleep(1)
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()
