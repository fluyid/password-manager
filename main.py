from tkinter import Tk, Canvas, PhotoImage, Label, Entry, Button, END, messagebox
from random import randint, choice, shuffle
from pyperclip import copy
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)
    password = "".join(password_list)

    password_input.insert(0, password)
    copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    """used to save data to a text file"""
    site = website_input.get()
    login = login_id_input.get()
    passkey = password_input.get()
    new_data = {site: {
        "login": login,
        "password": passkey,
    }}

    if len(site) == 0 or len(passkey) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        try:
            with open("data.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)
            with open("data.json", "w") as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            website_input.delete(0, END)
            password_input.delete(0, END)
            website_input.focus()


# Search Function

def find_password():
    website_name = website_input.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found")
    else:
        if website_name in data:
            login_detail = data[website_name]["login"]
            passkey = data[website_name]["password"]
            messagebox.showinfo(title=website_name, message=f"Login: {login_detail}\nPassword: {passkey}")
        else:
            messagebox.showinfo(title="Oops", message=f"No details for {website_name} exists")


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
website_input.grid(row=1, column=1, sticky="ew")
website_input.focus()

login_id_input = Entry()
login_id_input.grid(row=2, column=1, columnspan=2, sticky="ew")
login_id_input.insert(0, "kailash@gmail.com")

password_input = Entry()
password_input.grid(row=3, column=1, sticky="ew")

# Buttons

search_button = Button(text="Search", command=find_password)
search_button.grid(row=1, column=2, sticky="ew")

generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2, sticky="ew")

add_to_directory_button = Button(text="Add", width=36, command=save)
add_to_directory_button.grid(row=4, column=1, columnspan=2, sticky="ew")

# Window exit
window.mainloop()
