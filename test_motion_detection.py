#!/usr/bin/env python3

# USAGE
# python motion_detector.py
# python motion_detector.py --video videos/example_01.mp4

import argparse
import datetime
import time
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video", help="path to the video file")
ap.add_argument("-a", "--min-area", type=int, default=55, help="minimum area size")
args = vars(ap.parse_args())

if args.get("video", None) is None:
	camera = cv2.VideoCapture("tcambin ! video/x-bayer,format=bggr,width=1024,height=768,framerate=30/1 ! capssetter join=false caps=\"video/x-bayer,format=gbrg\" ! bayer2rgb ! videoconvert ! appsink")
	time.sleep(0.25)
else:
	camera = cv2.VideoCapture(args["video"])

firstFrame = None
counter = 0

mask = cv2.imread("/home/nvidia/Desktop/Bachelor/mask.png")
grayMask = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)
retvalMask, thresholdMask = cv2.threshold(grayMask, 0, 255, cv2.THRESH_BINARY_INV)


while True:
	(grabbed, frame) = camera.read()
	text = "Unoccupied"
	
	if not grabbed:
		break
	
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	gray = cv2.GaussianBlur(gray, (	3, 3), 0)
	
	if firstFrame is None:
		firstFrame = gray
		continue
	
	frameDelta = cv2.absdiff(firstFrame, gray)
	thresh = cv2.threshold(frameDelta, 25, 255, cv2.THRESH_BINARY)[1]
	
	thresh = cv2.bitwise_and(thresh, thresholdMask)
	
	#dilate = cv2.dilate(thresh.copy(), None, iterations=2)
	thresh = cv2.dilate(thresh, None, iterations=2)
	#cv2.imshow("dilate", dilate)
	#cv2.waitKey(3)
	
	#thresh = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, None)
	#cv2.imshow("morphology", thresh)
	#cv2.waitKey(3)
	
	#_, cnts, _ = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
	_, cnts, _ = cv2.findContours(thresh.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
	
	for c in cnts:
		if(cv2.contourArea(c) < 50):
			continue

		#(x, y, w, h) = cv2.boundingRect(c)
		#cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
		
		(x, y), radius = cv2.minEnclosingCircle(c)
		cv2.circle(frame, (int(x), int(y)), int(radius), (0, 0, 255), 2)
		
		#cv2.drawContours(frame, [c], -1, (0,0,255), 2)		
		text = "Occupied"

	cv2.putText(frame, "Room Status: {}".format(text), (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
	cv2.putText(frame, datetime.datetime.now().strftime("%A %d %B %Y %I:%M:%S%p"), (10, frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 0, 255), 1)

	# show the frame and record if the user presses a key
	cv2.imshow("Security Feed", frame)
	cv2.waitKey(3)
	#cv2.imshow("Thresh", thresh)
	#cv2.imshow("Frame Delta", frameDelta)
	key = cv2.waitKey(1) & 0xFF

	if key == ord("q"):
		break
	
	if counter % 30 == 0:
		firstFrame = gray
	counter += 1

camera.release()
cv2.destroyAllWindows()
