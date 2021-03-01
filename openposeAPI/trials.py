from displayHelper import displayImage
import api
import cv2
import matplotlib.pyplot as plt
# print(Scoring(r"D:\openpose\examples\media\Dance.jpg",r"D:\openpose\examples\media\Dance2.png"))
# twoSkeleton(r"D:\openpose\examples\media\Dance.jpg",r"D:\openpose\examples\media\Dance2.png")
# draw_skeleton(r"D:\openpose\examples\media\IMAGE2.jpg",False)
# datum = processImage(r"D:\openpose\examples\media\IMAGE2.jpg")
# print(datum.poseKeypoints)
# DisplayImageWithSkeleton(r"D:\openpose\examples\media\IMAGE2.jpg")
# print(Keypoints(r"D:\openpose\examples\media\IMAGE2.jpg",True))
# img = cv2.imread(r"D:\openpose\examples\media\IMAGE2.jpg")
# print(type(img))
api.draw_skeleton(r'D:\openpose_re\openpose\examples\media\Dance.jpg',True)