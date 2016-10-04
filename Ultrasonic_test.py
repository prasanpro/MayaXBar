#Program to test ultrasonic sensor data in order to detect the level of liquid in each container
import os
import RPi.GPIO as GPIO
import time
import subprocess

# Define Ultrasonic pins 
TRIG = 2
ECHO = 3
# Trigger pin to connect LED for detection
RaspTrigger = 12

GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
GPIO.setup(RaspTrigger, GPIO.OUT)
print "Distance Measurement In Progress"

while True:
	GPIO.output(TRIG, False)
	#print "Waiting For Sensor To Settle"
	#time.sleep(2)
	
	GPIO.output(TRIG, True)
	time.sleep(0.00001)
	GPIO.output(TRIG, False)
	
	while GPIO.input(ECHO)==0:
	  pulse_start = time.time()
	
	while GPIO.input(ECHO)==1:
	  pulse_end = time.time()
	
	pulse_duration = pulse_end - pulse_start
	
	distance = pulse_duration * 17150
	
	distance = round(distance, 2)
	
	print "Distance:",distance,"cm"
	
	if (distance < 50):
		GPIO.output(RaspTrigger, True)
        #time.sleep(1)
	else:
		GPIO.output(RaspTrigger, False)
		time.sleep(0.1)
	
	# Clean up the GPIO ports to prevent any warning message during next execution
	# http://raspi.tv/2013/rpi-gpio-basics-3-how-to-exit-gpio-programs-cleanly-avoid-warnings-and-protect-your-pi
	GPIO.cleanup()	

