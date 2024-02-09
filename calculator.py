from tkinter import *

def text_add(value):
    current_text = label.cget("text")

    if value == "C":
        label.config(text="")
    else:
        label.config(text=current_text + str(value))

root = Tk()
root.geometry("300x600")

label = Label(root, text="", font=("Arial", 20, "bold"))
label.grid(row=0, column=0, columnspan=4)

buttons = (
    (1, 0, "7"), (1, 1, "8"), (1, 2, "9"), (1, 3, "/"),
    (2, 0, "4"), (2, 1, "5"), (2, 2, "6"), (2, 3, "*"),
    (3, 0, "1"), (3, 1, "2"), (3, 2, "3"), (3, 3, "-"),
    (4, 0, "0"), (4, 1, "."), (4, 2, "C"), (4, 3, "+"),
)

for i in buttons:
    b = Button(root, text=i[2], font=("Arial", 20, "bold"), command=lambda value=i[2]: text_add(value))
    b.grid(row=i[0], column=i[1], padx=5, pady=5)

root.mainloop()