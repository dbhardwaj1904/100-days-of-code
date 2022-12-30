from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import json
# import pyperclip

WHITE = "#ffffff"
FONT_SIZE = 12


# Search data
def search_data():
    _website = website_input.get()
    try:
        with open("sample_data.json", mode="r") as file:
            # Read json
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found")
    else:
        if _website in data:
            email = data[_website]["email"]
            user_password = data[_website]["password"]
            messagebox.showinfo(title=_website, message=f"Email: {email}\nPassword: {user_password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {_website}, exists.")

# Generate password
def generate_password():
    password_input.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '=']
    password_letters = [choice(letters) for item in range(randint(8, 10))]
    password_numbers = [choice(numbers) for item in range(randint(2, 4))]
    password_symbols = [choice(symbols) for item in range(randint(2, 4))]
    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)
    password_text = "".join(password_list)
    password_input.insert(0, password_text)
    # pyperclip.copy(password_text)


# Save password
def save_data_locally():
    _website = website_input.get()
    _user = email_input.get()
    _password = password_input.get()
    new_data = {
        _website: {
            "email": _user,
            "password": _password,
        }
    }
    if len(_website) == 0 or len(_password) == 0:
        messagebox.showinfo(title="Oops", message="Fields cannot be empty.")
    else:
        # Writing to text file
        # user_response = messagebox.askokcancel(title=_website, message=f"Do you want to save these details: \n"
        #                                                                f"Email: {_user}\nPassword: {_password}\n"
        #                                                                f"Website: {_website} ?")
        # if user_response:
        # with open("sample_data.txt", mode="a") as file:
        #     file.write(f"{_website} | {_user} | {_password}\n")
        #     website_input.delete(0, END)
        #     password_input.delete(0, END)

        # CRUD in json
        try:
            with open("sample_data.json", mode="r") as file:
                # Read json
                data = json.load(file)
        except FileNotFoundError:
            with open("sample_data.json", mode="w") as file:
                json.dump(new_data, file, indent=4)
        else:
            # Update json
            data.update(new_data)
            with open("sample_data.json", mode="w") as file:
                # Write json
                json.dump(data, file, indent=4)
        finally:
            website_input.delete(0, END)
            password_input.delete(0, END)


# UI
window = Tk()
window.title("Password Manager")
window.config(padx=60, pady=60, bg=WHITE)

canvas = Canvas(width=200, height=200, bg=WHITE, highlightthickness=0)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website: ", bg=WHITE)
website_label.grid(row=1, column=0)

user_email = Label(text="Email/Username: ", bg=WHITE)
user_email.grid(row=2, column=0)

password = Label(text="Password: ", bg=WHITE)
password.grid(row=3, column=0)

# Inputs
website_input = Entry(width=51)
website_input.grid(row=1, column=1, columnspan=1)
website_input.focus()

email_input = Entry(width=69)
email_input.grid(row=2, column=1, columnspan=2)
email_input.insert(0, "demo@gmail.com")

password_input = Entry(width=51)
password_input.grid(row=3, column=1)

# Buttons
generate_password_input = Button(text="Generate Password", command=generate_password)
generate_password_input.grid(row=3, column=2)

add_button = Button(text="Add", width=59, command=save_data_locally)
add_button.grid(row=4, column=1, columnspan=2)

search_button = Button(text="Search", width=14, command=search_data)
search_button.grid(row=1, column=2)

window.mainloop()
