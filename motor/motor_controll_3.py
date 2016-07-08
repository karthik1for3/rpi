import RPi.GPIO as GPIO 
import time 

GPIO.setmode(GPIO.BCM) ## Use board pin numbering
GPIO.setup(4, GPIO.OUT)
GPIO.setup(6, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)

GPIO.output(6, True)
GPIO.output(17,True)
GPIO.output(4,True)

speed = 0.5
try:
  with open("sample.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        bin = ' '.join(format(ord(x), 'b') for x in line)
        #print bin
        for l in bin:
            print l
            if l == '0':
              GPIO.output(4,True)## Switch on pin 7
              GPIO.output(17,False)
              time.sleep(speed)## Wait
            else:
              GPIO.output(4,False)## Switch off pin 7
              GPIO.output(17,True)
              time.sleep(speed)## Wait
except:
  GPIO.output(4,False)
  GPIO.output(17,False)
  GPIO.cleanup()
#GPIO.output(4,False)
#GPIO.output(17,False)
GPIO.cleanup()
