import RPi.GPIO as GPIO ## Import GPIO library
import time ## Import 'time' library. Allows us to use 'sleep'

GPIO.setmode(GPIO.BCM) ## Use board pin numbering
GPIO.setup(4, GPIO.OUT) ## Setup GPIO Pin 7 to OUT

speed = 1

while 1:
  GPIO.output(4,False)## Switch on pin 7
  time.sleep(1)
  GPIO.output(4,True)
