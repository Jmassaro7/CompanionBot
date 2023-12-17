#!/usr/bin/python3

import os
import csv
import boto3
import threading

class Emotion:
	
	def __init__(self):
		pass
		
	def evaluateEmotions():
		# Read access keys from a CSV file
		with open('Jakob_accesskeys.csv', 'r') as csvInput:
			next(csvInput)
			reader = csv.reader(csvInput)
			for line in reader:
				access_key_id = line[0]
				secret_access_key = line[1]

		# Ensure the indentation of the following lines is consistent with the block above
		photo = 'test.jpg'

		# Create a Rekognition client using the access keys
		client = boto3.client('rekognition', region_name='us-east-2', aws_access_key_id=access_key_id,
			aws_secret_access_key=secret_access_key)

		# Open the image file for reading
		with open(photo, 'rb') as source_image:
			source_bytes = source_image.read()

		# Use the source_bytes to send the image to the detect_faces function
		response = client.detect_faces(Image={'Bytes': source_bytes}, Attributes=['ALL'])

		# Check if faces are detected in the response
		if 'FaceDetails' in response:
			emotions = []

			# Iterate over detected faces
			for face_detail in response['FaceDetails']:
				# Extract emotions if available
				if 'Emotions' in face_detail:
					for emotion in face_detail['Emotions']:
						# Extract the type and confidence of the emotion
						emotion_type = emotion['Type']
						emotion_confidence = emotion['Confidence']
						emotions.append((emotion_type, emotion_confidence))

			for emotion, confidence in emotions:
				#for emotion, confidence in emotions:
				print(emotion)
				displayThread = threading.Thread(target=Emotion.display_animations, args=(str(emotion).lower(),3), daemon=True)
				displayThread.start()
				
				if("unknown" not in str(emotion).lower()):
					response = "I can say with " + str(int(confidence)) + " percent confidence that you seem " + str(emotion).lower()
					return response
				else:
					response = "No faces were detected in the image."
					return response
		else:
			response = "No faces were detected in the image."
			return response
	
	def display_animations(emotion):
		if emotion.lower() == "dance":
			os.system("mpg321 -q dance.mp3")
		if emotion.lower() == "listeningThree":
			os.system("mplayer -vf scale=800:600 -noborder -x 800 -y 600 ThreeSecondsListening.mp4")
		
		if emotion.lower() == "listeningFive":
			os.system("mplayer -vf scale=800:600 -noborder -x 800 -y 600 FiveSecondsListening.mp4")
		
		if emotion.lower() == "listeningSeven":
			os.system("mplayer -vf scale=800:600 -noborder -x 800 -y 600 SevenSecondsListening.mp4")	
		
		if emotion.lower() == "thinking":
			os.system("mplayer -vf scale=800:600 -noborder -x 800 -y 600 ThinkingV.mp4")
		
		if emotion.lower() == "happy" or emotion.lower()=="calm":
			os.system("mplayer -vf scale=800:600 -noborder -x 800 -y 600 HappyV.mp4")
		
		if emotion.lower() == "calm":
			os.system("mplayer -vf scale=800:600 -noborder -x 800 -y 600 CalmedV.mp4")
		
		if emotion.lower() == "sad":
			os.system("mplayer -vf scale=800:600 -noborder -x 800 -y 600 SadV.mp4")
		
		if emotion.lower() == "surprised":
			os.system("mplayer -vf scale=800:600 -noborder -x 800 -y 600 SurprisedV.mp4")	
		
		if emotion.lower() == "angry":
			os.system("mplayer -vf scale=800:600 -noborder -x 800 -y 600 AngryV.mp4")
		
		if emotion.lower() == "confused" or emotion.lower() == "unknown":
			os.system("mplayer -vf scale=800:600 -noborder -x 800 -y 600 ConfusedV.mp4")


		if emotion.lower() == "disgusted":
			os.system("mplayer -vf scale=800:600 -noborder -x 800 -y 600 DisgustedV.mp4")
			
		if emotion.lower() == "fear":
			os.system("mplayer -vf scale=800:600 -noborder -x 800 -y 600 ScaredV.mp4")
			
		if emotion.lower() == "idle":
			os.system("mplayer -vf scale=800:600 -noborder -x 800 -y 600 IdleV.mp4")
			
		if emotion.lower() == "timer":
			os.system("mplayer -vf scale=800:600 -noborder -x 800 -y 600 TimerV.mp4")
		
