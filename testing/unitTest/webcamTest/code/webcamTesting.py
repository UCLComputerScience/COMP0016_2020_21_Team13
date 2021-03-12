import os
import sys
import math
# from PIL import Image
import matplotlib.pyplot as plt

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(dir_path + r'/../../../../team13api');
import team13api

def picturesToBeProcessed(dirName):
    currentFolderName = os.path.dirname(os.path.abspath(__file__))
    imageFolderName = os.path.join(currentFolderName, dirName)
    try:
        if os.path.isdir(imageFolderName):
            fileNames = [f.path for f in os.scandir(imageFolderName)
                    if f.is_file() and f.path.endswith(('.png','.jpg'))
                ]
    except Exception as e:
        print(dirName , " does not exits")
    if len(fileNames)>2:
        print("too many pictures in a single file")
        return
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
folderList = dirList(r'/../data')
score = []
combinedSkeleton = []

for f in folderList:
    # score.append(Scoring(f[0],f[1]))
    fileNames = picturesToBeProcessed(f)
    result,canvas = team13api.compareWITHmodel(fileNames[0])
    print(type(canvas))
    score.append(result)
    combinedSkeleton.append(canvas)

displayImages(combinedSkeleton,score)
plt.show()