import cv2
import numpy as np
from opInfo import PartPairs
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
def drawingKeypoints(canvas, datum):
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
def drawingLines(canvas,datum,color=[0,0,0]):
    try:
        kp = keypointsTuple(datum.poseKeypoints)
    except Exception as error:
        # print("Input is an array")
        kp = datum
        
    for i in range(0,len(PartPairs)):
        p1 = PartPairs[i][0]
        p2 = PartPairs[i][1]
        # print(kp[p1],kp[p2])
        point1 = (int(kp[p1][0]),int(kp[p1][1]))
        point2 = (int(kp[p2][0]),int(kp[p2][1]))
        if point1 ==(0.0,0.0) or point2==(0.0,0.0):
            continue
        cv2.line(canvas,point1,point2,color,3)
    return canvas

# combine two skeleton together
def combineSkele(datumMod, datumInp):
    keypointMod = keypointsTuple(datumMod.poseKeypoints)
    keypointInp = keypointsTuple(datumInp.poseKeypoints)
    # print(result)
    width, height = getSize(datumMod.cvOutputData.shape)
    canvas = init_canvas(height,width)
    canvas = drawingKeypoints(canvas,keypointMod)
    canvas = drawingLines(canvas,keypointMod)
    canvas = drawingKeypoints(canvas,keypointInp)
    canvas = drawingLines(canvas,keypointInp,[122,122,122])
    return canvas

