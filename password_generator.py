from tkinter import *
import random


chars = """"abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXY~`!@#$%^&*()_-+={[}]|\"':;<,>.?/"""

def retrieve():
    password_len = int(my_entry.get())
    password_count = int(my_entry2.get())

    for i in range(0, password_count):
       password = ""
       for i in range(0,password_len):
           password_char = random.choice(chars)
           password += password_char
       text.insert("1.0", password + "\n")
    text.insert("\n")
          
root = Tk()
root.geometry("640x480")
frame = Frame(root)
frame.pack()

text=Text(root, width=80, height=15)
text.insert(END, "")
text.pack()

var = StringVar()
var.set("Please enter the length you want your password(s) to be and how many passwords you would like")

label = Label(frame, textvariable = var )
label.pack()

my_entry = Entry(frame, width = 20)
my_entry.insert(0, 'Length')
my_entry.pack(padx = 5, pady = 5)

my_entry2 = Entry(frame, width = 20)
my_entry2.insert(0, 'How many')
my_entry2.pack(padx = 5, pady = 5)

Button = Button(frame, text = "Submit", command = retrieve)
Button.pack(padx = 5, pady = 5)

root.title("Password Generator")
root.mainloop()