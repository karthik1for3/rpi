import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
TRIG = 23
GPIO.setup(TRIG,GPIO.OUT)
while True:
  GPIO.output(TRIG, False)
  time.sleep(0.5)
  GPIO.output(TRIG, True)
  time.sleep(0.5)
  GPIO.output(TRIG, False)
GPIO.cleanup()
