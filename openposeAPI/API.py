# Setting up section
import sys
import cv2
import os
from sys import platform
import argparse
from displayHelper import *
from scoringHelper import *

#TODO:
# refactoring code
# use a different transform algorithm
# alter from cosine similarity to Euclidean Distance

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

def _setup(image_dir):
    parser = argparse.ArgumentParser()
    if os.path.exists(image_dir) and os.path.isfile(image_dir):
        parser.add_argument("--image_path", default = image_dir, help="Process an image. Read all standard formats (jpg, png, bmp, etc.).")
        args = parser.parse_known_args()
        params = dict()
        params["model_folder"] = "/../openpose/models/"

        # Add others in path?
        for i in range(0, len(args[1])):
            curr_item = args[1][i]
            if i != len(args[1])-1: next_item = args[1][i+1]
            else: next_item = "1"
            if "--" in curr_item and "--" in next_item:
                key = curr_item.replace('-','')
                if key not in params:  params[key] = "1"
            elif "--" in curr_item and "--" not in next_item:
                key = curr_item.replace('-','')
                if key not in params: params[key] = next_item
        return args,params

def processImage(image_dir):
    # import image and model
    args,params = _setup(image_dir)
    # Starting OpenPose
    opWrapper = op.WrapperPython()
    opWrapper.configure(params)
    opWrapper.start()

    # Process Image
    datum = op.Datum()
    imageToProcess = cv2.imread(args[0].image_path)
    imageToProcess =cv2.resize(imageToProcess, (400, 400), interpolation=cv2.INTER_CUBIC)
    datum.cvInputData = imageToProcess
    opWrapper.emplaceAndPop(op.VectorDatum([datum]))
    return datum





# API functions
def draw_skeleton(img_dir,bool):
    datum = processImage(img_dir)
    array = keypointsTuple(datum.poseKeypoints)
    width, height = getSize(datum.cvOutputData.shape)
    canvas = init_canvas(height,width)
    if(bool == False):
        canvas = kponly(canvas,array)
        displayImage("keypoints of the skeleton",canvas)
    else:
        canvas = kponly(canvas,array)
        canvas = addingLine(canvas, array)
        displayImage("keypoints of the skeleton",canvas)

def DisplayImageWithSkeleton(img_dir):
    datum = processImage(img_dir)
    displayImage("Image with skeleton added to the input picture",datum.cvOutputData)

def Keypoints(img_dir,bool):
    datum = processImage(img_dir)
    if(bool == True):
        return keypointsTuple(datum.poseKeypoints)
    else:
        return keypointsArray(datum.poseKeypoints)

def twoSkeleton(model_datum,input_datum):
    # model_datum = processImage(model_dir)
    # input_datum = processImage(input_dir)
    return combineSkele(model_datum,input_datum)


def Scoring(model_datum,input_datum):
    # model_datum = processImage(model_dir)
    # input_datum = processImage(input_dir)
    return final_score(model_datum,input_datum)

def scoreANDskele(model_dir,input_dir):
    model_datum = processImage(model_dir)
    input_datum = processImage(input_dir)    
    score = final_score(model_datum,input_datum)
    canvas = combineSkele(model_datum,input_datum)
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