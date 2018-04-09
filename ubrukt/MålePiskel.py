import cv2
import numpy as np
import os
from glob import glob

def asd():
    #im = cv2.imread("Hess1.jpg", cv2.IMREAD_GRAYSCALE)
    #im = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    im = cv2.imread("resultat.png")
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    #im = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)
    #hue ,saturation ,value = cv2.split(im)
    
    retval, threshold = cv2.threshold(gray, 40, 255, cv2.THRESH_BINARY_INV)
    medianFiltered = cv2.medianBlur(threshold, 5)

    params = cv2.SimpleBlobDetector_Params()
    
    params.minThreshold = 100;
    params.maxThreshold = 260;

    params.filterByColor = False
    params.blobColor = 255 #høgt tall er hvitt, små tall er mørkt

    params.filterByArea = True
    params.minArea = 50 #Sette størrelsen på piksel til stjerne
    params.maxArea = 4000

    params.filterByCircularity = False #Disse må være med, blir satt standard til true
    params.filterByConvexity = False
    params.filterByInertia = False

    detector = cv2.SimpleBlobDetector_create(params)
    keypoints = detector.detect(medianFiltered)
    if  not keypoints:
        print("Tom")
        return 0
    else:
        print("detekt")
        
        im_with = cv2.drawKeypoints(medianFiltered, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
        cv2.imshow("DETEKSJON", im_with)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        return 1

asd()
