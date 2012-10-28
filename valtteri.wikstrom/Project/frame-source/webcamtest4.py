#!/usr/bin/env python
import time
import os
import RPi.GPIO as GPIO
import cv

##camera setup

capture = cv.CreateCameraCapture(0)

#function for cropping cv-images
def crop(img, left, top, new_width, new_height):
	cropped = cv.CreateImage( (new_width, new_height), 8, 3)
	src_region = cv.GetSubRect(img, (left, top, new_width, new_height))
	cv.Copy(src_region, cropped)
	return cropped

width = 352 
height = 288 

cv.SetCaptureProperty(capture,cv.CV_CAP_PROP_FRAME_WIDTH,width)    

cv.SetCaptureProperty(capture,cv.CV_CAP_PROP_FRAME_HEIGHT,height) 





##SPI setup
GPIO.setmode(GPIO.BCM)
DEBUG = 1

# read SPI data from MCP3008 chip, 8 possible adc's (0 thru 7)
def readadc(adcnum, clockpin, mosipin, misopin, cspin):
        if ((adcnum > 7) or (adcnum < 0)):
                return -1
        GPIO.output(cspin, True)

        GPIO.output(clockpin, False)  # start clock low
        GPIO.output(cspin, False)     # bring CS low

        commandout = adcnum
        commandout |= 0x18  # start bit + single-ended bit
        commandout <<= 3    # we only need to send 5 bits here
        for i in range(5):
                if (commandout & 0x80):
                        GPIO.output(mosipin, True)
                else:
                        GPIO.output(mosipin, False)
                commandout <<= 1
                GPIO.output(clockpin, True)
                GPIO.output(clockpin, False)

        adcout = 0
        # read in one empty bit, one null bit and 10 ADC bits
        for i in range(12):
                GPIO.output(clockpin, True)
                GPIO.output(clockpin, False)
                adcout <<= 1
                if (GPIO.input(misopin)):
                        adcout |= 0x1

        GPIO.output(cspin, True)
        
        adcout >>= 1       # first bit is 'null' so drop it
        return adcout

# change these as desired - they're the pins connected from the
# SPI port on the ADC to the Cobbler
SPICLK = 4
SPIMISO = 17
SPIMOSI = 21
SPICS = 22

# set up the SPI interface pins
GPIO.setup(SPIMOSI, GPIO.OUT)
GPIO.setup(SPIMISO, GPIO.IN)
GPIO.setup(SPICLK, GPIO.OUT)
GPIO.setup(SPICS, GPIO.OUT)

#button setup
BUTTON = 25
GPIO.setup(BUTTON, GPIO.IN)



# distance sensor
analog_pin = 2;
last_read = 0 

print 'loop starts'

##loop starts
img = cv.QueryFrame(capture)
while True:

        # read the analog pin
        distance = readadc(analog_pin, SPICLK, SPIMOSI, SPIMISO, SPICS)
	#print distance
        last_read = distance
        # hang out and do nothing in seconds
        # time.sleep(0.1)

	#keyboard input
	#k = cv.WaitKey(100)

	#query camera

	#img = cv.QueryFrame(capture)
	#print time.clock()-timer
#	if started == True:
#		time.sleep(0.01)
#		cv.QueryFrame(capture)
	
	if not GPIO.input(BUTTON):
		#skip frames
		for x in range(0, 4):
			cv.QueryFrame(capture);
		img = cv.QueryFrame(capture);
		#cv.GrabFrame(capture)
		#img = cv.RetrieveFrame(capture)
		print 'taking picture'
		norm_d = 1.0-(max(min(distance, 700), 200)-200)/500.0
		print str(distance) + ' ' + str(norm_d)
		left = int(norm_d*100)
		top = int(norm_d*50)
		cropped = crop(img, left, top, width-left*2, int(2*(width-left*2)/3) )
		cv.SaveImage("crop.png", cropped)

	#time.sleep(0.1)


