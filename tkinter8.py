
from tkinter import *
from tkinter import messagebox
def call_me():
    messagebox.showinfo("success","installation complete")#showerror,showwarning

root=Tk()
b=Button(root,text="message",command=call_me)
b.pack()
root.geometry("400x400+120+120")
root.mainloop()