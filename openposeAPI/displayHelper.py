import cv2
import numpy as np
from DirectPath import PartPairs
#Canvas helper function

# create canvas
def init_canvas(width, height, color=(255, 255, 255)):
    canvas = np.ones((height, width, 3), dtype="uint8")
    canvas[:] = color
    return canvas
# determine the size of the canvas
def getSize(array):
    value1 = array[0]
    value2 = array[1]
    if value1>value2:
        print(value1," ",value2)
        return value1,value2
    else:
        return value2,value1
# return keep points in tuple form
def keypointsTuple(datum):
    result = []
    size = datum.shape[1]
    for i in range(0,size):
        point = (datum[0][i][0],datum[0][i][1])
        result.append(point)
    return result
# showing images and display the string as the heading on the window
def displayImage(string,canvas):
    cv2.imshow(string, canvas)
    cv2.waitKey(0)



# Processing Canvas
# Drawing circles as keypoints onto a canvas
def kponly(canvas, datum):
    try:
        kp = keypointsTuple(datum.poseKeypoints)
    except Exception as error:
        # print("Input is an array")
        kp = datum
    for i in range (0,len(kp)):
        a = int(kp[i][0])
        b = int(kp[i][1])
        cv2.circle(canvas,(a,b),5,[0,0,0],-1)
    return canvas

# Drawing lines between keypoints onto a canvas can be array or datum
def addingLine(canvas,datum):
    try:
        kp = keypointsTuple(datum.poseKeypoints)
    except Exception as error:
        # print("Input is an array")
        kp = datum
        
    for i in range(0,len(PartPairs)):
        p1 = PartPairs[i][0]
        p2 = PartPairs[i][1]
        # print(kp[p1],kp[p2])
        if kp[p1] ==(0.0,0.0) or kp[p2]==(0.0,0.0):
            continue
        cv2.line(canvas,kp[p1],kp[p2],[65,105,225],3)
    return canvas

