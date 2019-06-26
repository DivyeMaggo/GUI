from tkinter import *
root=Tk()
labelone=Label(root,text="one",bg="red")
labeltwo=Label(root,text="two",bg="yellow")
labelthree=Label(root,text="three",bg="blue")
labelone.pack()
labeltwo.pack(fill=X)
labelthree.pack(side=LEFT,fill=Y)
root.mainloop()
#grid: for making the labels buttons etc in format row and coloumn wise
"""name=Label(root,text="name")
password=Label(root,text="password")
entry1=Entry(root)
entry2=Entry(root)
name.grid(row=0,column=0)#no need to add coloumn by default it will take col to be 0
entry1.grid(row=0,column=1)
password.grid(row=1,column=0)
entry2.grid(row=1,column=1)
c=Checkbutton(root,text=" make me login")
c.grid(columnspan=2)
root.mainloop()
"""
