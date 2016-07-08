import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
TRIG = 4 
ECHO = 17
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
    return distance

def measure_avg():
    d1 = measure()
    time.sleep(0.1)
    d1 += measure()
    time.sleep(0.1)
    d1 += measure()
    d1 /= 3
    return d1

while True:
    try:
        d = measure_avg()
        print d, 'cm'
        time.sleep(0.25)
    except KeyboardInterrupt:
        GPIO.cleanup()
GPIO.cleanup()

