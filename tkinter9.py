from tkinter import *
from tkinter import messagebox
#user ans

def call_me():
    ans=messagebox.askquestion("exit","want to stay")#askyesnocancel
    if ans== 'yes':
        root.quit()
root=Tk()
b=Button(root,text="message",command=call_me)
b.pack()
root.geometry("400x400+120+120")
root.mainloop()
