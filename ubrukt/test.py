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

'''
def folder():
	return subprocess.run(["ssh", "hessfiles2@freja.hiof.no", "ls test/"], shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False).stdout

checkFolder = folder()
checkFolder = str(checkFolder).strip("b'").replace("n", "").split('\\')


print(checkFolder)
'''

#subprocess.run(["ssh", "hessfiles2@freja.hiof.no", "chmod 777 test/15-05-2018"], shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False)

'''
checkFolder = str(folder()).strip("b'").replace("n", "").split('\\')
checkFolder.pop()

folderExist = False

for folder in checkFolder:
	if(folder == datetime.now().strftime("%d-%m-%Y")):
		folderExist = True

if folderExist == False:
	subprocess.run(["ssh", "hessfiles2@freja.hiof.no", "mkdir test/" + datetime.now().strftime("%d-%m-%Y")], shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False)
	print("laget folder")
'''

'''
def uploadFile(filename):
	global filepath
	
	return not subprocess.Popen(["scp", "/home/nvidia/Desktop/Bachelor/" + filename, "hessfiles2@freja.hiof.no:/files/hessfiles2/test"]).wait()

print(uploadFile("todo"))
'''
