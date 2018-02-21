#!/urs/bin/python
import os
import time
from datetime import datetime
import cv2
import numpy as np

#20.02 test lappeteppe
img_mask = "C:\\Users\\Mathias\\AppData\\Local\\Programs\\Python\\Python36-32\\a.png"
#capture = cv2.VideoCapture("video.avi")


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
		#print(gray)
		print(asd("C:\\Users\\Mathias\\AppData\\Local\\Programs\\Python\\Python36-32\\a.png"))
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