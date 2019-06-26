from tkinter import *
def call_me():
    print(i.get())
root=Tk()
#i=IntVar()
i=StringVar()
#c=Checkbutton(root,text="item",variable=i)
c=Checkbutton(root,text="item",variable=i,offvalue="checked",onvalue="checked")
c.pack()
button=Button(root,text="click me",command=call_me)
button.pack()
i.set(1)
root.mainloop()
