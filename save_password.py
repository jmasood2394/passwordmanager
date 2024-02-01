import json
from tkinter import messagebox, END


def save_password(website_entry, email_entry, password_entry):
    """ Save data in entry fields to file data.json """
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="No Entry", message="Please fill all the fields")

    else:
        # Message box to confirm
        is_ok = messagebox.askokcancel(title=website,
                                       message=f"These are the details entered:\n\nWebsite: {website}\nUsername:{email}"
                                       f"\nPassword:{password}\n\nIs it ok to save?")

        # Save to file
        if is_ok:
            try:
                with open("data.json", 'r') as file:
                    # Read old data
                    data = json.load(file)
                    # update data with new data
                    data.update(new_data)
                    # write to file
                with open("data.json", "w") as file:
                    json.dump(data, file, indent=4)
            except json.decoder.JSONDecodeError:
                with open("data.json", "w") as file:
                    json.dump(new_data, file, indent=4)
            except FileNotFoundError:
                with open("data.json", "w") as file:
                    json.dump(new_data, file, indent=4)
            finally:
                # Clear the entry boxes
                website_entry.delete(0, END)
                website_entry.focus()
                email_entry.delete(0, END)
                password_entry.delete(0, END)

                # Refill the entry boxes
                email_entry.insert(0, string="j.masood34@gmail.com")
                password_entry.insert(0, string="Enter password....")
