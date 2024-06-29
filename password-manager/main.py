import sys
import tkinter
from tkinter import messagebox
import password_generator
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    pg = password_generator.Password_generator()
    password_entry.delete(0,tkinter.END)
    new_password = password_entry.insert(0, pg.generate_password())

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    is_empty_field = False
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    if website == "" or email == "" or password == "":
        is_empty_field = True
        messagebox.showwarning(title="Oops", message="Please don't leave any field empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email}\nPassword: {password}\nIs it ok to save?")
        if is_ok and not is_empty_field:
            with open('data.txt', 'a') as f:
                f.write(f"{website} | {email} | {password}\n")
            website_entry.delete(0,tkinter.END)
            pyperclip.copy(password)
            password_entry.delete(0,tkinter.END)
            messagebox.showinfo(title="Successful", message="Login saved and password copied to clipboard")




# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()
window.config(padx=20, pady=20, bg="white")
window.title("Password Manager")

# Picture of padlock
canvas = tkinter.Canvas(width=200, height=200, bg="white", highlightthickness=0)
my_pass_img = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=my_pass_img)
canvas.grid(row=0, column=1)

# labels
website_label = tkinter.Label(text="Website:", bg="white")
website_label.grid(row=1, column=0)

email_label = tkinter.Label(text="Email/Username:", bg="white")
email_label.grid(row=2, column=0)

password_label = tkinter.Label(text="Password:", bg="white")
password_label.grid(row=3, column=0)

# entires
website_entry = tkinter.Entry(width=40)
website_entry.grid(sticky="W", row=1, column=1, columnspan=2)
website_entry.focus()

password_entry = tkinter.Entry(width=21)
password_entry.grid(row=3, column=1,sticky="W")

email_entry = tkinter.Entry(width=40)
email_entry.grid(sticky="W", row=2, column=1, columnspan=2)
email_entry.insert(tkinter.END, "oshhettiarachchi@gmail.com")

# buttons
generate_password_button = tkinter.Button(text="Generate Password", bg="white", borderwidth=0, padx=0, pady=0, command=generate_password)
generate_password_button.grid(row=3, column=2)

add_button = tkinter.Button(text="Add", width=40, bg="white", borderwidth=0, padx=1, pady=0, command=save)
add_button.grid(sticky="W", row=4, column=1, columnspan=2)
    




window.mainloop()