import cv2
import numpy as np
import os
from glob import glob

capture = cv2.VideoCapture("video.avi")

def asd(object):
    image_path = "bilder/frame_0000.jpg"
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
