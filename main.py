from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=500)
window.config(padx=20, pady=20)

my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
# my_label.pack(side="left")
my_label.grid(row=0, column=0)

my_label["text"] = "New Text"
my_label.config(text="Power", padx=20, pady=20)


# Button


def button_clicked():
    print("I got clicked")
    new_text = input_st.get()
    my_label.config(text=new_text)


button = Button(text="Click Me", command=button_clicked)
button.grid(row=1, column=1)

new_button = Button(text="Click Me", command=button_clicked)
new_button.grid(row=0, column=2)

# Entry
input_st = Entry(width=10)
input_st.grid(row=3, column=3)

window.mainloop()
