# ---------------------------- PASSWORD GENERATOR ------------------------------- #

import random
from tkinter import messagebox
import json


def my_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
               'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    nr_letters = random.randint(10,12)
    nr_symbols = random.randint(3,5)
    nr_numbers = random.randint(3,5)
    
    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    
    password_list = password_letters + password_numbers + password_symbols
    random.shuffle(password_list)    
    
    password = "".join(password_list)
    password_entry.insert(0, password)
    
    # for autocopying password
    # pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    
    website_data = website_entry.get()
    email_data = email_entry.get()
    password_data = password_entry.get()
    new_data = {
        website_data: {
            "email": email_data,
            "password": password_data,
        }
                }
    
    if len(website_data) ==0 or len(password_data) ==0:
        messagebox.showinfo(title = "Oops", message = "Please make sure you have not left any fields empty")
    else:
        is_ok = messagebox.askokcancel(title = website, message = f"These are the details entered:\nEmail: {email_data}"
                                    f"\nPassword: {password_data} \nIs it ok to save?")
        
        if is_ok:
            try:
                
                with open("data.json", "r") as data_file:
                    # load json data
                    data = json.load(data_file)
            except FileNotFoundError:
                    with open("data.json", "w") as data_file:
                        json.dump(new_data, data_file, indent = 4)
                        website_entry.delete(0, END)
                        password_entry.delete(0, END)
            else:
                data.update(new_data)
                with open("data.json", "w") as data_file:
                    json.dump(data, data_file, indent = 4)
                    
            finally: 
                website_entry.delete(0, END)
                password_entry.delete(0, END)
                    
# ---------------------------- find password ------------------------------- #


def find_password():
    website = website_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
            
    except FileNotFoundError:
        messagebox.showinfo(title = "Error", message = "No data file found")
        
        
    else:    
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title = website, message = f"EMAIL: {email}\n Password: {password}")

        else:
            messagebox.showinfo(title = "Error", message = "No details for this website")
                 
# ---------------------------- UI SETUP ------------------------------- #

from tkinter import *


window = Tk()
window.title("Password generator")
window.config(padx=20, pady = 20)
canvas = Canvas(width = 200, height= 200)

logo = PhotoImage(file = "logo.png")
canvas.create_image(100, 100, image = logo)
canvas.grid(column=1, row = 0)

website = Label(text = 'Website')
website.grid(column = 0, row =1)

email = Label(text = 'Email/Username')
email.grid(column = 0, row =2)

password = Label(text = 'Password')
password.grid(column = 0, row = 3)


website_entry = Entry(width = 40)
website_entry.grid(row = 1, column = 1 )
website_entry.focus()

email_entry = Entry(width = 40)
email_entry.grid(row = 2, column = 1)
email_entry.insert(0, "sarjveladzebeqa98@gmail.com")

password_entry = Entry(width = 40)
password_entry.grid(column = 1, row = 3)

search = Button(text = 'Search', width =15, command = find_password)
search.grid(column = 2, row = 1)


generator = Button(text = 'Generate password', width =15, command = my_password)
generator.grid(column = 2, row = 3)

add = Button(text = 'add', width = 51, command = save)
add.grid(row = 4, column = 1, columnspan=2, )








window.mainloop()