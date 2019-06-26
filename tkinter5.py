from tkinter import *
root=Tk()
def right_click(event):
    print("hello this is right click ")
def left_click(event):
    print("hello this is left click")
def middle_click():
    print("hello this is middle click")
frame=Frame(root,height=100,width=200,bg="red")
frame.bind("<Button-1>",left_click)
frame.bind("<Button-2>",middle_click)
frame.bind("<Button-3>",right_click)
frame.pack()
root.mainloop()

