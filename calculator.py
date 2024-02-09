from tkinter import *
import re


def text_add(value):
    current_text = label.cget("text")
    try:
        if value == "C":
            label.config(text="")
        elif value != "":
            label.config(text=str(current_text) + str(value))
        else:
            label.config(text="Error, No value entered, Or started with number 0")
    except ZeroDivisionError:
        label.config(text="Error, division by zero")


def Equel_to(): 
    current_text = label.cget("text")
    try:
        current_text = current_text = re.sub(r'\b0[0-7]+\b', lambda x: str(int(x.group(), 8)), current_text)
        label.config(text=eval(str(current_text)))
    except (ZeroDivisionError, SyntaxError):
        label.config(text="Error")


root = Tk()

root.config(bg="lightblue")
root.title("Calculator")

label = Label(root, text="", font=("Arial", 20, "bold"), bg="lightblue",relief=SOLID, borderwidth=1, pady=10,padx=25, width=10)
label.grid(row=0, column=0, columnspan=4)

buttons = (
    (1, 0, "7"), (1, 1, "8"), (1, 2, "9"), (1, 3, "/"),
    (2, 0, "4"), (2, 1, "5"), (2, 2, "6"), (2, 3, "*"),
    (3, 0, "1"), (3, 1, "2"), (3, 2, "3"), (3, 3, "-"),
    (4, 0, "0"), (4, 1, "C"), (4, 2, "."), (4, 3, "+"),
)

for i in buttons:
    calculator_buttons = Button(root, text=i[2], font=("Arial", 25, "bold",),relief=SOLID, borderwidth=1,  command=lambda value=i[2]: text_add(value))
    calculator_buttons.grid(row=i[0], column=i[1], padx=5, pady=5)

Equal_button = Button(root, text="=", font=("Arial", 20, "bold"), relief=SOLID, borderwidth=1, command=Equel_to, width=12, pady=5, padx=5)
Equal_button.grid(columnspan=4)

root.resizable = False
                      
root.mainloop()