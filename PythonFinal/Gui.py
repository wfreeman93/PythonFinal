import json
import tkinter as tk
from jsonModule import Account
from jsonModule import AccountJSONEEncoder
import time

account_number = (time.strftime("%d%m%Y%H%M%S"))


def search_popup():
    search_popup_window = tk.Tk()
    search_popup_window.geometry("300x100")
    search_popup_window.title("Search customer")
    label = tk.Label(search_popup_window, text="Please enter an account number to search")
    label.pack()
    search_entry = tk.Entry(search_popup_window)
    search_entry.pack()
    lookup_button = tk.Button(search_popup_window, text="Look Up",
                              command=lambda: search_popup_successful(search_entry.get()))
    lookup_button.pack()
    search_popup_window.mainloop()


def add_popup():
    add_popup_window = tk.Tk()
    add_popup_window.geometry("400x200")
    add_popup_window.title("Add customer")
    label = tk.Label(add_popup_window, text="Please fill out as much information as possible")
    label.pack()
    first_name_label = tk.Label(add_popup_window, text="First Name: ")
    first_name_label.pack()
    first_name_entry = tk.Entry(add_popup_window)
    first_name_entry.pack()
    last_name_label = tk.Label(add_popup_window, text="Last Name: ")
    last_name_label.pack()
    last_name_entry = tk.Entry(add_popup_window)
    last_name_entry.pack()
    phone_number_lbl = tk.Label(add_popup_window, text="Phone Number: ")
    phone_number_lbl.pack()
    phone_number_entry = tk.Entry(add_popup_window)
    phone_number_entry.pack()
    address_lbl = tk.Label(add_popup_window, text="Address: ")
    address_lbl.pack()
    address_entry = tk.Entry(add_popup_window)
    address_entry.pack()
    save_data = tk.Button(add_popup_window,
                          text="Save Data",
                          command=lambda: add_popup_successful(account_number,
                                                               first_name_entry.get(),
                                                               last_name_entry.get(),
                                                               phone_number_entry.get(),
                                                               address_entry.get()))
    save_data.pack()
    add_popup_window.mainloop()


def add_popup_successful(anumber, fname, lname, phone, address):
    add_popup_successful_window = tk.Tk()
    add_popup_successful_window.geometry("400x200")
    success_lbl = tk.Label(add_popup_successful_window, text="Created customer file in Database!")
    success_lbl.pack()
    new_account = Account(account_number, fname, lname, phone, address)
    data = [new_account]
    with open(anumber, 'w') as json_file:
        json.dump(data, json_file, cls=AccountJSONEEncoder, indent=2)

    with open(anumber, 'r') as json_file:
        for line in json_file:
            print(line, end="")


def search_popup_successful(acc_number):
    search_popup_successful_window = tk.Tk()
    search_popup_successful_window.geometry("800x100")
    search_popup_successful_window.title("Customer information")
    with open(acc_number, 'r') as json_file:
        printdata = json.load(json_file)
    search_popup_successful_label = tk.Label(search_popup_successful_window, text=printdata)
    search_popup_successful_label.pack()


initial = tk.Tk()
initial.geometry("300x100")
initial.title("Welcome to DataProDataBase")

#choices for initial window#
search_button = tk.Button(initial, text="Would you like to search the Database?", command=search_popup)
search_button.pack()

add_button = tk.Button(initial, text="Would you like to add customer to Database?", command=add_popup)
add_button.pack()

initial.mainloop()

