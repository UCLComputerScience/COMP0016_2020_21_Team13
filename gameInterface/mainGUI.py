
from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.geometry("1000x1000")
frame = Frame(root)
frame.pack()

leftframe = LabelFrame(root)
leftframe.pack(side = LEFT)

rightframe = Frame(root)
rightframe.pack(side = RIGHT)

rightTOPframe = LabelFrame(rightframe,text="Next Move", relief=RIDGE)
rightTOPframe.pack(side=TOP)

rightBOtframe = LabelFrame(rightframe,text="Combine Together", relief=RIDGE)
rightBOtframe.pack(side=BOTTOM)

load = Image.open(r'D:\danceGame\openpose\examples\media\IMAGE1.jpg')
load = load.resize((550,680))
model_img = ImageTk.PhotoImage(load)

canvas = Canvas(leftframe,width= 550, height= 680)
canvas.pack()
canvas.create_image(0,0, anchor=NW, image=model_img) 

pictureOFuser = Canvas(rightTOPframe,bg='GREEN',width=450,height=340)
pictureOFuser.pack()

pictureOFcombine =Canvas(rightBOtframe,bg='RED',width=450,height=340)
pictureOFcombine.pack()

root.mainloop()