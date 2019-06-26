from tkinter import *
def call_me():
    s.set("hello")
    print(entry.get())#entry from user and print on click
root=Tk()
"""entry=Entry(root)
entry.pack()
button=Button(root,text="click me",command=call_me)"""
s=StringVar()
entry=Entry(root,textvariable=s)
s.set("hello")
entry.pack()
button=Button(root,text="click me",command=call_me)
button.pack()
root.mainloop()