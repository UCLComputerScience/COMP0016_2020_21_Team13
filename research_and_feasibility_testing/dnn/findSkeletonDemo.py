import skeletonRecognitionUtils as skltnUtil
import numpy as np
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
from PIL import Image
import resizeImage 
import math
import os
from numpy import asarray

def getAllImages(dirName):
    currentFolderName = os.path.dirname(os.path.abspath(__file__))
    imageFolderName = os.path.join(currentFolderName, dirName)
    fileNames = [f.path for f in os.scandir(imageFolderName)
            if f.is_file() and f.path.endswith(('.png','.jpg'))
        ]
    originFrames=[]
    skeletonFrames=[]
    for fileName in fileNames:
        frame = Image.open(fileName)
        if frame.size != (513,513):
            frame = resizeImage.resizeImage(frame)
        print(frame.shape)
        originFrames.append(frame)
        skeletonFrame = skltnUtil.findSkeleton(frame)
        skeletonFrames.append(skeletonFrame)
    return originFrames, skeletonFrames

def displayImages(images):
    nImageEachRow = math.isqrt(len(images)) + 1
    nImageEachCol = len(images)//nImageEachRow + 1
    fig, ax = plt.subplots(nrows=nImageEachCol, ncols=nImageEachRow)
    flattenedAx = ax.flatten()
    for i in range(0, len(images)):
        flattenedAx[i].imshow(images[i])
    for i in flattenedAx:
        i.axis("off")



originFrames, skeletonFrames = getAllImages('images')
displayImages(skeletonFrames)


plt.show()


