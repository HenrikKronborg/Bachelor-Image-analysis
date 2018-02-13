import cv2
import numpy as np
im = cv2.imread("test.png", cv2.IMREAD_GRAYSCALE)

def asd():
    
    params = cv2.SimpleBlobDetector_Params()

    params.minThreshold = 10;
    params.maxThreshold = 200;

    params.filterByColor = True
    params.blobColor = 255

    params.filterByArea = True
    params.minArea = 5000 #Sette størrelsen på piksel til stjerne

    params.filterByCircularity = True
    params.minCircularity = 0.1

    params.filterByConvexity = False
    params.filterByInertia = False

    detector = cv2.SimpleBlobDetector_create(params)
    #print(str(detector))
    keypoints = detector.detect(im)
    if  not keypoints:
        print("Tom")
        
        im_with = cv2.drawKeypoints(im, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
        cv2.imshow("keypoinjts", im_with)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        return 0
    else:
        print("detet")
        im_with = cv2.drawKeypoints(im, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
        cv2.imshow("keypoinjts", im_with)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        return 1

print(asd())
