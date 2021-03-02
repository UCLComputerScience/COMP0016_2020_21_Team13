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
    # take a picture every 60 seconds (better change to every move)
    if ret and time.time()-startTime >= 60:
        imgName = "Image{}.png".format(nImage)
        cv2.imwrite(imgName, frame)
        print("picture{} formed".format(nImage))
        a = np.asarray(frame)
        print(a)
        #print(type(a))
        #print(a.shape)
        startTime = time.time()
        nImage += 1
    

cap.release()
cv2.destroyAllWindows()
