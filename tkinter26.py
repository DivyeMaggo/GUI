from tkinter import *
def call_me():
    s=spin.get()
    print(s)
root=Tk()
spin=Spinbox(root,from_=1,to=10)
spin.pack()
button=Button(root,text="print",command=call_me)
button.pack()
root.mainloop()