from tkinter import *
root=Tk()
canvas=Canvas(root,width=200,height=100)
canvas.pack()
photo=PhotoImage(file="C://Users//vikram//Desktop//a.png")
canvas.create_image(20,20,image=photo,anchor=CENTER)#NW
root.mainloop()