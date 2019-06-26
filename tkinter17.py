from tkinter import *

def print_me():
    clicked_items=l.curselection()
    print(clicked_items)
    for items in clicked_items:
        print(l.get(items))

root=Tk()
l=Listbox(root,width=30,height=35,selectmode=MULTIPLE)
l.insert(1,"c++")
l.insert(2,"c")
l.insert(3,"html")
l.insert(4,"python")
l.pack()
button=Button(root, text="print",command=print_me)
button.pack()
root.geometry("400x400+120+120")
root.mainloop()