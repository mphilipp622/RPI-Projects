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

def parallel():
    #this function will set the parallel LED's on and the Blue one off
    GPIO.output(LedPin, True)
    GPIO.output(LedBlue, False)

def blue():
    #This function turns on the blue LED but turns off the parallel LED's
    GPIO.output(LedBlue, True)
    GPIO.output(LedPin, False)

def all():
    #This function turns on all the LED's!
    GPIO.output(LedBlue, True)
    GPIO.output(LedPin, True)

def off():
    #turn off all LED's
    GPIO.output(LedBlue, False)
    GPIO.output(LedPin, False)

def destroy():
	GPIO.output(LedPin, False)     # Set High before cleaning up
        GPIO.output(LedBlue, False)
	GPIO.cleanup()                     # Release resource

def inputLoop():
    try:
        while True:
            choice = raw_input("""What Do you Want to Do?\n\n'parallel': turn the parallel LED's on\n'blue': Turn the Blue LED on\n'loop': Start the blinking LED loop (ctrl+c to break loop)\n'all': Turn all the LED's on\n'off': Turn all the LED's off\n'quit': Quit the program\n\n""")
            
            if choice == "loop":
	        try:
	            loop()
	        except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
	            continue
            elif choice == "parallel":
                parallel()
            elif choice == "blue":
                blue()
            elif choice == "all":
                all()
            elif choice == "off":
                off()
            elif choice == "quit":
                break
    except KeyboardInterrupt:
        destroy()


if __name__ == '__main__':     # Program start from here
	setup()
        inputLoop()
        destroy()
