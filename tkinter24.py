from tkinter import *
def call_me():
    value=s.get()
    print(value)
root=Tk()
s=Scale(root,from_ = 0,to=100,orient=HORIZONTAL, length=200,width=10,sliderlength=50)#default vertical,slider lenght defaultt is 30
s.grid(row=0)
s.set(50)
button=Button(root,text="print",command=call_me)
button.grid(row=1)

s.mainloop()