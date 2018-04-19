#!/usr/bin/env python3
import datetime
import time
import cv2

firstFrame = None
counter = 0

camera = cv2.VideoCapture("tcambin ! video/x-bayer,format=bggr,width=1024,height=768,framerate=30/1 ! capssetter join=false caps=\"video/x-bayer,format=gbrg\" ! bayer2rgb ! videoconvert ! appsink")
time.sleep(0.25)

while True:
	(grabbed, frame) = camera.read()
	
	if(counter % 15 == 0):
		cv2.imwrite("/home/nvidia/Bachelor/dokument/bilde" + str(counter) + ".jpg", frame, [int(cv2.IMWRITE_JPEG_QUALITY), 100])	
	
	if not grabbed:
		break
	
	counter += 1

camera.release()
cv2.destroyAllWindows()
