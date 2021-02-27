# From Python
# It requires OpenCV installed for Python
import sys
import os
from sys import platform

#TODO:
# refactoring code
# use a different transform algorithm
# alter from cosine similarity to Euclidean Distance

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
def _matchingPairs():
    poseModel = op.PoseModel.BODY_25
    array = op.getPosePartPairs(poseModel)
    result = []
    i=0
    while(i<len(array)):
        pairs = []
        pairs.append(array[i])
        pairs.append(array[i+1])
        result.append(pairs)
        i +=2
    return result

# model info
poseModel = op.PoseModel.BODY_25
BodyPartNumber = op.getPoseBodyPartMapping(poseModel)
PartPairs = _matchingPairs()
poseMapIndex = op.getPoseMapIndex(poseModel)





# def _input_transform(model_features,input_features): #x as the keep points of the input image and y as the model image
#     # see details at https://becominghuman.ai/single-pose-comparison-a-fun-application-using-human-pose-estimation-part-2-4fd16a8bf0d3
#     pad = lambda x : np.hstack([x, np.ones((x.shape[0],1))])
#     unpad = lambda x : x[:,:-1]

#     Y = pad(model_features)
#     X = pad(input_features)

#     A, res, rank, s = np.linalg.lstsq(X,Y)
#     A[np.abs(A) < 1e-10] = 0  # set really small values to zero
#     transform = lambda x : unpad(np.dot(pad(x),A))
#     input_transform = transform(input_features)
#     return input_transform

# def transformedShape(model_dir,input_dir):
#     model, input = _process_two_images(model_dir,input_dir)
#     kpModel = _keepKP_list(model.poseKeypoints)
#     kpInput = _keepKP_list(input.poseKeypoints)
#     result = _input_transform(kpModel, kpInput)
#     vec_Mod = _getVectors(kpModel)
#     vec_Inp = _getVectors(result)
#     print(_cosSim(vec_Mod,vec_Inp))

#     img = _draw_two_sets_of_points_with_line(model,kpModel,result)
#     cv2.imshow("two sets of points combine together",img)
#     cv2.waitKey(0)    

# def beforeTransfor(model_dir, input_dir):
#     model, input = _process_two_images(model_dir,input_dir)
#     kpModel = _keepKP_list(model.poseKeypoints)
#     kpInput = _keepKP_list(input.poseKeypoints)
#     vec_Mod = _getVectors(kpModel)
#     vec_Inp = _getVectors(kpInput)
#     print(_cosSim(vec_Mod,vec_Inp))
#     img = _draw_two_sets_of_points_with_line(model,kpModel,kpInput)
#     cv2.imshow("two sets of points combine together",img)
#     cv2.waitKey(0)        