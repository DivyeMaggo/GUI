#shortkeys
from tkinter import *
from tkinter import messagebox
def call_me(event=""):
    messagebox.showinfo(" trying","something imp")

root=Tk()
root.bind('<Control-c>',call_me)
button=Button(root,text="call me",command=call_me)
button.pack()
root.geometry("300x300")
root.mainloop()