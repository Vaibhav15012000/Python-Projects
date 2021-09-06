from tkinter import *
from tkinter.font import BOLD
import tkinter.messagebox as tmsg

root = Tk()


def click(event):
    try:
        global screen_value
        text = event.widget.cget("text")

        if text == "=":

            if screen_value.get().isdigit():

                value = int(screen_value.get())

            else:

                value = eval(screen.get())

            screen_value.set(value)
            screen.update()

        elif text == "C":

            screen_value.set("")
            screen.update()

        else:

            screen_value.set(screen_value.get()+text)
            screen.update()

    except Exception as e:
        tmsg.showinfo("Calculator", 'Invalid Operation')


def showInfo():
    tmsg.showinfo(
        "Calculator", "This calculator is made by Vaibhav Dubey.\nHope you like it :)")


try:
    root.geometry("280x376")
    root.title("Calculator")
    # root.wm_iconbitmap("calculator.ico")
    root.configure(background='gray32')
    root.maxsize(280, 376)
    root.minsize(280, 376)

    screen_value2 = " Welcome User :) "
    label1 = Label(root, text=screen_value2, font=(
        "lucida", 15, BOLD), relief=FLAT, background="light sky blue", borderwidth=2)
    label1.place(height=50, width=10)
    label1.pack(fill=X)
    Button(label1, text="info", font=('lucida', 10, BOLD),
           command=showInfo, relief=FLAT).pack(side=RIGHT)

    screen_value = StringVar()
    screen_value.set("")
    screen = Entry(root, textvariable=screen_value,
                   font=("lucida", 25), relief=FLAT)
    screen.pack(fill=X, pady=2)

    frame1 = Frame(root, background='gray32')

    button9 = Button(
        frame1, text='9', padx=10, pady=7, font=("lucida", 17, BOLD), relief=FLAT
    )
    button9.pack(
        side=LEFT, padx=7, pady=7
    )
    button9.bind(
        "<Button-1>", click
    )

    button8 = Button(
        frame1, text='8', padx=10, pady=7, font=("lucida", 17, BOLD), relief=FLAT
    )
    button8.pack(
        side=LEFT, padx=7, pady=7
    )
    button8.bind(
        "<Button-1>", click
    )

    button7 = Button(
        frame1, text='7', padx=10, pady=7, font=("lucida", 17, BOLD), relief=FLAT
    )
    button7.pack(
        side=LEFT, padx=7, pady=7
    )
    button7.bind(
        "<Button-1>", click
    )

    buttonc = Button(
        frame1, text='C', padx=10, pady=7, font=("lucida", 15, BOLD), relief=FLAT
    )
    buttonc.pack(
        side=LEFT, padx=7, pady=7
    )
    buttonc.bind(
        "<Button-1>", click
    )

    frame1.pack(anchor="s")

    # ______________________________________________________________________________________

    frame2 = Frame(root, background='gray32')

    button6 = Button(
        frame2, text='6', padx=10, pady=7, font=("lucida", 17, BOLD), relief=FLAT
    )
    button6.pack(
        side=LEFT, padx=7, pady=7
    )
    button6.bind(
        "<Button-1>", click
    )

    button5 = Button(
        frame2, text='5', padx=10, pady=7, font=("lucida", 17, BOLD), relief=FLAT
    )
    button5.pack(
        side=LEFT, padx=7, pady=7
    )
    button5.bind(
        "<Button-1>", click
    )

    button4 = Button(
        frame2, text='4', padx=10, pady=7, font=("lucida", 17, BOLD), relief=FLAT
    )
    button4.pack(
        side=LEFT, padx=7, pady=7
    )
    button4.bind(
        "<Button-1>", click
    )

    button_multiply = Button(
        frame2, text='*', padx=10, pady=7, font=("lucida", 17, BOLD), relief=FLAT
    )

    button_multiply.pack(
        side=LEFT, padx=7, pady=7
    )
    button_multiply.bind(
        "<Button-1>", click
    )

    frame2.pack(anchor="s")

    # ______________________________________________________________________________________

    frame3 = Frame(root, background='gray32')

    button3 = Button(
        frame3, text='3', padx=10, pady=7, font=("lucida", 17, BOLD), relief=FLAT
    )
    button3.pack(
        side=LEFT, padx=7, pady=7
    )
    button3.bind(
        "<Button-1>", click
    )

    button2 = Button(
        frame3, text='2', padx=10, pady=7, font=("lucida", 17, BOLD), relief=FLAT
    )
    button2.pack(
        side=LEFT, padx=7, pady=7
    )
    button2.bind(
        "<Button-1>", click
    )

    button1 = Button(
        frame3, text='1', padx=10, pady=7, font=("lucida", 17, BOLD), relief=FLAT
    )
    button1.pack(
        side=LEFT, padx=7, pady=7
    )
    button1.bind(
        "<Button-1>", click
    )

    button_divide = Button(
        frame3, text='/', padx=10, pady=7, font=("lucida", 17, BOLD), relief=FLAT
    )
    button_divide.pack(
        side=LEFT, padx=7, pady=7
    )
    button_divide.bind(
        "<Button-1>", click
    )

    frame3.pack(anchor="s")

    # ____________________________________________________________________________________

    frame4 = Frame(root, background='gray32')

    button0 = Button(
        frame4, text='0', padx=10, pady=7, font=("lucida", 17, BOLD), relief=FLAT
    )
    button0.pack(
        side=LEFT, padx=7, pady=7
    )
    button0.bind(
        "<Button-1>", click
    )

    button_add = Button(
        frame4, text='+', padx=10, pady=7, font=("lucida", 17, BOLD), relief=FLAT
    )
    button_add.pack(
        side=LEFT, padx=7, pady=7
    )
    button_add.bind(
        "<Button-1>", click
    )

    button_sub = Button(
        frame4, text='-', padx=10, pady=7, font=("lucida", 17, BOLD), relief=FLAT
    )
    button_sub.pack(
        side=LEFT, padx=7, pady=7
    )
    button_sub.bind(
        "<Button-1>", click
    )

    button_equal = Button(
        frame4, text='=', padx=10, pady=7, font=("lucida", 17, BOLD), relief=FLAT
    )
    button_equal.pack(
        side=LEFT, padx=7, pady=7
    )
    button_equal.bind(
        "<Button-1>", click
    )

    frame4.pack(anchor="s")

except Exception as e:
    tmsg.showinfo(
        "Calculator", "Something went wrong :(\nPlease restart the application.")

root.mainloop()