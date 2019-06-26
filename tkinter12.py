from tkinter import *
root=Tk()
#pack()
#grid()
#place()  : place at any position
root.geometry("400x400+120+120")
label=Label(root,text="label1",bg="pink")
label.place(x=120,y=300)
root.mainloop()