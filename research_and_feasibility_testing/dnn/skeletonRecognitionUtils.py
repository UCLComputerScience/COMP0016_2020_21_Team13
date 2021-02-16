import cv2
import os

workingDir = os.path.dirname(os.path.abspath(__file__))
protoFile = os.path.join(workingDir, "pose/mpi/pose_deploy_linevec_faster_4_stages.prototxt")
weightsFile = os.path.join(workingDir, "pose/mpi/pose_iter_160000.caffemodel")
net = cv2.dnn.readNetFromCaffe(protoFile, weightsFile)

def findSkeleton(f):
    frame = f.copy()
    inWidth = frame.shape[1]
    inHeight = frame.shape[0]

    inpBlob = cv2.dnn.blobFromImage(frame, 1.0 / 255, (inWidth, inHeight), (0, 0, 0), swapRB=False, crop=False)
    net.setInput(inpBlob)

    output = net.forward()

    H = output.shape[2]
    W = output.shape[3]
    points = []
    for i in range(44):
        probMap = output[0, i, :, :]
        minVal, prob, minLoc, point = cv2.minMaxLoc(probMap)
        x = (inWidth * point[0]) / W
        y = (inHeight * point[1]) / H

        cv2.circle(frame, (int(x), int(y)), 5, (0, 255, 255), thickness=-1, lineType=cv2.FILLED)
        cv2.putText(frame, "{}".format(i), (int(x), int(y)), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 255), 1, lineType=cv2.LINE_AA)
        points.append((int(x), int(y)))
    POSE_PAIR = [[0,1],[1,2],[2,3],[3,4],[1,5],[5,6],[6,7],[1,14],[14,8],[8,9],[9,10],[14,11],[11,12],[12,13]]
    for pair in POSE_PAIR:
        partA = pair[0]
        partB = pair[1]
        cv2.line(frame, points[partA], points[partB], (0, 255, 0), 3)
    return frame




