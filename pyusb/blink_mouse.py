import RPi.GPIO as GPIO ## Import GPIO library
import time ## Import 'time' library. Allows us to use 'sleep'

GPIO.setmode(GPIO.BCM) ## Use board pin numbering
GPIO.setup(2, GPIO.OUT) ## Setup GPIO Pin 7 to OUT
GPIO.setup(3, GPIO.OUT) ## Setup GPIO Pin 7 to OUT

speed = 1

import sys
import usb.core
import usb.util
# decimal vendor and product values
dev = usb.core.find(idVendor=0x3938, idProduct=0x1031)
# or, uncomment the next line to search instead by the hexidecimal equivalent
#dev = usb.core.find(idVendor=0x45e, idProduct=0x77d)
# first endpoint
interface = 0
endpoint = dev[0][(0,0)][0]
# if the OS kernel already claimed the device, which is most likely true
# thanks to http://stackoverflow.com/questions/8218683/pyusb-cannot-set-configuration
if dev.is_kernel_driver_active(interface) is True:
	# tell the kernel to detach
	dev.detach_kernel_driver(interface)
	# claim the device
	usb.util.claim_interface(dev, interface)
collected = 0
attempts = 50
while 1:#collected < attempts :
    try:
		data = dev.read(endpoint.bEndpointAddress,endpoint.wMaxPacketSize)
		collected += 1
		if data[1] == 4:
			break
		#print data, data[1]#data.find('['), data.find(']')]
		if data[1] == 1:
			print "left"
			GPIO.output(2,True)## Switch on pin 7
			GPIO.output(3,False)
			time.sleep(speed)## Wait
		if data[1] == 2:
			print "right"
			GPIO.output(2,False)## Switch off pin 7
			GPIO.output(3,True)
			time.sleep(speed)## Wait
		#GPIO.cleanup()
		#print data
    except usb.core.USBError as e:
		data = None
		if e.args == ('Operation timed out',):
			continue
# release the device
usb.util.release_interface(dev, interface)
# reattach the device to the OS kernel
dev.attach_kernel_driver(interface)

