#!/urs/bin/python
import os
import time
from datetime import datetime
import cv2
import numpy as np
#from time import gmtime, strftime


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


class VideoObj(object):
	name = ""
	finished = False
	def __init__(self, timestamp, status):
		self.name = timestamp
		self.finished = status

###im = cv2.imread(object, cv2.IMREAD_GRAYSCALE)
###retval, otsu = cv2.threshold(im, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

detectionArray = []
CompletedVideoQueue = Queue()
test = 0
test2=0

def MathiasAlg():
    
    params = cv2.SimpleBlobDetector_Params()

    params.minThreshold = 10;
    params.maxThreshold = 400;

    params.filterByColor = False
    params.blobColor = 255 #høgt tall er hvitt, små tall er mørkt

    params.filterByArea = True
    params.minArea = 20 #Sette størrelsen på piksel til stjerne
    params.maxArea = 5000

    params.filterByCircularity = False #Disse må være med, blir satt standard til true
    params.filterByConvexity = False
    params.filterByInertia = False

    detector = cv2.SimpleBlobDetector_create(params)
    #print(str(detector))
    keypoints = detector.detect(otsu)
    if  not keypoints:
        print("Tom")

        return 0
    else:
        print("detet")
        
        im_with = cv2.drawKeypoints(otsu, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
        cv2.imshow("DETEKSJON", im_with)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        return 1

##Gjør noe i oppstarten èn gang
#TODO: def(?) innstillinger, startparametere(?)

#TODO: def threadStart():
##Egen prosess/tråd som konstant filmer i intervaller, lagrer nye mapper for frames osv(?)
#TODO: Start tråd som kjører independent, kanskje bare på kveldstid(?)
## obs, filstier *kan* variere
##Lag mappe for neste intervall
def egenFunk():
	global test
	while(test < 3):
		i = datetime.now()
		
		
		CurrentVideo = str(i.strftime('%Y_%m_%d_%H:%M:%S'))
		print(CurrentVideo)
		####os.system("mkdir /home/nvidia/Bachelor/Frames/" + CurrentVideo)
		obj = VideoObj(CurrentVideo, False)
		
		#TODO: Film --> Henrik_Code() bruker CurrentVideo
		#print("Filmer... videoen har status: false")
		print("")
		#TODO(?):vent til alle frames er filmet ferdig; 
		
		#print("Videoen er ferdiglagd, setter status = True og objektet blir lagt til i CompletedVideoQueue")
		setattr(obj, 'finished', 'True')
		CompletedVideoQueue.enqueue(obj) ###lage objektet her inne i steden for
		##^ Denne køen blir sjekket lengre nede i while
		#print("Filmet ferdig: ",thisObject.finished)
		
		time.sleep(1.1)# For test
		test += 1
	mainProg()
	#Skriv ut køen
	#while test2 < videoQueue.size():
	#	temp = videoQueue.dequeue()
	#	print(temp.name +" : "+ temp.finished)

		




	##Hvis det er to video-intervaller i Videoer-mappen; start analyse på første//Kan byttes ut med noe annet så lenge vi ikke begynner før et helt intervall er ferdig.
	#if len(os.listdir('/home/nvidia/Bachelor/Videoer')) > 1:
		#todo: for			
			#if end=".mp4"

def mainProg():
	if len(os.listdir('/home/nvidia/Bachelor/Videoer')) > 1: #Mulig en bare kan se bort i denne 99% sure
		if not CompletedVideoQueue.isEmpty():
			print("Fant video")
			#while test2 < CompletedVideoQueue.size():
			#	temp = CompletedVideoQueue.dequeue()
			#	print(temp.name +" : "+ temp.finished)
			####video = CompletedVideoQueue.dequeue() #Alle videoer som ligger i denne er ferdig behandlet.
			####path = "/home/nvidia/Bachelor/Frames/"+video.name
			testpath = "/home/nvidia/Bachelor/Frames/Bilder"
			#print(path)
			#print(orgNavn)
			##Få tak i tilhørende mappe
			for frame in os.listdir(testpath): #Hva er frame her? navnet? Må kanskje ta tak i på annet vis
				###print(MathiasAlg(frame))
				#JonasAlg(MathiasAlg(frame))
				#print("framee")
			
			orgVideo = video.name
			orgVideoPath = "/home/nvidia/Bachelor/Videoer/" + orgVideo
			#print(orgVideoPath)
			for detection in detectionArray:		#_Gjør noe med tindspunktene start(), dura()									#Sjekk navn, obj
				os.system("ffmpeg -i " + orgVideoPath + " -ss 00:00:04 -t 00:00:01 -async 1 -strict -2 /home/nvidia/Bachelor/Trims/[T]"+detection.name)
			
			#Vent?
			for trim in os.listdir("home/nvidia/Bachelor/Trims"):
				#TODO Send over til Hessdalen.noe
				
				
			###os.system(remove /home/nvidia/Bachelor/$orgVideoPath)
			###os.system(remove /home/nvidia/Bachelor/Trims .*)
			###os.system(remove /home/nvidia/Bachelor/Frames/path)
		else:
			print("Ingen videoer i køen.")
		
		
		
		
	
	
#print("hei")
egenFunk()


'''
for video in os.listdir('/home/bachelor/Git/Bachelor/raw'):
	if video.endswith('.mp4'):
		global deteksjonArray
		#//send "video" inn i algoritmen
		#analyseAlgo(video)
		#//Inne i analyseAlgo blir AlarmPhase() kalt --> lagrer alle detek.objekter i deteksjonArray
		os.system("ffmpeg -i /home/bachelor/Git/Bachelor/raw/"+ video + " -ss 00:00:04 -t 00:00:01 -async 1 -strict -2 /home/bachelor/Git/Bachelor/trims/[T]" +  video)
   #^Filnavnet blir allerede lagret som datoen/orginalfil(?)
		

	#//Gå igjennom alle lagrede deteksjoner for denne videoen og lag trims 
	for deteksjon in deteksjonArray:
		
		#os.system("ffmpeg -i " + str(deteksjon.name) + " -ss 00:00:" + str(deteksjon.start) + " -t 00:00:" + str(deteksjon.duration) + " -async 1 strict -2 [Trimmed]" + deteksjon.name + ".mp4")

	#Når analysen er ferdig lager vi 
	#print(strftime("%Y-%m-%d %H:%M:%S", gmtime()))
	#print(gmtime())
	

print("Ferdig")
'''