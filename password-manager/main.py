from tkinter import *
from tkinter import messagebox
from generator import generate_password
import pyperclip
import json

# ---------------------------- SEARCH FOR PASSWORD------------------------------- #

def search_for_password():

    website = website_entry.get()

    if len(website) == 0:
        messagebox.showinfo(title='Oops!', message="Try again, some details are missing")
    else:
        try:
            with open('data.json', 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            messagebox.showerror(title='DATA FILE NOT FOUND', message='Your data file has not been found, please check '
                                                                      'records.')
        else:
            found = False
            for k, v in data.items():
                if website == k:
                    messagebox.showinfo(title='Password Details',
                                        message=f'Website: {website}\n'
                                                f'E-mail: {v["email"]}\n'
                                                f'Password: {v["password"]}')
                    found = True
            if not found:
                messagebox.showwarning(title='No Match', message='No matching details')


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_password():

    result = StringVar()
    p_word = generate_password()
    result.set(p_word)

    password_entry.delete(0, END)
    password_entry.insert(0, p_word)
    pyperclip.copy(p_word)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_entry():

    website = website_entry.get()
    email = email_entry.get()
    p_word = password_entry.get()
    new_data = {
        website:{
            'email' : email,
            'password' : p_word
                    }
    }
    missing_details = len(website) == 0 or len(p_word) == 0
    if missing_details:
        messagebox.showinfo(title='Oops!', message="Try again, some details are missing")
    else:
        try:
            with open('data.json', 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            with open('data.json', 'w') as file:
                json.dump(new_data, file, indent=4)
        else:
            data.update(new_data)
            with open('data.json', 'w') as file:
                json.dump(data, file, indent=4)
        finally:
            website_entry.delete(0, 'end')
            password_entry.delete(0,'end')

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Manager')
window.config(padx=20, pady=20)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file='logo.png')
canvas.create_image(100,100,image=logo_img)
canvas.grid(column=1, row=0)

website_label = Label(text='Website:')
website_label.grid(column=0, row=1)
email_label = Label(text='Email/Username')
email_label.grid(column=0, row=2)
password_label = Label(text='Password')
password_label.grid(column=0, row=3)

website_entry = Entry(width=21)
website_entry.grid(column=1, row=1)
email_entry = Entry(width=35)
email_entry.insert(0,'alistairedwardjenkins.gmail.com')
email_entry.grid(column=1, row=2, columnspan=2)
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

search_button = Button(text='Search', width=13, command=search_for_password)
search_button.grid(column=2, row=1)
generate_password_button = Button(text='Generate password', command=gen_password)
generate_password_button.grid(column=2, row=3)
add_button = Button(text='Add', width=36, command=add_entry)
add_button.grid(column=1, row=4, columnspan=2)



window.mainloop()

