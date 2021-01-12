import cv2
import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

protoFile = "pose/mpi/pose_deploy_linevec_faster_4_stages.prototxt"
weightsFile = "pose/mpi/pose_iter_160000.caffemodel"
net = cv2.dnn.readNetFromCaffe(protoFile, weightsFile)


# POSE_PAIR is a list made up by two-element list (eg [[1,2],[3,4]]), each sublist tells 
# which pair of points are connected together
POSE_PAIR = [[0,1],[1,2],[2,3],[3,4],[1,5],[5,6],[6,7],[1,14],[14,8],[8,9],[9,10],[14,11],[11,12],[12,13]]

# lists to hold pictures to be displayed:
# skeletonFrame: holds picture after skeleton has been added to the picture
# originFrame: holds original picture
skeletonFrame=[]
originFrame=[]

# list which holds the name of the picture
frameName=[]

# constants to be used in the funciont plt.subplot, for skeleton picture or original picture respectively
sub_plot_skeleton = [222,224]
sub_plot_origin = [221,223]

def inputImage():
    # put all the image(.jpg/.png) file from the images folder into a list to iterate
    fileName = [f.path for f in os.scandir('images')
            if f.is_file() and f.path.endswith(('.png','.jpg'))
        ]
    return fileName

def ImageName(list):
    frameName=[]
    for f in list:
        title_name_one = f[7:]
        frameName.append(title_name_one)
    return frameName

def processImage(f):
    frame = f.copy()
    print(frame.shape)
    inWidth = frame.shape[1]
    inHeight = frame.shape[0]

    threshold = 0.8
    inpBlob = cv2.dnn.blobFromImage(frame, 1.0 / 255, (inWidth, inHeight), (0, 0, 0), swapRB=False, crop=False)
    net.setInput(inpBlob)

    output = net.forward()

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
    for pair in POSE_PAIR:
        partA = pair[0]
        partB = pair[1]
        cv2.line(frame, points[partA], points[partB], (0, 255, 0), 3)
    # plt.subplot(111)
    # plt.imshow(frame)
    # plt.title("good")
    # plt.axis('off')
    # plt.show()

def main():
    originFrame=[]
    skeletonFrame=[]
    frameName = inputImage()
    for f in frameName:
        frame = mpimg.imread(f)
        originFrame.append(frame)
        skeletonImage = processImage(frame)
        skeletonFrame.append(skeletonImage)


# list = inputImage()
# picture = list[0]
# frame=mpimg.imread(picture)
# processImage(frame)




# for i in range (len(skeletonFrame)):
#     # fig = plt.figure()
#     plt.subplot(sub_plot_origin[i])
#     plt.imshow(originFrame[i])
#     plt.title(frameName[i])
#     plt.axis('off')
#     plt.subplot(sub_plot_skeleton[i])
#     plt.imshow(skeletonFrame[i])
#     plt.title('Skeleton')
#     plt.axis('off')
# plt.show()

