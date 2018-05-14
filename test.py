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


frameStart = 30
stopTime = 90

capture = cv2.VideoCapture("Detections/Trims/14-05-2018_10-31-53.mp4")

capture.set(1, frameStart)

count = frameStart
while(capture.isOpened()):
	ret, frame = capture.read()
	
	if ret == False:
		break

	cv2.imshow("test", frame)
	cv2.waitKey(30)
	
	if count >= stopTime:
		break
	
	count += 1
	
capture.release()
cv2.destroyAllWindows()
