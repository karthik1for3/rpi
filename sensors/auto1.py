import RPi.GPIO as GPIO ## Import GPIO library
import time ## Import 'time' library. Allows us to use 'sleep'

GPIO.setmode(GPIO.BCM) ## Use board pin numbering

GPIO.cleanup()

pe1 = 5
pe2 = 6
pmi1 = 4
pmi2 = 17
pmi3 = 22
pmi4 = 27 

GPIO.setup(pe1, GPIO.OUT)  #E1
GPIO.setup(pe2, GPIO.OUT)  #E2
GPIO.setup(pmi1, GPIO.OUT) #INT1
GPIO.setup(pmi2, GPIO.OUT) #INT2
GPIO.setup(pmi3, GPIO.OUT) #INT3
GPIO.setup(pmi4, GPIO.OUT) #INT4

GPIO.output(pe1,True)
GPIO.output(pmi1,False)
GPIO.output(pmi2,True)

GPIO.output(pe2, True)
GPIO.output(pmi3,True)
GPIO.output(pmi4,False)

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


speed = 1
print 'starting the program'
while True:
    try:
        d = measure()#_avg()
        #print d, 'cm' 
        if d <= 50:
            print "avoid"
            GPIO.output(pmi1,True)
            GPIO.output(pmi2,False)
            #GPIO.output(pmi3,True)
            #GPIO.output(pmi4,False)
            time.sleep(0.1)
            #GPIO.output(pmi3,False)
            #GPIO.output(pmi4,True)
        else:
            print 'move'
            GPIO.output(pmi1,False)
            GPIO.output(pmi2,True)
            GPIO.output(pmi3,False)
            GPIO.output(pmi4,True)
    except KeyboardInterrupt:
        GPIO.cleanup()
        #print sys.exc_info()[0] 
        break

GPIO.cleanup()
