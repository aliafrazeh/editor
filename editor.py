from tkinter import *


root = Tk()

root.title('Editor')
root.minsize(900,600)
root.maxsize(900,600)
root.config(bg="#FEFFCC")

def display_text():
    global entry,entry2
    lab_str = entry.get()
    file = open(lab_str,"a")
    lab_str2 = entry2.get("1.0",END)
    file.write(lab_str2)




label=Label(root,bg="#FEFFCC", text="file:", font=('calibre',20,'normal'))
label.pack()
entry = Entry(root,width=40,bg="#FCFFDD")
entry.focus_set()
entry.pack()

label=Label(root,bg="#FEFFCC", text="text:", font=('calibre',20,'normal'))
label.pack()
entry2 = Text(root,width=900,bg="#FCFFDD")
entry2.focus_set()
entry2.pack()
Button(root,bg="#e1ecff", text= "Save",width= 20, command= display_text).pack(pady=0)
root.mainloop()
