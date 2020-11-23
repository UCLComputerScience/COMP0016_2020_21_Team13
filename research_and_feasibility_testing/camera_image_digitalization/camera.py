import cv2
import numpy as np
import time

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
nImage = 0
startTime = time.time()

while(True):
    ret,frame = cap.read()
    #cv2.imshow("camera",frame)
    k = cv2.waitKey(1) & 0xFF
    if k == ord("q"):
        break;
    # take a picture every 2 seconds (better change to every move)
    if time.time()-startTime >= 60:
        imgName = "Image{}.png".format(nImage)
        cv2.imwrite(imgName, frame)
        print("picture formed")
        startTime = time.time()
        #cv2.findcontour()
    nImage += 1
    

cap.release()
cv2.destroyAllWindows()
