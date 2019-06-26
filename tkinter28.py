from tkinter import *
from tkinter import filedialog
def openfile():
    result=filedialog.askopenfile(initialdir="E:/",title="select file",filetypes=(("text files",".txt"),("all files","*.*")))
    print(result)
    for c in result:
        print(c)


root=Tk()
button=Button(root,text="open file",command=openfile)
button.pack()
root.mainloop()