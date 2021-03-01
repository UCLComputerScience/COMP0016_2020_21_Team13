# Setting up section
import sys
import cv2
import os
from sys import platform
import displayHelper
import scoringHelper



dir_path = os.path.dirname(os.path.realpath(__file__))
try:
    # Windows Import
    if platform == "win32":
        # Change these variables to point to the correct folder (Release/x64 etc.)
        sys.path.append(dir_path + r'/../openpose/build/python/openpose/Release');
        os.environ['PATH']  = os.environ['PATH'] + ';' + dir_path + r'/../openpose/build/x64/Release;' +  dir_path + r'/../openpose/build/bin;'
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
params["model_folder"] = "/../openpose/models/"

def processImage(image_source):
    opWrapper = op.WrapperPython()
    opWrapper.configure(params)
    opWrapper.start()

    datum = op.Datum()
    try:
        imageToProcess = cv2.imread(image_source)
        imageToProcess =cv2.resize(imageToProcess, (400, 400), interpolation=cv2.INTER_CUBIC)
    except:
        imageToProcess = image_source
        imageToProcess =cv2.resize(imageToProcess, (400, 400), interpolation=cv2.INTER_CUBIC)
    datum.cvInputData = imageToProcess
    opWrapper.emplaceAndPop(op.VectorDatum([datum]))
    return datum





# API functions
def draw_skeleton(img_dir,bool):
    datum = processImage(img_dir)
    array = displayHelper.keypointsTuple(datum.poseKeypoints)
    print(type(array))
    width, height = displayHelper.getSize(datum.cvOutputData.shape)
    canvas = displayHelper.init_canvas(height,width)
    if(bool == False):
        canvas = displayHelper.kponly(canvas,array)
        displayHelper.displayImage("keypoints of the skeleton",canvas)
    else:
        canvas = displayHelper.kponly(canvas,array)
        canvas = displayHelper.addingLine(canvas, array)
        displayHelper.displayImage("keypoints of the skeleton",canvas)

def DisplayImageWithSkeleton(img_dir):
    datum = processImage(img_dir)
    displayHelper.displayImage("Image with skeleton added to the input picture",datum.cvOutputData)

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

def compareWITHmodel(model_dir):
    webcamImage = displayHelper.takePic()
    model_datum = processImage(model_dir)
    input_datum = processImage(webcamImage)    
    score = scoringHelper.final_score(model_datum,input_datum)
    canvas = displayHelper.combineSkele(model_datum,input_datum)
    return score,canvas































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