#label frame
from tkinter import *
root=Tk()
label=LabelFrame(root,text="new frame " ,padx=5,pady=4)
label.pack()
button=Button(label,text="button")
button.pack()
root.geometry("300x300")
root.mainloop()