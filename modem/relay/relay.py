import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
TRIG = 17
GPIO.setup(TRIG,GPIO.OUT)
while True:
  GPIO.output(TRIG, False)
  time.sleep(1)
  print 'off'
  GPIO.output(TRIG, True)
  time.sleep(1)
  print 'on'
  #GPIO.output(TRIG, False)
GPIO.cleanup()
