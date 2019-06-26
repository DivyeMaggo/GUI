from tkinter import *
from tkinter.ttk import Combobox
def printing():
    value=com.get()
    print(value)
root=Tk()
va=["c++","c","python","html","java","sql"]
com=Combobox(root,value=va)
com.set("select")
com.pack()
button=Button(root,text="print",command=printing)
button.pack()
root.mainloop()