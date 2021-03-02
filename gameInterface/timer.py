import tkinter

def button_countdown(i, label):
    if i > 0:
        i -= 1
        label.set(i)
        root.after(1000, lambda: button_countdown(i, label))
    else:
        label.set("click me")
        window = tkinter.Toplevel(root)
        tkinter.Label(window, text="countdown finished").pack()

root = tkinter.Tk()

counter = 5
button_label = tkinter.StringVar()
button_label.set("click me")
tkinter.Button(root, textvariable=button_label, command=lambda:button_countdown(counter, button_label)).pack()

root.mainloop()
