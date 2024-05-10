""" import tkinter as tk

def on_menu_select(value):
    print("Selected:", value)

root = tk.Tk()
root.title("Simple Dropdown Menu")

selected_value = tk.StringVar(root)
dropdown = tk.OptionMenu(root, selected_value, "Option 1", "Option 2", "Option 3", command=on_menu_select)
dropdown.pack()

selected_value.set("Option 1")

root.mainloop()
 """
""" import tkinter as tk

def on_menu_select(value):
    print("Selected:", value)

root = tk.Tk()
root.title("Multi-level Dropdown Menu")

menu = tk.Menu(root)
root.config(menu=menu)

submenu = tk.Menu(menu)
menu.add_cascade(label="Options", menu=submenu)
submenu.add_command(label="Option 1", command=lambda: on_menu_select("Option 1"))
submenu.add_command(label="Option 2", command=lambda: on_menu_select("Option 2"))
submenu.add_command(label="Option 3", command=lambda: on_menu_select("Option 3"))

root.mainloop()
 """

import tkinter as tk
from tkinter import ttk

def login():
    username = username_entry.get()
    password = password_entry.get()
    access_level = access_level_var.get()
    
    # Perform authentication logic here
    print("Username:", username)
    print("Password:", password)
    print("Access Level:", access_level)

root = tk.Tk()
root.title("Login Page")

# Frame to contain login elements
login_frame = tk.Frame(root, padx=20, pady=20)
login_frame.pack()

# Username label and entry
username_label = tk.Label(login_frame, text="Username:")
username_label.grid(row=0, column=0, sticky="w")

username_entry = ttk.Entry(login_frame)
username_entry.grid(row=0, column=1)

# Password label and entry
password_label = tk.Label(login_frame, text="Password:")
password_label.grid(row=1, column=0, sticky="w")

password_entry = ttk.Entry(login_frame, show="*")
password_entry.grid(row=1, column=1)

# Access level label and dropdown
access_level_label = tk.Label(login_frame, text="Access Level:")
access_level_label.grid(row=2, column=0, sticky="w")

access_level_var = tk.StringVar()
access_level_dropdown = ttk.Combobox(login_frame, textvariable=access_level_var, values=["Admin", "User"])
access_level_dropdown.grid(row=2, column=1)
access_level_dropdown.current(0)

# Login button
login_button = ttk.Button(login_frame, text="Login", command=login)
login_button.grid(row=3, columnspan=2, pady=10)

root.mainloop()
