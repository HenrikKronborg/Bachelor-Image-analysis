#!/urs/bin/python
import os
import time
from datetime import datetime
import cv2
import numpy as np
#from time import gmtime, strftime

#20.02 test lappeteppe
img_mask = "C:\\Users\\Mathias\\AppData\\Local\\Programs\\Python\\Python36-32\\a.png"
capture = cv2.VideoCapture("video.avi")
 



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

###im = cv2.imread(object, cv2.IMREAD_GRAYSCALE)
###retval, otsu = cv2.threshold(im, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

#For trim-arrayen
class VideoArrayObject(object):
		start = 0
		stopp = 0
		duration = 0
		def __init__(self, name, startT, stoppT, dura):
			self.name = name
			self.start = startT
			self.stopp = stoppT
			self.duration = dura

test = 0
test2 = 0
stoppTrim = 0
startTrim = 0
duration = 0
CompletedVideoQueue = Queue()
detectionPhase = False
detectionArray = []
detectionAmount = 0


def MathiasAlg():
	while(True):
 
    ret, frame = capture.read()
 

 
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
 

 
    #cv2.imshow("frame", gray)
 
    if cv2.waitKey(1) & 0xFF == ord("q"):
 
        break
 
    cv2.imwrite('a.png', gray)
 
    print(gray)
 
    print(asd("C:\\Users\\Mathias\\AppData\\Local\\Programs\\Python\\Python36-32\\a.png"))
 
    #os.system("rm a.png")
 
   # os.popen('Del /F C:\\Users\\Mathias\\AppData\\Local\\Programs\\Python\\Python36-32\\a.png')
 
    cv2.waitKey(0)
 

 
capture.release()
 
cv2.destroyAllWindows()
 
    
    
def asd(object):
 
    image_path = img_mask
 
    print(object)
 
    print(image_path)
 
    im = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
 
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
 
        print("Tom")
 
        return 0
 
    else:
 
        print("detekt")
 
        
 
        im_with = cv2.drawKeypoints(threshold, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
 
        #cv2.imshow("DETEKSJON", im_with)
 
        cv2.waitKey(0)
 
        cv2.destroyAllWindows()
 
        return 1

def AlarmPhase(isDetect):
	#Variabler som holder styr på tiden
	#ta inn filmetid (0-60s), 
	#variabel som sjekker om det fortsatt er alarmstatus /bool
		#isDetect er enten 0 eller 1
	global stoppTrim
	global startTrim
	global duration
	global detectionPhase
	global detectionArray
	global detectionAmount

	if isDetect == 1:
		if detectionPhase == False:
			print(" >[] Detection []<")
			#startTrim = counter-1 må byttes ut med tidspunktet til framen.
			startTrim = frame.name
			#konverter navnet til faktisk tid
			detectionPhase = True
		
			
		elif detectionPhase == True:
			print("Currently in detectionPhase, not storing a new startTrim")
			
		
	else:
		if detectionPhase == False:
			print("No detection")

		elif detectionPhase == True:
			print(" >[X] Deteksjon avsluttet [X]< ")
			detectionPhase = False
			#stoppTrim = counter+1 bytt
			#duration = stoppTrim - startTrim bytt
			#Få tak i frame name evt?
			trimName = "Detect_"+str(detectionAmount)
			#dette tallet må resetes ved nytt "intervall"
			detectionAmount += 1
			print("Trim videoen på tidspunk: ", startTrim, " (",startTrim+1,")")
			print("Slutt trimmingen på tidspunkt: ", stoppTrim," (",stoppTrim-1,")")
			print("Varighet: ", duration)
			
			
			
			detectionArray.append(VideoArrayObject(trimName, startTrim, stoppTrim, duration))
			print(detectionArray[(detectionAmount-2)].name, "Added.")
			
			""""
			videoName = "test15.mp4"
			trimmedVideo = "[TRIMMED]"+videoName
			#Videoen som tak tas i heter ikke altid "test15.mp4"
			#-loglevel quiet fjerner ALL output fra ffmpeg
			########Ikke behandle det her; vent til alle detekteringssteder fra array er med. 1x60s loop
			os.system("ffmpeg -loglevel quiet -i " + videoName + " -ss 00:00:" + str(startTrim) + " -t 00:00:" + str(duration) + " -async 1 -strict -2 " + trimmedVideo)
			#Lage objekter som har dette som properties, lagre objektene i en array(?), foreach/in
			"""
			'''
'''
## obs, filstier *kan* variere
##Lag mappe for neste intervall
def egenFunk():
	global test
	while(test < 3): #while som simulerer tre intervaller med filming&frames
		i = datetime.now()
		CurrentVideo = str(i.strftime('%Y_%m_%d_%H:%M:%S:%f'))
		print(CurrentVideo)
		####os.system("mkdir /home/nvidia/Bachelor/Frames/" + CurrentVideo)
		obj = VideoObj(CurrentVideo, False)
		
		#TODO: Film --> Henrik_Code() bruker CurrentVideo 
		print("")
		#TODO(?):vent til alle frames er filmet ferdig; 
		
		#print("Videoen er ferdiglagd, setter status = True og objektet blir lagt til i CompletedVideoQueue")
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

		




	##Hvis det er to video-intervaller i Videoer-mappen; start analyse på første//Kan byttes ut med noe annet så lenge vi ikke begynner før et helt intervall er ferdig.
	#if len(os.listdir('/home/nvidia/Bachelor/Videoer')) > 1:
		#todo: for			
			#if end=".mp4"

def mainProg():
	#if len(os.listdir('/home/nvidia/Bachelor/Videoer')) > 1: #Mulig en bare kan(og burde) se bort i denne 99% sure
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
			##Gå igjennom tilhørende Frames-folder
			#for frame in os.listdir(testpath):
			####if frame.lower().endswith('mp4'):
					####print(MathiasAlg(frame))
					#JonasAlg(MathiasAlg(frame))
					#print("frame")
			
			#orgVideo = video.name
			#orgVideoPath = "/home/nvidia/Bachelor/Videoer/" + orgVideo
			#print(orgVideoPath)
			#for detection in detectionArray:
			#_Gjør noe med tindspunktene start(), dura() Sjekk navn, obj
			#	os.system("ffmpeg -i " + orgVideoPath + " -ss 00:00:04 -t 00:00:01 -async 1 -strict -2 /home/nvidia/Bachelor/Trims/[T]"+detection.name)
			
			#Vent?
			#for trim in os.listdir("home/nvidia/Bachelor/Trims"):
				#TODO Send over til Hessdalen.no MathiasCode?
			
			####os.system("rm -rv /home/nvidia/Bachelor/Videoer/"+orgVideo) # Benytt -rf til slutt
			####os.system("rm -v /home/nvidia/Bachelor/Trims/*")
			####os.system("rm -rv /home/nvidia/Bachelor/Frames/"+orgVideo)

		#else:
		#	print("Ingen videoer i køen.")
		
		
egenFunk()
