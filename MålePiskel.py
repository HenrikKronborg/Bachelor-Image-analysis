import cv2
import numpy as np

im = cv2.imread("Hess1.jpg", cv2.IMREAD_GRAYSCALE)
retval, otsu = cv2.threshold(im, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
retval2, threshold2 = cv2.threshold(im, 12, 255, cv2.THRESH_BINARY)

mean = cv2.adaptiveThreshold(im, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,11,2)

def asd():
    
    params = cv2.SimpleBlobDetector_Params()

    params.minThreshold = 10;
    params.maxThreshold = 400;

    params.filterByColor = False
    params.blobColor = 255 #høgt tall er hvitt, små tall er mørkt

    params.filterByArea = True
    params.minArea = 20 #Sette størrelsen på piksel til stjerne
    params.maxArea = 5000

    params.filterByCircularity = False #Disse må være med, blir satt standard til true
    params.filterByConvexity = False
    params.filterByInertia = False

    detector = cv2.SimpleBlobDetector_create(params)
    #print(str(detector))
    keypoints = detector.detect(otsu)
    if  not keypoints:
        print("Tom")

        return 0
    else:
        print("detet")
        
        im_with = cv2.drawKeypoints(otsu, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
        cv2.imshow("DETEKSJON", im_with)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        return 1

print(asd())
