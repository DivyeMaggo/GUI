from tkinter import *
root=Tk()
frame=Frame(root)# because by using geometry the scrollabr and listbox are not coming with same align
frame.pack()
scroll=Scrollbar(frame)
scroll.pack(side=RIGHT,fill=Y)
listbox = Listbox(frame,yscrollcommand=scroll.set)
for i in range(1,100):
    listbox.insert(END,"list"+str(i))
listbox.pack(side=LEFT)
scroll.config(command=listbox.yview)
root.geometry("400x400")
root.mainloop()


