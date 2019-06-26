from tkinter import *
root=Tk()
l=Listbox(root,height=12,width=10,selectmode=MULTIPLE)#single,browse
l.insert(1,"python")
l.insert (2,"c")
l.insert(3,"c++")
l.insert (4,"c#")
l.pack()
root.mainloop()
