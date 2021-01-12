import cv2
import time

protoFile = "pose/mpi/pose_deploy_linevec_faster_4_stages.prototxt"
weightsFile = "pose/mpi/pose_iter_160000.caffemodel"
net = cv2.dnn.readNetFromCaffe(protoFile, weightsFile)

frame = cv2.imread("Images/kyte.jpg")
start = time.time()
print(frame.shape)
inWidth = frame.shape[1]
inHeight = frame.shape[0]

threshold = 0.8

inpBlob = cv2.dnn.blobFromImage(frame, 1.0 / 255, (inWidth, inHeight), (0, 0, 0), swapRB=False, crop=False)
net.setInput(inpBlob)

output = net.forward()
print(time.time()-start)
H = output.shape[2]
W = output.shape[3]
points = []

for i in range(15):
    probMap = output[0, i, :, :]
    minVal, prob, minLoc, point = cv2.minMaxLoc(probMap)
    x = (inWidth * point[0]) / W
    y = (inHeight * point[1]) / H

    cv2.circle(frame, (int(x), int(y)), 5, (0, 255, 255), thickness=-1, lineType=cv2.FILLED)
    cv2.putText(frame, "{}".format(i), (int(x), int(y)), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 255), 1, lineType=cv2.LINE_AA)
    points.append((int(x), int(y)))
    points.append(None)

cv2.imshow("Output-Keypoints",frame)
cv2.waitKey(0)
cv2.destroyAllWindows()




