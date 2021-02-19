from API import *
import matplotlib.pyplot as plt
# print(Scoring(r"D:\openpose\examples\media\Dance.jpg",r"D:\openpose\examples\media\Dance2.png"))
plt.imshow(twoSkeleton(r"D:\openpose\examples\media\Dance.jpg",r"D:\openpose\examples\media\Dance2.png"))
plt.axis('off')
plt.show()
# draw_skeleton(r"D:\openpose\examples\media\IMAGE2.jpg",True)