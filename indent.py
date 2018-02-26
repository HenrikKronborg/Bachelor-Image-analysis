#!/urs/bin/python
import os
import time
from datetime import datetime
import cv2
import numpy as np

#20.02 test lappeteppe
#23.02 lappeteppe good to go

class Queue:
	def __init__(self):
		self.items = []

	def isEmpty(self):
		return self.items == []

	def enqueue(self, item):
		self.items.insert(0,item)

	def dequeue(self):
		return self.items.pop()

	def size(self):
		return len(self.items)

#For køen
class VideoObj(object):
	name = ""
	finished = False
	def __init__(self, timestamp, status):
		self.name = timestamp
		self.finished = status

class VideoArrayObject(object):
		start = 0.0
		stopp = 0.0
		duration = 0.0
		startFrame = 0
		endFrame = 0
		def __init__(self, name, startT, stoppT, dura, sFrame, eFrame):
			self.name = name
			self.start = startT
			self.stopp = stoppT
			self.duration = dura
			self.startFrame = sFrame
			self.endFrame = eFrame
			


test = 0
test2 = 0
stoppTrim = 0
startTrim = 0
duration = 0.0
CompletedVideoQueue = Queue()
detectionPhase = False
detectionArray = []
detectionAmount = 0
video = ""
antNuller = 0
antEnere = 0
videoName = ""
startTime = 0.0
stopTime = 0.0
frameCounter = 1
captureFrameRate = 300
timeOfFrame = 0
frameStarter = 0
frameEnder = 0

def MathiasAlg():
	global videoName
	global frameCounter
	filePath = "Videoer/"+videoName
	capture = cv2.VideoCapture(filePath)
	print("MathiasAlg:",filePath)
	while(capture.isOpened()):
		ret, frame = capture.read()
		if ret == False:
			break
			
		cv2.imwrite('a.png', frame)

		AlarmPhase(asd("/home/nvidia/Bachelor/a.png"))
		frameCounter += 1

	capture.release()
	cv2.destroyAllWindows()
	print("Antall nuller: " + str(antNuller))
	print("Antall enere: " + str(antEnere))
	
	
def asd(object):
	#print(object)
	#print(image_path)
	im = cv2.imread(object, cv2.IMREAD_GRAYSCALE)
	retval, threshold = cv2.threshold(im, 200, 255, cv2.THRESH_BINARY_INV)	 
	params = cv2.SimpleBlobDetector_Params()
	params.minThreshold = 100; 
	params.maxThreshold = 260;
	params.filterByColor = False
	params.blobColor = 255 #høgt tall er hvitt, små tall er mørkt 
	params.filterByArea = True 
	params.minArea = 30 #Sette størrelsen på piksel til stjerne
	params.maxArea = 4000
	params.filterByCircularity = False #Disse må være med, blir satt standard til true
	params.filterByConvexity = False
	params.filterByInertia = False
	detector = cv2.SimpleBlobDetector_create(params) 
	keypoints = detector.detect(threshold)
 
	if  not keypoints:
		#print("Tom")
		global antNuller
		antNuller += 1
		return 0
 
	else:
		print("Detection")#
		im_with = cv2.drawKeypoints(threshold, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
		cv2.destroyAllWindows()
		global antEnere
		antEnere += 1
		return 1

def AlarmPhase(isDetect):
	#isDetect er enten 0 eller 1
	global stoppTrim
	global startTrim
	global duration
	global detectionPhase
	global detectionArray
	global detectionAmount
	global timeOfFrame
	global startTime
	global stopTime
	global frameCounter
	global frameStarter
	global frameEnder

	if isDetect == 1:
		if detectionPhase == False:
			frameStarter = frameCounter
			print(" >[] Detection []< in", videoName)
			#print(videoName)
			startTime = (frameCounter/30)-1
			print("Starttime:",startTime)
			detectionPhase = True
			
		elif detectionPhase == True:
			print("Currently in detectionPhase, not storing a new startTrim")
			
	else:
		if detectionPhase == False:
			print("No detection")#do nothing
			
		elif detectionPhase == True:
			frameEnder = frameCounter
			print(" >[X] Deteksjon avsluttet [X]< ")
			stopTime = frameCounter/30
			print("stopTime:",stopTime)
			duration = (stopTime - startTime)+1
			detectionPhase = False
			detectionAmount += 1
			print("Trim videoen på tidspunk: ", startTime, " (",startTime-1,"), Frame# : ",frameStarter)
			print("Slutt trimmingen på tidspunkt: ", stopTime," (",stopTime+1,") Frame# : ",frameEnder)
			print("Varighet: ", duration)
			detectionArray.append(VideoArrayObject(videoName, startTime, stopTime, duration, frameStarter, frameEnder))
			print(detectionArray[(detectionAmount-2)].name, "Added to array.")
			
			
def egenFunk():
	global test
	while(test < 2): #while som simulerer tre intervaller med filming&frames
		i = datetime.now()
		#CurrentVideo = str(i.strftime('%Y_%m_%d_%H:%M:%S:%f'))
		CurrentVideo = "2018_02_21_09:42:30" + ".mp4"
		print(CurrentVideo)

		####os.system("mkdir /home/nvidia/Bachelor/Frames/" + CurrentVideo)
		obj = VideoObj(CurrentVideo, False)
		
		#TODO: Film --> Henrik_Code() bruker CurrentVideo 
		print("")
		#TODO(?):vent til alle frames er filmet ferdig; 
		
		print("Videoen er ferdiglagd, setter status = True og objektet blir lagt til i CompletedVideoQueue")
		setattr(obj, 'finished', 'True')
		CompletedVideoQueue.enqueue(obj) ###lage objektet her inne i steden for
		##^ Denne køen blir sjekket lengre nede i mainProg
		#print("Filmet ferdig: ",thisObject.finished)
		
		time.sleep(1.1)# For test
		test += 1
	mainProg()
	#Skriv ut køen
	#while test2 < videoQueue.size():
	#	temp = videoQueue.dequeue()
	#	print(temp.name +" : "+ temp.finished)


def mainProg():
	#if len(os.listdir('/home/nvidia/Bachelor/Videoer')) > 1: #Mulig en bare kan(og burde) se bort i denne 99% sure
		if not CompletedVideoQueue.isEmpty():
			print("Fant video")
			
			global videoName
			global frameCounter
			video = CompletedVideoQueue.dequeue() #Alle videoer som ligger i denne er ferdig behandlet.
			videoName = video.name
			print(videoName)
			MathiasAlg()
			
			#orgVideo = video.name
			orgVideoPath = "/home/nvidia/Bachelor/Videoer/" + videoName
			#print(orgVideoPath)
			print("Antall frames i videoen:",frameCounter)
			print("Antall deteksjoner:",detectionAmount)
			print("Filsti:", orgVideoPath)
			print("")
			print("Deteksjoner (array):")
			for detection in detectionArray:
				print("Navn:",detection.name,", starttidspunkt:",detection.start,", stopptidspunkt:",detection.stopp,", duration:",detection.duration,", startframe:",detection.startFrame,", endframe:", detection.endFrame)
			####TRIM FILM
			####TODO: (def?)Reset alle variabler
			
			#_Gjør noe med tindspunktene start(), dura() Sjekk navn, obj
				#os.system("ffmpeg -i " + str(orgVideoPath) + " -ss " +  str(detection.start) + " -t " + str(detection.duration) + " -async 1 -strict -2 /home/nvidia/Bachelor/Trims/[T]"+detection.name)
				#print("Ferdig")
			#Vent?
			#for trim in os.listdir("home/nvidia/Bachelor/Trims"):
				#TODO Send over til Hessdalen.no MathiasCode?
			
			####os.system("rm -rv /home/nvidia/Bachelor/Videoer/"+videoName) # Benytt -rf til slutt
			####os.system("rm -v /home/nvidia/Bachelor/Detections/Trims/*")
			####os.system("rm -rv /home/nvidia/Bachelor/Frames/"+videoName)

egenFunk()


