#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

LedPin = 19    # PIN our parallel LED's are connected to
LedBlue = 17    # PIN our blue LED is connected to

def setup():
        GPIO.setmode(GPIO.BCM)       # Numbers GPIOs by Hardware PIN #
	
        GPIO.setup(LedPin, GPIO.OUT)   # Set LedPin's mode is output
		GPIO.output(LedPin, False) # Set LedPin high(+3.3V) to off led
        
        GPIO.setup(LedBlue, GPIO.OUT) #set up Blue LED as output
        GPIO.output(LedBlue, False) # set Blue LED to be off at start

def loop():
	while True:
	    GPIO.output(LedPin, False)  # Parallel LED's off
	    time.sleep(0.5) # wait .5 seconds
            GPIO.output(LedBlue, True) # Blue LED On
            time.sleep(0.5)
            GPIO.output(LedBlue, False) # Blue LED off
            time.sleep(0.5)
	    GPIO.output(LedPin, True) # Parallel LED's on
	    time.sleep(0.5)
		
def destroy():
	GPIO.output(LedPin, False)    
    GPIO.output(LedBlue, False)
	GPIO.cleanup()                     # Release resource
		
if __name__ == '__main__':     # Program start from here
	setup()
        try:
			loop
		except KeyboardInterrupt:
			destroy()