from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

FONT = ('Arial', 11)
LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def save():
    website_field = website_entry.get()
    user_field = user_entry.get()
    password_field = password_entry.get()
    new_data = {
        website_field: {
            'user': user_field,
            'password': password_field
        }
    }
    if website_field == '' or password_field == '':
        messagebox.showwarning(title='ERROR', message='Don\'t leave any field empty!')
    else:
        try:
            with open('data.json', 'r') as data_file:
                data = json.load(data_file)
                data.update(new_data)
            with open('data.json', 'w') as data_file:
                json.dump(data, data_file, indent=4)
        except FileNotFoundError:
            with open('data.json', 'w') as data_file:
                json.dump(new_data, data_file)
        website_entry.delete(0, END)
        password_entry.delete(0, END)


def generate_password():
    password_letters = [random.choice(LETTERS) for x in range(random.randint(8, 10))]
    password_symbols = [random.choice(SYMBOLS) for y in range(random.randint(2, 4))]
    password_numbers = [random.choice(NUMBERS) for z in range(random.randint(2, 4))]
    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)
    password = ''.join(password_list)

    pyperclip.copy(password)
    password_entry.delete(0, END)
    password_entry.insert(0, f'{password}')


def search():
    website = website_entry.get()
    try:
        with open('data.json', 'r') as data_file:
            data = json.load(data_file)
            if website in data:
                user = data[website]["user"]
                password = data[website]["password"]
                messagebox.showwarning(title=f'{website.title()}', message=f'User: {user}\nPassword: {password}')
            else:
                messagebox.showwarning(title='ERROR', message='No details for the website exists')
    except FileNotFoundError:
        messagebox.showwarning(title='ERROR', message='No Data File Found')


window = Tk()
window.title('Password')
window.config(padx=50, pady=50)

logo_img = PhotoImage(file='logo.png')
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

website_label = Label(text='Website:', font=FONT, anchor='w', width=14)
website_label.grid(column=0, row=1)
user_label = Label(text='Email/Username:', font=FONT, anchor='w', width=14)
user_label.grid(column=0, row=2)
password_label = Label(text='Password:', font=FONT, anchor='w', width=14)
password_label.grid(column=0, row=3)

website_entry = Entry(width=32)
website_entry.grid(column=1, row=1, sticky="W", pady=4)
user_entry = Entry(width=35)
user_entry.insert(0, 'lucamanfroi@gmail.com')
user_entry.grid(column=1, row=2, columnspan=2, sticky="EW", pady=4)
password_entry = Entry(width=32)
password_entry.grid(column=1, row=3, sticky="W", pady=4)

password_button = Button(text='Generate Password', command=generate_password)
password_button.grid(column=2, row=3, sticky="EW")
add_button = Button(text='Add', width=36, command=save)
add_button.grid(column=1, row=4, columnspan=24, sticky="EW", pady=4)
search_button = Button(text='Search', command=search)
search_button.grid(column=2, row=1, columnspan=24, sticky="EW", pady=4)


window.mainloop()
