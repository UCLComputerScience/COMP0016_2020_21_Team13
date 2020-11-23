import cv2
import numpy as np

#cap = cv2.VideoCapture('/home/lilly/dancegame/【溟雨】性感在可爱面前一文不值！thumbs up！超可爱旗袍竖屏蹦迪.mp4')
img = cv2.imread('/home/lilly/dancegame/viewc2.png')
cv2.imshow("frame",img)
cv2.waitkey(5000)
print("done")

'''
while(True):
    ret,frame = cap.read()
    #print(ret)
    #print(frame)
    #cv2.imshow("camera",frame)
    k = cv2.waitKey(1) & 0xFF
    if k == ord("s"):
        cv2.imwrite('image.jpg'%(i), img)
    elif k == ord("q"):
        break;
    #cv2.findcontour()

cap.release()
'''
cv2.destroyAllWindows()