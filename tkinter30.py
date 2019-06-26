from tkinter import *
from tkinter import colorchooser
def call_me():
    clr=colorchooser.askcolor(title="select color")
    print(clr)
    root.config(background=clr[1])
root=Tk()
button=Button(root,text="colorchoose",command=call_me)
button.pack()
root.geometry("300x300")
root.mainloop()
