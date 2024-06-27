import tkinter

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    pass
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
generate_password_button = tkinter.Button(text="Generate Password", bg="white", borderwidth=0, padx=0, pady=0)
generate_password_button.grid(row=3, column=2)

add_button = tkinter.Button(text="Add", width=40, bg="white", borderwidth=0, padx=1, pady=0)
add_button.grid(sticky="W", row=4, column=1, columnspan=2)
    




window.mainloop()