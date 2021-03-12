import os
import sys
import numpy as np

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(dir_path + r'/../team13api');
import team13api
import directoryHelper

dir = dir_path + r"\input"

def preprocessImages(folder_dir):
    listOFimage = directoryHelper.picturesToBeProcessed(folder_dir)
    npyFileDir = directoryHelper.mkdirForNpyFile(folder_dir)
    datum = team13api.processImage(listOFimage[0])
    poseKeypoints = datum.poseKeypoints
    cvOutputData = datum.cvOutputData

    for i in listOFimage:
        name = os.path.basename(i[0:-4])
        npyFileName = npyFileDir + "\\" +name
        datum = team13api.processImage(i)
        poseKeypoints = datum.poseKeypoints
        cvOutputData = datum.cvOutputData
        np.savez(npyFileName, poseKeypoints, cvOutputData)

if os.path.isdir(dir):
    preprocessImages(dir)