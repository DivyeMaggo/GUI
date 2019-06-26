
#new window opening
from tkinter import *
def win():
    top=Toplevel()
    top.title("new window")
    top.geometry("200x200+300+120")
    but=Button(top,text="close",command=top.destroy)
    but.pack()
root=Tk()
button=Button(root,text="open window",command=win)
button .pack()
root.geometry("400x400")
root.mainloop()
