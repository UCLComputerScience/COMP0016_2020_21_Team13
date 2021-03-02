from tkinter import *

root = Tk()
root.geometry("150x150")

redframe = Frame(root, background="red", height = 100, width=50)
redframe.pack( side = LEFT)


blueframe = Frame(root, background="blue", height = 100, width=50)
blueframe.pack( side = LEFT)

greenframe = Frame(root, background="green", height = 100, width=50)
greenframe.pack( side = LEFT)

root.mainloop()
