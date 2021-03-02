from tkinter import *  
from PIL import ImageTk,Image  

# print(load.size)
load = Image.open(r'D:\danceGame\openpose\examples\media\Dance.jpg')
imgSize = load.size
maxSize = max(imgSize)
minSize = min(imgSize)
root = Tk()  
canvas = Canvas(root, width = minSize, height = maxSize)  
canvas.pack()  
img = ImageTk.PhotoImage(load) 
canvas.create_image(20, 20, anchor=NW, image=img) 
root.mainloop()