from tkinter import *

def do():
    print(" do this")
root=Tk()
main_menu=Menu(root)
root.config(menu=main_menu)
file_menu=Menu(main_menu)
main_menu.add_cascade(label="file",menu=file_menu)
edit_menu=Menu(main_menu)
main_menu.add_cascade(label="edit",menu="edit_menu")
view_menu=Menu(main_menu)
main_menu.add_cascade(label="view",menu="view_menu")
file_menu.add_command(label="new project",command=do)
save_menu=Menu(file_menu)
file_menu.add_cascade(label="save file",menu="save_menu")
save_menu.add_command(label=" save and next",command=do)
view_menu.add_command(label="tool window",command=do)
mainloop()