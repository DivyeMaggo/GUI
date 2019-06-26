from tkinter import *
from tkinter.font import Font
from tkinter import font #for font list
root=Tk()
fonts=list(font.families())
for i  in fonts:
    print(i)
"""my_font=Font( family="Times New Roman",size=19,weight="normal",slant="italic",underline=1,overstrike=1)#weight=bold
label=Label(root,text="label size has been increased ",font=my_font)
label.pack()"""
root.mainloop()

