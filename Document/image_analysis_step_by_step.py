#!/usr/bin/env python3

import cv2
import numpy as np

frame = cv2.imread("new.jpg")
old = cv2.imread("old.jpg")

### Maske
mask = cv2.imread("mask.png")
grayMask = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)
retvalMask, thresholdMask = cv2.threshold(grayMask, 0, 255, cv2.THRESH_BINARY_INV)
###

grayOld = cv2.cvtColor(old, cv2.COLOR_BGR2GRAY)
cv2.imwrite("bilder/grayOld.jpg", grayOld, [int(cv2.IMWRITE_JPEG_QUALITY), 100])

grayOld = cv2.GaussianBlur(grayOld, (3, 3), 0)
cv2.imwrite("bilder/blurOld.jpg", grayOld, [int(cv2.IMWRITE_JPEG_QUALITY), 100])

gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
cv2.imwrite("bilder/gray.jpg", gray, [int(cv2.IMWRITE_JPEG_QUALITY), 100])

gray = cv2.GaussianBlur(gray, (3, 3), 0)
cv2.imwrite("bilder/blur.jpg", gray, [int(cv2.IMWRITE_JPEG_QUALITY), 100])

frameDelta = cv2.absdiff(grayOld, gray)
cv2.imwrite("bilder/forskjell.jpg", frameDelta, [int(cv2.IMWRITE_JPEG_QUALITY), 100])

thresh = cv2.threshold(frameDelta, 25, 255, cv2.THRESH_BINARY)[1]
cv2.imwrite("bilder/threshold.jpg", thresh, [int(cv2.IMWRITE_JPEG_QUALITY), 100])

thresh = cv2.bitwise_and(thresh, thresholdMask)
cv2.imwrite("bilder/thresholdMedMaske.jpg", thresh, [int(cv2.IMWRITE_JPEG_QUALITY), 100])

thresh = cv2.dilate(thresh, None, iterations=2)
cv2.imwrite("bilder/thresholdDilate.jpg", thresh, [int(cv2.IMWRITE_JPEG_QUALITY), 100])

_, contours, _ = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

contourList = []
for contour in contours:
	if cv2.contourArea(contour) < 200: #or cv2.contourArea(contour) > 500:
		continue
	
	(x, y), radius = cv2.minEnclosingCircle(contour)
	cv2.circle(frame, (int(x), int(y)), int(radius), (0, 0, 255), 2)
	contourList.append(contour)

cv2.imwrite("bilder/markert.jpg", frame, [int(cv2.IMWRITE_JPEG_QUALITY), 100])