# Setting up section
import sys
import cv2
import os
import numpy as np
from sys import platform

from numpy.core.defchararray import endswith
from directoryHelper import mkdirForNpyFile, picturesToBeProcessed
import displayHelper
import scoringHelper
from datumClass import datumClass



dir_path = os.path.dirname(os.path.realpath(__file__))
try:
    # Windows Import
    if platform == "win32":
        # Change these variables to point to the correct folder (Release/x64 etc.)
        sys.path.append(dir_path + r'/../../openpose/build/python/openpose/Release');
        os.environ['PATH']  = os.environ['PATH'] + ';' + dir_path + r'/../../openpose/build/x64/Release;' +  dir_path + r'/../../openpose/build/bin;'
        import pyopenpose as op
    else:
        # Change these variables to point to the correct folder (Release/x64 etc.)
        sys.path.append('../../python');
        # If you run `make install` (default path is `/usr/local/python` for Ubuntu), you can also access the OpenPose/python module from there. This will install OpenPose and the python library at your desired installation path. Ensure that this is in your python path in order to use it.
        # sys.path.append('/usr/local/python')
        from openpose import pyopenpose as op
except ImportError as e:
    print('Error: OpenPose library could not be found. Did you enable `BUILD_PYTHON` in CMake and have this Python script in the right folder?')
    raise e

params = dict()
params["model_folder"] = "/../../../openpose/models/"

def processImage(image_source):
    if (isinstance(image_source,np.ndarray)):
        image_source = np.array(image_source)
        imageToProcess = image_source
        imageToProcess =cv2.resize(imageToProcess, (400, 400), interpolation=cv2.INTER_CUBIC)
    elif image_source.endswith('.npz'):
        if not os.path.isfile(image_source):
            print("file does not exists, please try agian")
            return        
        datumclass = loadNpy(image_source)
        return datumclass
    elif image_source.endswith('.jpg') or image_source.endswith('.png'):
        if not os.path.isfile(image_source):
            print("file does not exists, please try agian")
            return
        imageToProcess = cv2.imread(image_source)
        print(type(imageToProcess))
        imageToProcess =cv2.resize(imageToProcess, (400, 400), interpolation=cv2.INTER_CUBIC)
    opWrapper = op.WrapperPython()
    opWrapper.configure(params)
    opWrapper.start()
    datum = op.Datum()
    datum.cvInputData = imageToProcess
    opWrapper.emplaceAndPop(op.VectorDatum([datum]))
    print(type(datum))
    return datum

def loadNpy(npy_dir):
    npy = np.load(npy_dir)
    datum = datumClass(npy['arr_0'],npy['arr_1'])
    return datum



# API functions
def draw_skeleton(img_dir,bool):
    datum = processImage(img_dir)
    array = displayHelper.keypointsTuple(datum.poseKeypoints)
    width, height = displayHelper.getSize(datum.cvOutputData.shape)
    canvas = displayHelper.init_canvas(height,width)
    if(bool == False):
        canvas = displayHelper.kponly(canvas,array)
        return canvas
    else:
        canvas = displayHelper.kponly(canvas,array)
        canvas = displayHelper.addingLine(canvas, array)
        return canvas

def DisplayImageWithSkeleton(img_dir):
    datum = processImage(img_dir)
    return datum.cvOutputData

def Keypoints(img_dir,bool):
    datum = processImage(img_dir)
    if(bool == True):
        return displayHelper.keypointsTuple(datum.poseKeypoints)
    else:
        return scoringHelper.keypointsArray(datum.poseKeypoints)

def twoSkeleton(model_dir,input_dir):
    model_datum = processImage(model_dir)
    input_datum = processImage(input_dir)
    canvas = displayHelper.combineSkele(model_datum,input_datum)
    displayHelper.displayImage("two skeleton",canvas)



def Scoring(model_dir,input_dir):
    model_datum = processImage(model_dir)
    input_datum = processImage(input_dir)
    return scoringHelper.final_score(model_datum,input_datum)

def scoreANDskele(model_dir,input_dir):
    model_datum = processImage(model_dir)
    input_datum = processImage(input_dir)    
    score = scoringHelper.final_score(model_datum,input_datum)
    canvas = displayHelper.combineSkele(model_datum,input_datum)
    return score,canvas

def compareWITHmodel(model_dir,userImage):
    model_datum = processImage(model_dir)
    input_datum = processImage(userImage)
    # print(type(input_datum.poseKeypoints))
    if input_datum.poseKeypoints is None:
        print("did not detect any one in the frame")
        canvas = None
        score = 0
        return score, canvas, False    
    score = scoringHelper.final_score(model_datum,input_datum)
    combinedSkeleton = displayHelper.combineSkele(model_datum,input_datum)
    return score,combinedSkeleton, True
        
        



























# Unused
# def afterTransformed(model_dir,input_dir):
    # modelDatum = _processImage(model_dir)
    # inputDatum = _processImage(input_dir)
    # keypointMod = np.array(keypointsArray(modelDatum.poseKeypoints))
    # keypointInp = np.array(keypointsArray(inputDatum.poseKeypoints))
    # result = input_transform(keypointMod,keypointInp)
    # # print(result)
    # width, height = getSize(modelDatum.cvOutputData.shape)
    # canvas = init_canvas(height,width)
    # canvas = kponly(canvas,keypointMod)
    # canvas = addingLine(canvas,keypointMod)
    # canvas = kponly(canvas,keypointInp)
    # canvas = addingLine(canvas,keypointInp,[122,122,122])
    # canvas = kponly(canvas,result)
    # canvas = addingLine(canvas,result)
    # canvas = kponly(canvas,keypointMod)
    # canvas = addingLine(canvas,keypointMod,[122,122,122])
    # displayImage("skeleton after tansformation",canvas)