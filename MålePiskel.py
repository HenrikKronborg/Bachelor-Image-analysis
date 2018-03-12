import cv2
import numpy as np
import os
from glob import glob

img_mask = "C:\\Users\\Mathias\\AppData\\Local\\Programs\\Python\\Python36-32\\Bilder\\"
def asd(object):
    image_path = img_mask + object
    print(image_path)
    #im = cv2.imread("Hess1.jpg", cv2.IMREAD_GRAYSCALE)
    #im = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    im = cv2.imread(image_path)
    im = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)
   # hue ,saturation ,value = cv2.split(im)
    
    retval, threshold = cv2.threshold(im, 137, 255, cv2.THRESH_BINARY_INV)
    medianFiltered = cv2.medianBlur(threshold,3)

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

for fn in os.listdir(img_mask):
    print(asd(fn))
