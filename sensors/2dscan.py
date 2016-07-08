#!#/usr/bin/python

import RPi.GPIO as GPIO ## Import GPIO library
import time ## Import 'time' library. Allows us to use 'sleep'

GPIO.setmode(GPIO.BCM) ## Use board pin numbering

TRIG = 18 
ECHO = 24
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

def measure():
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
    return distance

def measure_avg():
    d = measure()
    time.sleep(0.1)
    d += measure()
    time.sleep(0.1)
    d += measure()
    d /= 3
    return d


while True:
    try:
        d = measure_avg()
        print d, 'cm'
        '''
        if d <= 15:
            print "avoid"
        else:
            print 'move'
        '''
    except KeyboardInterrupt:
        GPIO.cleanup()
        break

GPIO.cleanup()
