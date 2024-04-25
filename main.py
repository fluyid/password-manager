from tkinter import Tk, Canvas, PhotoImage, Label, Entry, Button
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

# window

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# canvas

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels

website = Label(text="Website:")
website.grid(row=1, column=0)

login_id = Label(text="Email/Username:")
login_id.grid(row=2, column=0)

password = Label(text="Password:")
password.grid(row=3, column=0)

# Entries

website_input = Entry()
website_input.grid(row=1, column=1, columnspan=2, sticky="ew")

login_id_input = Entry()
login_id_input.grid(row=2, column=1, columnspan=2, sticky="ew")

password_input = Entry()
password_input.grid(row=3, column=1, sticky="ew")

# Buttons

generate_password_button = Button(text="Generate Password")
generate_password_button.grid(row=3, column=2, sticky="ew")

add_to_directory_button = Button(text="Add", width=36)
add_to_directory_button.grid(row=4, column=1, columnspan=2, sticky="ew")

# Window exit
window.mainloop()
