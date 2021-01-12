from PIL import Image 
import matplotlib.image as mpimg
from numpy import asarray

def resizeImage(f):
    frame = f.resize((513,513))
    data = asarray(frame)
    return data


path = 'C:\\Users\\84587\\Desktop\\YearTwo\\COMP0016\\COMP0016_2020_21_Team13\\research_and_feasibility_testing\\OpenPose\\images\\TestingImage.jpg'

f = Image.open(path)
if f.size != (513,513):
    frame = resizeImage(f)
    print(frame.shape)
# print(f.size)
# frame = resizeImage(f)
# print(frame.shape)
# frame = Image.fromarray(frame)
# frame.show()