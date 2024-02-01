import json
from tkinter import messagebox


def find_password(website):
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No data file has been saved yet.")
    else:
        if website in data:
            username = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=f"{website}", message=f"Username:{username}\nPassword:{password}")
        else:
            messagebox.showerror(title="Error", message=f"No information for {website} saved.")
