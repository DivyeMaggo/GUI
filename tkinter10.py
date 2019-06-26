from tkinter import *
root=Tk()
canvas=Canvas(root,height=400,width=500,bg="blue")
canvas.pack()
"""line=canvas.create_line((0,0,300,100),fill="red")
n_line=canvas.create_line((300,100,200,0),fill="pink")
ARc=canvas.create_arc(100,300,200,100,extent=120)# starting and ending point the angle form is of 90 if want to chnge 90 by other use extend
root.geometry("400x400+120+120")"""

canvas=canvas.create_rectangle(100,100,250,250,fill="red",outline="yellow")
points=[200,200,100,130,220,400,239,222]
canvas.create_polygon(points,fill="red")
"""canvas=canvas.create_oval(100,100,250,250 )#not working line"""
root.mainloop()