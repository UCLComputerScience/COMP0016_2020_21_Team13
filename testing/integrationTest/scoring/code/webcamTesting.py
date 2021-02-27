import os
import sys
import cv2
# from PIL import Image
import matplotlib.pyplot as plt

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(dir_path + r'/../../../../openposeAPI');
from api import compareWITHmodel
from testing import dirList, displayImages, picturesToBeProcessed

folderList = dirList(r'/../webcamTesting')
score = []
combinedSkeleton = []

for f in folderList:
    # score.append(Scoring(f[0],f[1]))
    datumList=[]
    print(f)
    fileNames = picturesToBeProcessed(f,1)
    result,canvas = compareWITHmodel(fileNames[0])
    score.append(result)
    combinedSkeleton.append(canvas)

displayImages(combinedSkeleton,score)
plt.show()