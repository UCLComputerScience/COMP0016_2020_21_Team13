from typing import Counter
from directoryRelatedAPI import *
from tkinter import *
import tkinter
import time
import sys
from PIL import ImageTk, Image
import cv2
from threading import *


dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(dir_path + r'/../team13api');
import team13api

# setting up webcam
width, height = 800, 600
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

def takeScreenshot():
    ref, frame = cap.read()
    return frame


def show_frame():
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    img = Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)
    video_panel.imgtk = imgtk
    video_panel.configure(image=imgtk)
    video_panel.after(10, show_frame)

def newThread(label):
    Thread(target =lambda : openposeCalculation(label)).start() 


def resizeImageToScale(image):
    imgSize = image.size
    scale = max(imgSize)/340
    newWidth = int(imgSize[0]/scale)
    newLength = int(imgSize[1]/scale)
    image = image.resize((newWidth,newLength))
    return image


picturesToBeDisplayed = picturesToBeProcessed(dir_path + r"/ImagesForTesting")
photoImageType = []
preprocessedImage = picturesToBeProcessed(dir_path+ r"/preprocessOutput")
skeletonImage_photoImageType= []

# function parts

def button_countdown(time_to_countdown, label):
    if time_to_countdown > 0:
        time_to_countdown -= 1
        label.set(time_to_countdown)
        root.after(1000, lambda: button_countdown(time_to_countdown, label))
    else:
        openposeCalculation(label)




def updateImage(photoImage,panel):
    panel.configure(image=photoImage)
    panel.image = photoImage

def updateScore():
    totalScoreLabel.configure(text = userScore)
    totalScoreLabel.text = userScore

def getUserScore(panel):
    global current
    userImage = takeScreenshot()
    model_img = preprocessedImage[current]
    if not scoreUserMove(model_img,panel,userImage):
        totalScoreLabel.configure(text = "Did not detect Player, try agian!")
        return FALSE
    return TRUE


def scoreUserMove(model_dir,panel,userImage):
    global userScore
    score,canvas, success = team13api.compareWITHmodel(model_dir,userImage)
    if not success:
        return False
    canvas = Image.fromarray(canvas)
    canvas = ImageTk.PhotoImage(canvas)
    updateImage(canvas,panel)
    userScore += score 
    updateScore()
    return True

current=0
userScore = 0
totalImage = len(preprocessedImage)
clicked = 0
def openposeCalculation(label):
    global userScore, current, totalImage, clicked
    if current < totalImage:
        next = current+1
        if clicked == 0:
            label.set("Click to Start")
            print("case 0")
            updateImage(skeletonImage_photoImageType[current],current_move_panel)
            updateImage(skeletonImage_photoImageType[next],nextMoveLabel)
            clicked += 1
        elif clicked ==1:
            label.set("Click Me")
            print("case 1")
            if not getUserScore(pictureOFcombine):
                return
            clicked +=1
            current += 1
            print(clicked , "  ",current)
            updateImage(skeletonImage_photoImageType[current],current_move_panel)
            updateImage(skeletonImage_photoImageType[next+1],nextMoveLabel)
        elif current+2 == totalImage:
            label.set("Last Image")
            print("case 2")
            print("current: ", current)
            if not getUserScore(pictureOFcombine):
                return
            current+=1
            updateImage(skeletonImage_photoImageType[current],current_move_panel)
            updateImage('',nextMoveLabel)
            print(current)
        elif current == totalImage:
            print("case 3")
            label.set("Finished")
            root.destroy()      
        else:
            label.set("Click Me")
            print("case 4")
            if not getUserScore(pictureOFcombine):
                return
            if current+1 == totalImage:
                print("current: ", current)
                time.sleep(5)
                label.set("Finished")
                root.destroy()
                return
            current+=1
            updateImage(skeletonImage_photoImageType[current],current_move_panel)
            if next +1 == totalImage:
                updateImage('',nextMoveLabel)
            else:
                updateImage(skeletonImage_photoImageType[next+1],nextMoveLabel)
            
    return

def positionOFpicture(image):
    imgSize = image.size
    imgWidth = imgSize[0]
    value = int((550-imgWidth)/2)
    return value

root = Tk()
root.geometry("1000x1000")
frame = LabelFrame(root,text="Game Interface",relief=RIDGE)
frame.pack()

leftFrame = Frame(root)
leftFrame.pack(side=LEFT)

leftTOPlabel = LabelFrame(leftFrame,text="Current Move", relief=RIDGE)
leftTOPlabel.pack(side = TOP)

leftBOTlabel = LabelFrame(leftFrame,text = "video", relief=RIDGE)
leftBOTlabel.pack(side=BOTTOM)



rightframe = Frame(root)
rightframe.pack(side = RIGHT)

rightTOPframe = LabelFrame(rightframe,text="Combine Skeleton and Score", relief=RIDGE)
rightTOPframe.pack(side=TOP)


rightBOtframe = LabelFrame(rightframe,text="Next Move", relief=RIDGE)
rightBOtframe.pack(side=BOTTOM)

totalScoreLabel = tkinter.Label(leftTOPlabel,text=userScore,bg = "RED", width = 30,relief=RIDGE)
totalScoreLabel.grid(row = 0,column=0)

# current_move_score = tkinter.Label(leftTOPlabel,text=userScore,bg = "Blue", width = 30,relief=RIDGE)
# totalScoreLabel.grid(row=0,column=1)

# right frame widgets
load = Image.open(picturesToBeDisplayed[0])
img = resizeImageToScale(load)
model_img = ImageTk.PhotoImage(img)
current_move_panel = tkinter.Label(leftTOPlabel, image=model_img, width= 550, height=340)
current_move_panel.grid(row=1)

video_panel = tkinter.Label(leftBOTlabel,width=550,height=340)
video_panel.grid(row=0)

# left frame widgets
pictureOFcombine = tkinter.Label(rightTOPframe,image=model_img,width=550,height=340)
pictureOFcombine.grid(row = 0)

nextMoveLabel =Label(rightBOtframe,image=model_img,width=550,height=340)
nextMoveLabel.grid(row=0)

for k in preprocessedImage:
    skele = team13api.draw_skeleton(k,True)
    skele = Image.fromarray(skele)
    skele = ImageTk.PhotoImage(skele)
    skeletonImage_photoImageType.append(skele)

for j in picturesToBeDisplayed:
    load = Image.open(j)
    img = resizeImageToScale(load)
    model_img = ImageTk.PhotoImage(img)
    photoImageType.append(model_img)

button_label = tkinter.StringVar()
button_label.set("Click to Start")
Counter = 5
tkinter.Button(rightTOPframe, textvariable=button_label,command=lambda : button_countdown(Counter,button_label)).grid(row=1)



show_frame()
root.mainloop()




