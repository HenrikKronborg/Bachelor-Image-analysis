#!/usr/bin/env python3

import cv2
import numpy as np
import time
import os
import math
import sys
import gi
from datetime import datetime, timedelta
from multiprocessing import *
import subprocess
import copy

gi.require_version("Tcam", "0.1")
gi.require_version("Gst", "1.0")

from gi.repository import Tcam, Gst

# Number of seconds to record and save
filmDuration = 20
# Location of the project files
filepath = "/home/nvidia/Bachelor/"
detectionPhase = False
previousFrame = None

def getSettings():
	global filepath
	
	# Read settings from the config.txt file saved from the control panel
	f = open(filepath + "config.txt", "r")
	
	for line in f:
		settings.append(line.strip("\n"))
	f.close()
	'''
	Settings read from the config.txt file with corresponding array location:
	0: Seconds saved before detection, 1: Seconds saved after detection, 2: Minimum object size for detection, 3: Maximum object size for detection,
	4: Number of frames before updating reference picture, 5: Number of frames containing a detection before start recording,
	6: Number of frames not containing a detection before stop recording, 7: Text overlay
	'''
	
	# Grayscale and threshold the mask drawn on the control panel.
	mask = cv2.imread(filepath + "mask.png")
	grayMask = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)
	retvalMaskTemp, thresholdMaskTemp = cv2.threshold(grayMask, 0, 255, cv2.THRESH_BINARY_INV)
	# Variable to share the mask between processes
	thresholdMask.value = thresholdMaskTemp

def record():
	global filepath
	
	while(True):
		currentTime = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
		
		Gst.init(sys.argv)
		pipeline = Gst.Pipeline.new()
		'''
		Pipeline to start recording. Records for previously defined number of seconds.
		Specifies wanted width, height, framerate and for it to be recorded in color
		Converts to and saves in MP4 format to previously defined filepath/Videos.
		Filename is set to the date and time the recording was started
		'''
		pipeline = Gst.parse_launch('tcamsrc num-buffers=' + str((filmDuration * 30)) +' serial=4810628 '
					+ '! tcamautoexposure '
					+ '! tcamwhitebalance '
					+ '! tcamautofocus '
					+ '! video/x-bayer,format=bggr,width=1024,height=768,framerate=30/1 '
					+ '! capssetter join=false caps="video/x-bayer,format=gbrg" '
					+ '! bayer2rgb '
					+ '! videoconvert '
					+ '! omxh264enc '
					+ '! mp4mux '
					+ '! filesink location=' + filepath + 'Videos/' + currentTime + '.mp4 ')
		pipeline.set_state(Gst.State.PLAYING)
		
		# Required to make the thread sleep while the function records. Addition of 0.5 to make sure the camera has time to save the MP4 file correctly before closing the thread
		time.sleep(filmDuration + 0.5)
		
		pipeline.set_state(Gst.State.NULL)
		
		# Add the filename to the queue
		recorded.put(currentTime)
		print(currentTime + " enqueuet")

def read():
	global detectionPhase
	global filepath
	
	while(True):
		# If the queue is not empty, read video
		if not recorded.empty():
			videoName.value = recorded.get()
			datetime_object = datetime.strptime(videoName.value, "%d-%m-%Y_%H-%M-%S")
			capture = cv2.VideoCapture(filepath + "Videos/" + videoName.value + ".mp4")
			
			frameNumber = 0
			detectStartCount = 0
			detectEndCount = 0
			while(capture.isOpened()):
				ret, frame = capture.read()
				
				if ret == False:
					break
				
				# Handling the returns from the picture analysis
				if analyse(frame, frameNumber) == 1:
					# The picture analysis returns 1:
					
					# Remembers the frame and frame number if detectionphase is false
					if detectionPhase == False:
						startFrame = frame
						startTime = frameNumber
						detectionPhase = True
						print("FIKK EN 1'ER OG NÅ HUSKER VI STARTFRAME :)")
					# Saves two images if the picture analysis has returned 1 a userdefined number of times in a row
					elif detectionPhase == True and detectStartCount == int(settings[5]):
						print("!!!!!!!!!!! DETECTION !!!!!!!!!!!")
						# Calculate to readable time from frameNumber
						frameTime = datetime_object + timedelta(seconds=frameNumber / 30)
						
						# Write text to image two times. First time in black, then a second time in white with a slightly smaller font. This to achieve a black border
						cv2.putText(startFrame, settings[7] + " " + frameTime.strftime("%d/%m/%Y %H:%M:%S"), (2,762), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0,0,0), 2)
						cv2.putText(startFrame, settings[7] + " " + frameTime.strftime("%d/%m/%Y %H:%M:%S"), (2,762), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255,255,255))
						cv2.imwrite(filepath + "Detections/Pictures/" + str(frameTime.strftime("%d-%m-%Y_%H-%M-%S")) + ".jpg", startFrame, [int(cv2.IMWRITE_JPEG_QUALITY), 100])
						
						# Draw the contours of detected phenomena onto the image
						for contour in contourList:
							(x, y), radius = cv2.minEnclosingCircle(contour)
							cv2.circle(startFrame, (int(x), int(y)), int(radius), (0, 0, 255), 2)
						cv2.imwrite(filepath + "Detections/Pictures/" + str(frameTime.strftime("%d-%m-%Y_%H-%M-%S")) + "_marked.jpg", startFrame, [int(cv2.IMWRITE_JPEG_QUALITY), 100])
					# Force trim if the picture analysis has returned 1 a userdefined number of times in a row and we're at the last frame of the video to avoid corrupted trims
					elif detectionPhase == True and frameNumber == (filmDuration * 30) - 2 and detectStartCount >= int(settings[5]):
						stopTime = frameNumber
						print("start " + str(startTime) + " slutt " + str(stopTime))
						trim(startTime, stopTime)
						print("AVBRYTER PGA SLUTT AV FILM!###########")
						detectionPhase = False
					# If we're in detectionphase, reset the detectEndCount variable that's counting number of times the picture analysis returns 0
					elif detectionPhase == True:
						print(str(frameNumber) + " Currently in detectionPhase, not storing a new startTrim")
						detectEndCount = 0
					
					print("detection start count " + str(detectStartCount))
					detectStartCount += 1					
				else:
					# The picture analysis returns 0:
					if detectionPhase == False:
						print(str(frameNumber) + "No detection")
					
					# Same logic as above. Force trim if the picture analysis has returned 1 a userdefined number of times in a row and we're at the last frame of the video to avoid corrupted trims
					if detectionPhase == True and frameNumber == (filmDuration * 30) - 2 and detectStartCount >= int(settings[5]):
						stopTime = frameNumber
						print("start " + str(startTime) + " slutt " + str(stopTime))
						trim(startTime, stopTime)
						print("AVBRYTER PGA SLUTT AV FILM!###########")
						detectionPhase = False
					# If we're in detectionphase
					elif detectionPhase == True:
						print(str(detectEndCount) + " detectEndCount")
						
						# If detectStartCount is less than or equal to the userdefined variable counting number of times the picture analysis returns 1 in a row, then reset the variable and go out of detectinophase
						if detectStartCount <= int(settings[5]):
							detectStartCount = 0
							detectionPhase = False
						# If the picture analysis returns 0 a userdefined number of times make a trim of the video and prepare the program for a new possible detection
						if detectEndCount == int(settings[6]):
							stopTime = frameNumber - int(settings[6])
							print("start " + str(startTime) + " slutt " + str(stopTime))
							trim(startTime, stopTime)
							detectionPhase = False
							detectStartCount = 0
							detectEndCount = 0
						
						detectEndCount += 1
					
					print("detection start count " + str(detectStartCount))
				
				# Save a new background image for the control panel at the 50th frame of read video
				if frameNumber == 50:
					cv2.imwrite(filepath + "reference.jpg", frame, [int(cv2.IMWRITE_JPEG_QUALITY), 100])
				
				frameNumber += 1

			capture.release()
			cv2.destroyAllWindows()
			
			upload()
			
			# Delete the read video
			os.system("rm -f " + filepath + "Videos/" + str(videoName.value) + ".mp4")
		
def analyse(frame, frameNumber):
	global previousFrame
	
	# If first read frame of video, grayscale and blur the frame so it can be used in the next call of this function. Return 0 to imply no detection
	if previousFrame is None:
		previousFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		previousFrame = cv2.GaussianBlur(previousFrame, (3, 3), 0)
		return 0
	
	# Grayscale the frame
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	
	# Blur the frame to reduse and remove noise. (3, 3) is the size - has to be an odd number
	gray = cv2.GaussianBlur(gray, (3, 3), 0)
	
	# Calculate the difference between the reference picture and frame we're handling now
	frameDelta = cv2.absdiff(previousFrame, gray)
	
	# Threshold the difference image, making it black and white. This is done by checking if every pixels average color is above 25
	# The calculation done for each pixel in the image:	(Red + Green + Blue) / 3
	thresh = cv2.threshold(frameDelta, 25, 255, cv2.THRESH_BINARY)[1]
	
	# Multiply the mask in, removing the parts of the image where the user has drawn on the control panel
	thresh = cv2.bitwise_and(thresh, thresholdMask.value)
	
	# Increase the white of the image. This is done to fill holes in the contours
	thresh = cv2.dilate(thresh, None, iterations=2)
	
	# Find all contours in the image and place them in an array
	_, contours, _ = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
	
	# New array to store only wanted contours
	contourList[:] = []
	for contour in contours:
		# For each contour in contours check if it's both larger and smaller than userdefined settings through the control panel
		if cv2.contourArea(contour) > float(settings[2]) and cv2.contourArea(contour) < float(settings[3]):
			contourList.append(contour)
	
	# Update reference picture at every userdefined frame. This setting is per standard 30, meaning the reference picture is updated every second
	if frameNumber % int(settings[4]) == 0:
		previousFrame = gray
	
	if not contourList:
		# Return no detection if the contourList array is empty
		return 0
	else:
		# Return detection if there's elements in the contourList array
		return 1

def trim(startTime, stopTime):
	global filepath
	
	# Calculate time based on the videos name
	datetime_object = datetime.strptime(videoName.value, "%d-%m-%Y_%H-%M-%S")
	filename = datetime_object + timedelta(seconds=startTime / 30)
	
	# Calculating which frame to start reading the video at. This also adds the userdefined number of seconds in the trim before the detection happened
	frameStart = startTime - (int(settings[0]) * 30)
	if(frameStart <= 0):
		frameStart = 0
	
	capture = cv2.VideoCapture(filepath + "Videos/" + str(videoName.value) + ".mp4")
	# Only read the video from the calculated start frame. This to avoid having to read the entire videofile
	capture.set(1, frameStart)
	# Specify where to make the new videofile, what format, frames per second and size
	out = cv2.VideoWriter(filepath + "Detections/Trims/" + str(filename.strftime("%d-%m-%Y_%H-%M-%S")) + ".mp4", 0x00000021, 30.0, (1024,768))
	
	count = 0
	while(capture.isOpened()):
		ret, frame = capture.read()
		
		if ret == False:
			break
		
		timeOverlay = datetime_object + timedelta(seconds=count / 30)
		
		# Write text to the bottom left corner telling the time and date
		cv2.putText(frame, settings[7] + " " + timeOverlay.strftime("%d/%m/%Y %H:%M:%S"), (2,762), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0,0,0), 2)
		cv2.putText(frame, settings[7] + " " + timeOverlay.strftime("%d/%m/%Y %H:%M:%S"), (2,762), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255,255,255))
		
		# Write read frame to the trim videofile
		out.write(frame)
		
		# Includes the userdefined number of seconds to include in the trim after the detection happened
		if count == (stopTime + (int(settings[1]) * 30)):
			break
		
		count += 1
		
	capture.release()
	out.release()
	cv2.destroyAllWindows()

def upload():
	global filepath
	
	# For each picture in filepath/Detections/Pictures, try to upload it. If upload is succesful delete the file
	for picture in os.listdir(filepath + "Detections/Pictures"):
		if uploadFile("Detections/Pictures/" + picture):
			os.system("rm -f " + filepath + "Detections/Pictures/" + picture)
	# For each trim in filepath/Detections/Trims, try to upload it. If upload is succesful delete the file
	for trim in os.listdir(filepath + "Detections/Trims"):
		if uploadFile("Detections/Trims/" + trim):
			os.system("rm -f " + filepath + "Detections/Trims/" + trim)

def uploadFile(filename):
	global filepath
	# Connect to the Hessdalen server through SCP and upload file specified in the functions parameter
	return not subprocess.Popen(["scp", filepath + filename, "hessfiles2@freja.hiof.no:/files/hessfiles2/test"]).wait()

if __name__ == "__main__":
	# Creating a manager to share variables between processes
	m = Manager()
	settings = m.list()
	recorded = m.Queue()
	videoName = m.Value('c', "")
	frameSave = m.Value('c', "")
	frameSaveMarked = m.Value('c', "")
	thresholdMask = m.Value('c', "")
	contourList = m.list()
	
	# If there exists videofiles from previous runs of the program, put them in the queue so they can be handled
	for video in os.listdir(filepath + "Videos"):
		recorded.put(os.path.splitext(video)[0])
	
	settingsProcess = Process(target=getSettings)		
	settingsProcess.start()
	settingsProcess.join()
	
	recordProcess = Process(target=record)
	readProcess = Process(target=read)
	
	recordProcess.start()
	readProcess.start()
	recordProcess.join()
	readProcess.join()
	
	recordProcess.terminate()
	readProcess.terminate()
