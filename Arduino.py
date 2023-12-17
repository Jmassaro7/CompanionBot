#!/usr/bin/python3

import RPi.GPIO as GPIO
import time

is_drive = 29 #output
is_dance = 31 #output
is_ready = 37 #input

class Arduino:
	#using bool convention since these are GPIO pins which correspond to these values

	def __init__(self):
		pass

	def initialize():
		#configure pins
		#GPIO.setwarnings(False) #it complains, but the pins are actually open based off of hardware documentation
		GPIO.setmode(GPIO.BOARD)
		GPIO.setup(is_drive,GPIO.OUT)
		GPIO.setup(is_dance,GPIO.OUT)
		GPIO.setup(is_ready,GPIO.IN)

		GPIO.output(is_drive, GPIO.LOW)
		GPIO.output(is_dance,GPIO.LOW)
		
	def arduinoCall(choice):	
		#Arduino shall be in ready state before another option can be selected, else wait
		while(GPIO.input(is_ready) == True):
			print("Is ready")
			GPIO.output(is_drive, GPIO.LOW)
			GPIO.output(is_dance,GPIO.LOW)
			print("Is ready state: " + str(GPIO.input(is_ready)))
			
			if(choice == 1):
				GPIO.output(is_dance, GPIO.HIGH)
				GPIO.output(is_dance, GPIO.LOW)
				GPIO.output(is_drive, GPIO.LOW)
				print("Sending dance input from Pi to Arduino.")
				
			elif(choice == 2):
				GPIO.output(is_drive,GPIO.HIGH)
				GPIO.output(is_drive,GPIO.LOW)
				GPIO.output(is_dance,GPIO.LOW)
				print("Sending drive input from Pi to Arduino.")
			else:
				print("invalid")
				
		while (GPIO.input(is_ready) == False):
			GPIO.output(is_drive, GPIO.LOW)
			GPIO.output(is_dance,GPIO.LOW)
			#print("waiting")
			time.sleep(0.1)
			break
