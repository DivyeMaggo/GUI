from tkinter import *
root=Tk()
"""def call_me():
    print("i am called")
button=Button(root,text="click me",command=call_me)
button.pack()
root.mainloop()
"""
def call_me(event):
    print("i am parul")

button=Button(root,text="click me")
button.bind("<Button-1>",call_me)
button.pack()
root.mainloop()

