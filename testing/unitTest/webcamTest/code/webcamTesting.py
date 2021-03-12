import os
import sys
import math
import cv2
# from PIL import Image
import matplotlib.pyplot as plt

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(dir_path + r'/../../../../team13api');
import team13api

width, height = 800, 600
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

def takeScreenshot():
    ref, frame = cap.read()
    return frame


def picturesToBeProcessed(dirName):
    dir_path = os.path.dirname(os.path.abspath(__file__))
    imageFolderName = dir_path + dirName
    try:
        if os.path.isdir(imageFolderName):
            fileNames = [f.path for f in os.scandir(imageFolderName)
                    if f.is_file() and f.path.endswith(('.png','.jpg'))
                ]
    except Exception as e:
        print(dirName , " does not exits")
    # if len(fileNames)>2:
    #     print("too many pictures in a single file")
    #     return
    return fileNames

def dirList(directory):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    path = dir_path + directory
    folderName = [f.path for f in os.scandir(path) if f.is_dir]
    return folderName

def displayImages(images,score):
    nImageEachRow = int(math.sqrt(len(images)) + 1)
    nImageEachCol = len(images)//nImageEachRow + 1
    fig, ax = plt.subplots(nrows=nImageEachCol, ncols=nImageEachRow)
    flattenedAx = ax.flatten()
    for i in range(0, len(images)):
        flattenedAx[i].imshow(images[i])
        flattenedAx[i].set_title(score[i])
    for i in flattenedAx:
        i.axis("off")



# print(dir(team13api))
folderList = picturesToBeProcessed(r'/../data')
score = []
combinedSkeleton = []
i=0
while i <len(folderList):
    # score.append(Scoring(f[0],f[1]))
    userImage = takeScreenshot()
    result,skeletonImage, success = team13api.compareWITHmodel(folderList[i],userImage)
    if not success:
        print("did not detect anyone in the picture")
        continue
    i+=1
    score.append(result)
    combinedSkeleton.append(skeletonImage)

displayImages(combinedSkeleton,score)
plt.show()