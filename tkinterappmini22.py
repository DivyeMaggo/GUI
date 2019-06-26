from tkinter import *
import wikipedia
def text_me():
    t=entry.get()
    try:
        answer_value=wikipedia.summary(t)
        ans.delete(1.0,END)
        ans.insert(END,answer_value)
    except:
        ans.insert(INSERT,"plz check internet connection /input")

root=Tk()
frame=Frame(root)
entry=Entry(frame)
entry.pack()
button=Button(frame,text="search",command=text_me)
button.pack()
frame.pack(side=TOP)
bframe=Frame(root)
scroll=Scrollbar(bframe)
scroll.pack(side=RIGHT,fill=Y)
ans=Text(bframe,width=50,height=20,yscrollcommand=scroll.set,wrap=WORD)
scroll.config(command=ans.yview)
ans.pack()
bframe.pack()

root.mainloop()
