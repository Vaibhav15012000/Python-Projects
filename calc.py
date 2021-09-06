from tkinter import *
root=Tk()

root.geometry("344x900")
# root.maxsize(344,900)
root.wm_iconbitmap("one.ico")
root.title("Calculator by Vaibhav")
scvalue=StringVar()
scvalue.set("")

def click(event):
    global scvalue
    text=event.widget.cget("text")
    # print(text)
    if text=="=":
        if scvalue.get().isdigit():
            value=int(scvalue.get())
        else:
            try:
                value=eval(screen.get())
            except Exception as e:
                print(e)
                value="Error"
                screen.update()

        scvalue.set(value)
        screen.update()


            

    elif text=="C":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get()+ text)
        screen.update()

        




screen=Entry(root,textvariable=scvalue,font="lucida 40 bold")
screen.pack(padx=10,fill=X,pady=10)


f1=Frame(root,bg="grey")
b1=Button(f1,text="9",padx=10,pady=10,font="lucida 25 bold")
b1.pack(side=LEFT,padx=10,pady=10)
b1.bind("<Button-1>",click)

b2=Button(f1,text="8",padx=10,pady=10,font="lucida 25 bold")
b2.pack(side=LEFT,padx=10,pady=10)
b2.bind("<Button-1>",click)

b3=Button(f1,text="7",padx=10,pady=10,font="lucida 25 bold")
b3.pack(side=LEFT,padx=10,pady=10)
b3.bind("<Button-1>",click)

f1.pack()

f1=Frame(root,bg="grey")
b1=Button(f1,text="6",padx=10,pady=10,font="lucida 25 bold")
b1.pack(side=LEFT,padx=10,pady=10)
b1.bind("<Button-1>",click)

b2=Button(f1,text="5",padx=10,pady=10,font="lucida 25 bold")
b2.pack(side=LEFT,padx=10,pady=10)
b2.bind("<Button-1>",click)

b3=Button(f1,text="4",padx=10,pady=10,font="lucida 25 bold")
b3.pack(side=LEFT,padx=10,pady=10)
b3.bind("<Button-1>",click)

f1.pack()

f1=Frame(root,bg="grey")
b1=Button(f1,text="3",padx=10,pady=10,font="lucida 25 bold")
b1.pack(side=LEFT,padx=10,pady=10)
b1.bind("<Button-1>",click)

b2=Button(f1,text="2",padx=10,pady=10,font="lucida 25 bold")
b2.pack(side=LEFT,padx=10,pady=10)
b2.bind("<Button-1>",click)

b3=Button(f1,text="1",padx=10,pady=10,font="lucida 25 bold")
b3.pack(side=LEFT,padx=10,pady=10)
b3.bind("<Button-1>",click)

f1.pack()

f1=Frame(root,bg="grey")
b1=Button(f1,text="=",padx=10,pady=10,font="lucida 25 bold")
b1.pack(side=LEFT,padx=8,pady=8)
b1.bind("<Button-1>",click)

b2=Button(f1,text="C",padx=10,pady=10,font="lucida 25 bold")
b2.pack(side=LEFT,padx=8,pady=8)
b2.bind("<Button-1>",click)

b3=Button(f1,text="+",padx=10,pady=10,font="lucida 25 bold")
b3.pack(side=LEFT,padx=8,pady=8)
b3.bind("<Button-1>",click)

f1.pack()

f1=Frame(root,bg="grey")
b1=Button(f1,text="*",padx=1,pady=10,font="lucida 25 bold")
b1.pack(side=LEFT,padx=13,pady=13)
b1.bind("<Button-1>",click)

b2=Button(f1,text="/",padx=10,pady=10,font="lucida 25 bold")
b2.pack(side=LEFT,padx=13,pady=13)
b2.bind("<Button-1>",click)

b3=Button(f1,text="%",padx=10,pady=10,font="lucida 25 bold")
b3.pack(side=LEFT,padx=13,pady=13)
b3.bind("<Button-1>",click)

f1.pack()

f1=Frame(root,bg="grey")
b1=Button(f1,text="-",padx=10,pady=10,font="lucida 25 bold")
b1.pack(side=LEFT,padx=9,pady=9)
b1.bind("<Button-1>",click)

b2=Button(f1,text=".",padx=10,pady=10,font="lucida 25 bold")
b2.pack(side=LEFT,padx=9,pady=9)
b2.bind("<Button-1>",click)

b3=Button(f1,text="00",padx=10,pady=10,font="lucida 25 bold")
b3.pack(side=LEFT,padx=9,pady=9)
b3.bind("<Button-1>",click)

f1.pack()















root.mainloop()