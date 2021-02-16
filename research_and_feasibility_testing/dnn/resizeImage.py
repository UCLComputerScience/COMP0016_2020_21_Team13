from PIL import Image 
import matplotlib.image as mpimg
from numpy import asarray

def resizeImage(f):
    frame = f.resize((512,512))
    frame=frame.convert("RGB")
    data = asarray(frame)
    return data


