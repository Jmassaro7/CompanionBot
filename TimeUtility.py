#!/usr/bin/python3

import datetime
import time
from Verbal import Verbal
from Emotion import Emotion
import string
import os
import threading
verbal = Verbal()
emotion = Emotion()

class TimeUtility:
	def __init__(self):
		pass

	def processTimerInput(self, timerInput):
		word_dict = {"zero": 0, "0": 0, "one": 1, "1": 1, "two": 2, "2": 2, "three": 3, "3": 3, 
					 "four": 4, "4": 4, "five": 5, "5": 5, "six": 6, "6": 6, "seven": 7, "7": 7,
					 "eight": 8, "8": 8, "nine": 9, "9": 9,"ten": 10, "10": 10, "eleven": 11, 
					 "11": 11, "twelve": 12, "12": 12, "thirteen": 13, "13": 13,"fourteen": 14, 
					 "14": 14, "fifteen": 15, "15": 15,"sixteen": 16, "16": 16,"seventeen": 17, 
					 "17": 17, "eighteen": 18, "18": 18, "nineteen": 19, "19": 19,"twenty": 20, 
					 "20": 20, "thirty": 30, "30": 30, "forty": 40, "40": 40, "fifty": 50, "50": 50}
		result = 0
		valueExists = False
		timerInput = timerInput.translate(str.maketrans('','',string.punctuation)).lower()
		print(timerInput + "/")
		for word in timerInput.split():
			if word in word_dict:
				valueExists = True
				result += word_dict[word]
				print(str(result))
		if(valueExists): return result

		else: return int(timerInput)

	def set_timer(self):
		while True:
			# Get hours, minutes, and seconds from user
			Verbal.textToSpeech("How many hours would you like on your timer?")
			displayThread = threading.Thread(target=Emotion.display_animations, args=("surprised",), daemon=True)
			displayThread.start()
			input_hours = Verbal.speechToText("timer.wav",3)
			input_hours = "0"#Verbal.speechToText("timer.wav" , 3)+
			Verbal.textToSpeech("How many minutes would you like on your timer?")
			displayThread = threading.Thread(target=Emotion.display_animations, args=("surprised",), daemon=True)
			displayThread.start()
			input_minutes = Verbal.speechToText("timer.wav",3)
			input_minutes = "0"#Verbal.speechToText("timer.wav", 3)
			Verbal.textToSpeech("How many seconds would you like on your timer?")
			displayThread = threading.Thread(target=Emotion.display_animations, args=("surprised",), daemon=True)
			displayThread.start()
			input_seconds = Verbal.speechToText("timer.wav",3)
			input_seconds = "20"#Verbal.speechToText("timer.wav", 3)

			if input_hours is not None and input_minutes is not None and input_seconds is not None:
				print("Input: " + input_hours + " hours, " + input_minutes + " minutes, and " + input_seconds + " seconds.")

				# Convert inputs to integers
				timer_hour = self.processTimerInput(input_hours)
				timer_minute = self.processTimerInput(input_minutes)
				timer_second = self.processTimerInput(input_seconds)

				print(str(timer_hour) + ":" + str(timer_minute) + ":" + str(timer_second))

				timer_hour = int(timer_hour)
				timer_minute = int(timer_minute)
				timer_second = int(timer_second)

				# Calculate total seconds for the timer
				total_seconds = timer_hour * 3600 + timer_minute * 60 + timer_second

				# Get the current time in seconds
				current_time = time.time()

				# Calculate the alert time in seconds
				alert_time = current_time + total_seconds

				while True:
					current_time = time.time()
					if current_time >= alert_time:
						
						os.system("aplay /home/companion/Documents/New/chat/venv/Alarm.wav")
						break

					print(f"Target time: {time.ctime(alert_time)}")
					print(f"Current time: {time.ctime(current_time)}")
					print("If you would like to cancel the timer, say 'cancel'")
					displayThread = threading.Thread(target=Emotion.display_animations, args=("happy",), daemon=True)
					displayThread.start()
					Verbal.textToSpeech("The clock is ticking. If you would like to cancel the timer, say 'cancel'")
					displayThread = threading.Thread(target=Emotion.display_animations, args=("timer",), daemon=True)
					displayThread.start()
					timerInput = Verbal.speechToText("timer.wav", 5)
					
					if timerInput is None:
						print("timerInput is None")
						timerInput = ""
					
					if "cancel." in timerInput.lower() or "cancel" in timerInput.lower():
						displayThread = threading.Thread(target=Emotion.display_animations, args=("surprised",), daemon=True)
						displayThread.start()
						Verbal.textToSpeech("The timer has been cancelled.")
						break

					time.sleep(1)
				displayThread = threading.Thread(target=Emotion.display_animations, args=("happy",), daemon=True)
				displayThread.start()
				Verbal.textToSpeech("Fun! What else would you like to try from my main menu?")
				break
			else: 
				displayThread = threading.Thread(target=Emotion.display_animations, args=("confused",), daemon=True)
				displayThread.start()
				Verbal.textToSpeech("I'm sorry, I could not quite hear you. Could you please repeat your timer options?")
			
	def getTime():
		current_time = datetime.datetime.now()
		current_time_str = current_time.strftime("It is currently %I:%M %p on %A, %B %d, %Y")
		return current_time_str
