import os
import sys
import math
from PIL import Image
import cv2
import matplotlib.pyplot as plt

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(dir_path + r'/../../../../team13api');
import team13api

def picturesToBeProcessed(dirName):
    currentFolderName = os.path.dirname(os.path.abspath(__file__))
    print(currentFolderName)
    imagePath = currentFolderName + dirName
    print(imagePath)
    try:
        if os.path.isdir(imagePath):
            fileNames = [f.path for f in os.scandir(imagePath)
                    if f.is_file() and f.path.endswith(('.png','.jpg'))
                ]
        return fileNames
    except Exception as e:
        print(dirName , " does not exits")
        return
    # if len(fileNames)>2:
    #     print("too many pictures in a single file")
    #     return


def dirList(directory):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    path = dir_path + directory
    folderName = [f.path for f in os.scandir(path) if f.is_dir]
    return folderName

def displayImages(images):
    nImageEachRow = int(math.sqrt(len(images)) + 1)
    nImageEachCol = len(images)//nImageEachRow + 1
    fig, ax = plt.subplots(nrows=nImageEachCol, ncols=nImageEachRow)
    flattenedAx = ax.flatten()
    for i in range(0, len(images)):
        flattenedAx[i].imshow(images[i])
    for i in flattenedAx:
        i.axis("off")

fileList = picturesToBeProcessed(r'/../data')
imagesTobeDisplayed = []

for f in fileList:
    processedImage = team13api.DisplayImageWithSkeleton(f)
    image = Image.fromarray(cv2.cvtColor(processedImage,cv2.COLOR_BGR2RGB))
    imagesTobeDisplayed.append(image)

displayImages(imagesTobeDisplayed)
plt.show()