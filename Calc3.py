from tkinter import *
from tkinter import ttk
import tkinter.messagebox as tmsg
root = Tk()
root.geometry("850x569")
root.wm_iconbitmap("Calculator icon.ico")
root.title("Calculator by Vaibhav Dubey")
separator = ttk.Separator(root, orient='vertical')
separator.place(relx=0.64, rely=0, relwidth=0.2, relheight=1)
listbox= Listbox(root, relief=FLAT, width=34, height=27)
listbox.insert(END, "")
listbox.place(relx=0.7, rely=0.1)
def click(event):
    global entvar
    text= event.widget.cget("text")
    if text=="=":
        if entvar.get().isdigit():
            value= int(entvar.get())
        else:
            try:
                value= eval(entvar.get())
            except Exception as e:
                value="Error"
                tmsg.showerror()
        entvar.set(value)
        listbox.insert(ACTIVE, value)
        screen.update()
    elif text=="AC":
        entvar.set("")
        screen.update()
    elif text=="^2":
        value=str(int(entvar.get())**2)
        entvar.set(value)
        screen.update()
    else:
        entvar.set(entvar.get()+text)


buttonlist= ["/","7", "8","9", "*", "%", "4", "5", "6", "-","^2", "1", "2", "3", "AC", "0", ".", "="]
entvar= StringVar()
entvar.set("")
screen= Entry(root, textvariable=entvar, font="Lucida 30 bold" )
screen.pack(side=TOP, anchor="nw", pady=30, padx=25, ipadx=25, ipady=25)
f= Frame(root)
f2= Frame(root)
f3= Frame(root)
f4= Frame(root)
label2= Label(root, text= "History", font="Lucida 15 bold")
label2.place(relx=0.7, rely=0.05, anchor="nw")
for i in range(0, 5):
    b= Button(f, text=buttonlist[i], font="Lucida 20 bold", padx=15, pady=15)
    b.bind("<Button-1>", click)
    b.pack(side= LEFT,anchor= "nw", padx=20, pady=10)
for i in range(5, 10):
    b2= Button(f2, text=buttonlist[i], font="Lucida 20 bold", padx=15, pady=15)
    b2.bind("<Button-1>", click)
    b2.pack(side= LEFT,anchor= "nw", padx=17, pady=10)
    
for i in range(10, 14):
    b3= Button(f3, text=buttonlist[i], font="Lucida 20 bold", padx=15, pady=15)
    b3.bind("<Button-1>", click)
    b3.pack(side= LEFT ,anchor= "nw",padx=15, pady=10)
    
for i in range(14, 18):
    if i==14:
        b4= Button(f4, text=buttonlist[i], font="Lucida 20 bold", padx=15, pady=15, fg="white",bg="red")
        b4.bind("<Button-1>", click)
        b4.pack( side=LEFT,anchor= "nw", padx=15, pady=15)
    
    else:
        b4= Button(f4, text=buttonlist[i], font="Lucida 20 bold", padx=15, pady=15)
        b4.bind("<Button-1>", click)
        b4.pack( side=LEFT,anchor= "nw", padx=15, pady=15)
b= Button(root, text="+", font="Lucida 20 bold", padx=15, pady=15)
b.bind("<Button-1>", click)
b.place(relx=0.51, rely=0.67, height=175)
f.pack(anchor="nw")
f2.pack(anchor="nw")
f3.pack(anchor="nw")
f4.pack(anchor="nw")

root.mainloop()