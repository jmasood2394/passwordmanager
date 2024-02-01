from tkinter import *

from password_generator import generate_password
from find_password import find_password
from save_password import save_password


window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

# Canvas for Logo
canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=0, columnspan=3)

# Labels
website_label = Label(text="Website: ", font=("Arial", 12))
website_label.grid(sticky=E, row=1, column=0)

email_label = Label(text="Email/Username: ", font=("Arial", 12), pady=10)
email_label.grid(row=2, column=0)

password_label = Label(text="Password: ", font=("Arial", 12))
password_label.grid(sticky=E, row=3, column=0)

# Entry Fields
website_entry = Entry(width=24)
website_entry.insert(0, string="")
website_entry.grid(sticky=W, row=1, column=1)
website_entry.focus()

email_entry = Entry(width=44)
email_entry.insert(0, string="j.masood34@gmail.com")
email_entry.grid(sticky=W, row=2, column=1, columnspan=2)

password_entry = Entry(width=24)
password_entry.insert(0, string="Enter password....")
password_entry.grid(sticky=W, row=3, column=1)

# Buttons
search_button = Button(text="Search", height=1, width=14, command=lambda: find_password(website_entry.get()))
search_button.grid(row=1, column=2)

gen_password = Button(text="Generate Password", height=1, width=14, command=lambda: generate_password(password_entry))
gen_password.grid(sticky=S, row=3, column=2)

add_button = Button(text="Add", width=40, command=lambda: save_password(website_entry, email_entry, password_entry))
add_button.grid(row=4, column=1, columnspan=2, pady=10)


window.mainloop()
