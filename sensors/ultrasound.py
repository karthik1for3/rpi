import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
TRIG = 4 
ECHO = 17
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
try:  
  while 1:
    GPIO.output(TRIG, False)
    time.sleep(0.2)
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)
    while GPIO.input(ECHO)==0:
      pass
    pulse_start = time.time()

    while GPIO.input(ECHO)==1:
      pass
    pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150
    distance = round(distance, 2)
    #print distance
    if distance <= 5:
      print 'very close'
    if distance >= 100:
      print 'very far'
except:
  GPIO.cleanup()
GPIO.cleanup()

