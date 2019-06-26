from tkinter import *
from tkinter import simpledialog
def call_me():
    s=simpledialog.askstring("input","please enter your name")
    text.insert(INSERT, s)
root=Tk()
button=Button(root,text="popup",command=call_me)
button.pack()
text=Text(root)
text.pack()
root.mainloop()