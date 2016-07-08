import RPi.GPIO as GPIO ## Import GPIO library
import time ## Import 'time' library. Allows us to use 'sleep'

GPIO.setmode(GPIO.BCM) ## Use board pin numbering
GPIO.setup(2, GPIO.OUT) ## Setup GPIO Pin 7 to OUT
GPIO.setup(3, GPIO.OUT) ## Setup GPIO Pin 7 to OUT
GPIO.setup(4, GPIO.OUT)
GPIO.setup(17, GPIO.OUT) ## Setup GPIO Pin 7 to OUT
GPIO.setup(27, GPIO.OUT) ## Setup GPIO Pin 7 to OUT
GPIO.setup(22, GPIO.OUT)


GPIO.output(4,True)
GPIO.output(17,True)
GPIO.output(2,True)## Switch on pin 7
GPIO.output(3,False)
GPIO.output(27,True)## Switch on pin 7
GPIO.output(22,False)
speed = 1

import sys
import usb.core
import usb.util
dev = usb.core.find(idVendor=0x3938, idProduct=0x1031)
interface = 0
endpoint = dev[0][(0,0)][0]
if dev.is_kernel_driver_active(interface) is True:
	dev.detach_kernel_driver(interface)
	usb.util.claim_interface(dev, interface)
collected = 0
attempts = 50
while 1:#collected < attempts :
    try:
		data = dev.read(endpoint.bEndpointAddress,endpoint.wMaxPacketSize)
		collected += 1
		if data[1] == 4:
			break
		if data[1] == 1:
			print "left"
			GPIO.output(4,True)## Switch on pin 7
			GPIO.output(17,False)
			time.sleep(speed)## Wait
		if data[1] == 2:
			print "right"
			GPIO.output(4,False)## Switch off pin 7
			GPIO.output(17,True)
                        time.sleep(speed)## Wait
    except usb.core.USBError as e:
		data = None
		if e.args == ('Operation timed out',):
			continue
GPIO.output(4,False)
GPIO.output(17,False)
usb.util.release_interface(dev, interface)
dev.attach_kernel_driver(interface)
GPIO.cleanup()
