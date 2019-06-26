from tkinter import *

def call_me():
    #t=text.get(1.0,END)
   """ t=text.selection_get()
    ss=text.search(t,1.0,stopindex=END)"""
    t=text.delete(1.0,END)


    #print(ss)
   # print(t)
root=Tk()

text=Text(root,width=20,height=11,wrap=WORD,padx=10,pady=10,bd=5,selectbackground="blue")
text.config(font="itlalic")
text.pack()
text.insert(INSERT,"hello")

#button=Button(root,text="print",command=call_me)
button=Button(root,text="clear",command=call_me)
button.pack()

root.mainloop()