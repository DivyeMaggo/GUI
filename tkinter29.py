from tkinter import *
from tkinter import filedialog
def file():
    res=filedialog.asksaveasfile(mode='w',defaultextension=".txt")
    if file is None:
        return
    else:
        res.write("hello how are you ?")
root=Tk()
button=Button(root,text="save as",command=file)
button.pack()
root.mainloop()