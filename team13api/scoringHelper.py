import numpy as np
import math
from numpy.core.fromnumeric import size
from numpy.lib.function_base import average
from opInfo import PartPairs

def keypointsArray(datum):
    result = []
    size = datum.shape[1]
    for i in range(0,size):
        point = [datum[0][i][0],datum[0][i][1]]
        result.append(point)
    return result

def vectorCosineSim(x, y, norm=False):
    assert len(x) == len(y), "len(x) != len(y)"
    zero_list = np.array([0] * len(x))
    if x.all() == zero_list.all() or y.all() == zero_list.all():
        return float(1) if x.all() == y.all() else float(0)
    res = np.array([[x[i] * y[i], x[i] * x[i], y[i] * y[i]] for i in range(len(x))])
    cos = sum(res[:, 0]) / (np.sqrt(sum(res[:, 1])) * np.sqrt(sum(res[:, 2])))
    return 0.5 * cos + 0.5 if norm else cos
    # method 1
    

    # method 2
    # cos = bit_product_sum(x, y) / (np.sqrt(bit_product_sum(x, x)) * np.sqrt(bit_product_sum(y, y)))

    # method 3
    # dot_product, square_sum_x, square_sum_y = 0, 0, 0
    # for i in range(len(x)):
    #     dot_product += x[i] * y[i]
    #     square_sum_x += x[i] * x[i]
    #     square_sum_y += y[i] * y[i]
    # cos = dot_product / (np.sqrt(square_sum_x) * np.sqrt(square_sum_y))


def getVectors(datum):
    if hasattr(datum,'poseKeypoints'):
        kp = keypointsArray(datum.poseKeypoints)
    else:
        kp = datum
    vectors = []
    for i in range(0,len(PartPairs)):
        p1 = PartPairs[i][0]
        p2 = PartPairs[i][1]
        x = abs(kp[p1][0]-kp[p2][0])
        y = abs(kp[p1][1]-kp[p2][1])
        vectors.append([x,y])
    return np.array(vectors)

def imagesCosineSim(mod_datum,input_datum):
    vec_mod = getVectors(mod_datum)
    vec_inp = getVectors(input_datum)
    result = []
    for i in range(0,len(vec_mod)):
        res = vectorCosineSim(vec_mod[i],vec_inp[i])
        result.append(res)
    return average(result)

def input_transform(model_features,input_features): #x as the keep points of the input image and y as the model image
    # see details at https://becominghuman.ai/single-pose-comparison-a-fun-application-using-human-pose-estimation-part-2-4fd16a8bf0d3
    pad = lambda x : np.hstack([x, np.ones((x.shape[0],1))])
    unpad = lambda x : x[:,:-1]

    Y = pad(model_features)
    X = pad(input_features)

    A, res, rank, s = np.linalg.lstsq(X,Y)
    A[np.abs(A) < 1e-10] = 0  # set really small values to zero
    transform = lambda x : unpad(np.dot(pad(x),A))
    input_transform = transform(input_features)
    return input_transform

def cosine_sim_score(mod_datum,input_datum):
    similarity = imagesCosineSim(mod_datum,input_datum)
    score = 0.5*math.pow((1-similarity)*100,2)
    if score > 90:
        score = 90
    score = round(score,2)
    return score

def similarityScore(mod_datum,input_datum):
    return 100 - cosine_sim_score(mod_datum,input_datum)
