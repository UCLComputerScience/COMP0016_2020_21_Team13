import cv2
import numpy as np
import time

cap = cv2.VideoCapture('/home/lilly/dancegame/【溟雨】性感在可爱面前一文不值！thumbs up！超可爱旗袍竖屏蹦迪.mp4')
nImage = 0
startTime = time.time()

while(True):
    ret,frame = cap.read()
    #cv2.imshow("camera",frame)
    k = cv2.waitKey(1) & 0xFF
    if k == ord("q"):
        break;
    # take a picture every 2 seconds (better change to every move)
    if time.time()-startTime >= 2:
        imgName = "Image{}.png".format(nImage)
        cv2.imwrite(imgName, frame)
        #cv2.findcontour()
    nImage += 1
    

cap.release()
cv2.destroyAllWindows()