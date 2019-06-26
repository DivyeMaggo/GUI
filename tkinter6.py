# for manage the root size
from tkinter import *
root=Tk()
"""root.geometry("300x150+155+200")
root.mainloop()
"""

class mybuttons:
    def __init__(self,master):
        self.button=Button(master,text="print",command=self.message)
        self.button.pack(side=LEFT)
        self.quitbutton=Button(master,text="quit",command=master.quit)
        self.quitbutton.pack(side=RIGHT)
    def message(self):
        print(" hello you print something")

root=Tk()
b=mybuttons(root)
root.mainloop()