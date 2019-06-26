from tkinter import *
def call_me():
    if(i.get()==1):
        print("you are male")
    else:
        print("you are female")
root=Tk()
i=IntVar()
r1=Radiobutton(root,text="male",value=1,variable=i)
r2=Radiobutton(root,text="female",value=2,variable=i)
r1.pack()
r2.pack()
button=Button(root,text="click me",command=call_me)
button.pack()
root.mainloop()