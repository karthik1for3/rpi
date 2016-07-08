import RPi.GPIO as GPIO 
import time 

GPIO.setmode(GPIO.BCM) ## Use board pin numbering
GPIO.setup(2, GPIO.OUT) 
GPIO.setup(3, GPIO.OUT) 
GPIO.setup(4, GPIO.OUT)
GPIO.output(2,True)## Switch on pin 7
GPIO.output(3,False)

GPIO.setup(27, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
GPIO.output(27,True)## Switch on pin 7
GPIO.output(22,False)


GPIO.output(17,True)
GPIO.output(4,True)

speed = 0.5
with open("sample.txt", "r") as f:
	lines = f.readlines()
	for line in lines:
		for l in list(line):
			print l, ord(l)
			if ord(l) % 2 == 0:
				GPIO.output(4,True)## Switch on pin 7
				GPIO.output(17,False)
				time.sleep(speed)## Wait
			else:
				GPIO.output(4,False)## Switch off pin 7
                		GPIO.output(17,True)
				time.sleep(speed)## Wait

GPIO.output(4,False)
GPIO.cleanup()
