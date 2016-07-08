from django.shortcuts import render 
from django.shortcuts import render_to_response
import RPi.GPIO as GPIO ## Import GPIO library 
import time ## Import 'time' library. Allows us to use 'sleep'

GPIO.setmode(GPIO.BCM) ## Use board pin numbering
GPIO.setup(2, GPIO.OUT) ## Setup GPIO Pin 7 to OUT
GPIO.setup(3, GPIO.OUT) ## Setup GPIO Pin 7 to OUT


# Create your views here.

def control(request, led=1):
  GPIO.output(2,False)## Switch on pin 7
  GPIO.output(3,False)
  GPIO.output(int(led), True)
  #time.sleep(speed)
  return render_to_response('control.html', {})

def home(request):
  return render_to_response('control.html', {})
