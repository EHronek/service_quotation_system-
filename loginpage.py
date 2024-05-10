#!/usr/bin/env python3
import tkinter as tk
import tkinter.font as tkfont
from tkinter import messagebox
from tkinter import ttk
def on_menu_select(value):
    print("Selected:", value)



window = tk.Tk()
#window.geometry("400x200")
window.resizable(False, False)
window.title("Link Information System Login")
window.config(background="#094a94")

""" frame = tk.Frame(window, bg='blue', bd=2, relief=tk.SOLID)
frame.pack()

login_as = ["Super Administrator", "Administrator", "User"]


selected_value = tk.StringVar(frame)
dropdown = tk.OptionMenu(frame, selected_value, *login_as, command=on_menu_select)
dropdown.grid(row=0, column=1)

username_label = tk.Label(frame, text="Username ", font=("Arial", 12))
username_label.grid(row=1, column=0)

username_entry = tk.Entry(frame, tkfont('Arial', 12), bg="#0cff00")
username_entry.grid(row=2, column=1)

passwd_label = tk.Label(frame, text="Password ", font=("Arial", 12))
passwd_label.grid(row=2,column=0)

password_entry = tk.Entry(frame, tkfont("arial", 12), show='*')
password_entry.grid(row=2, column=1) """

# Frame to contain login elements
login_frame = tk.Frame(window, bg='#1d46c2', bd=2, relief="raised", pady=20, padx=20)
login_frame.grid(row=0, column=0)
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)

# custom font
custom_font = tkfont.Font(family='Arial', size=12)

# creating a list box of how to login
""" access_list = tk.Listbox(login_frame, font=custom_font)
access_list.grid(row=0, column=0)

access_list.insert(1, "Super Administrator")
access_list.insert(2, "Administrator")
access_list.insert(3, "User")
access_list.config(height=access_list.size()) """

def access_system_as():
    pass

def auth_details():
    
    username = username_entry.get()
    password = password_entry.get()
    """ role = access_list.cget(sel_role)
    print(role) """
    role = access_dropdown.get()
    #role = "Administrator"

    if role == "Super Administrator":
        if username == "SuperAdm" and password == "@superAdmin":
            print("Login Successfull")
            messagebox.showinfo(title="Pavilion Information system", message="Super Administrator login successful")
        else:
            print("Login unsuccessful")
            messagebox.showerror(title="Pavilion information system", message="Super Adminstrator Login Unsuccessful")
    elif role == "Administrator":
        if username == "Admin" and password == "AdminPass":
            print("Login Successfull")
            messagebox.showinfo(title="Pavilion information system", message="Administrator Login successfull")
        else:
            messagebox.showerror(title="Pavilion information system", message="Adminstrator Login Unsuccesfull. TRY AGAIN")
                
    elif role == "User":
        if username == "User01" and password == "UserPass":
            print("Login successful")
            messagebox.showinfo(title="Pavilion Information system", message="User Login Successful")
        else:
            print("Login Failure")
            messagebox.showerror(title="Pavilion Information System", message=" User Login Unsuccessful. TRY AGAIN!!!")


# Access system as who

access_list_label = tk.Label(login_frame, text="Access System as:")
access_list_label.grid(row=0, column=0)

access_role = ["Super Administrator", "Administrator", "User"]

# create a drop box
access_dropdown = ttk.Combobox(login_frame, value=access_role)
access_dropdown.current(0)
access_dropdown.grid(row=0, column=1)
# Bind the box with an action to perform
access_dropdown.bind("<<ComboboxSelected>>, ")

""" selected_role = tk.StringVar(login_frame)
access_list = tk.OptionMenu(login_frame,selected_role, *access_role)
access_list.grid(row=0, column=1) """

# user_label and Entry
username_label = tk.Label(login_frame, text="Username", bg="#1d46c2",font=custom_font, padx=10, pady=10)
username_label.grid(row=1,column=0, sticky="w")

username_entry = tk.Entry(login_frame, font=custom_font, bg="#d6c8a3", width=20)
username_entry.grid(row=1, column=1, padx=10)

#password label and entry field
password_label = tk.Label(login_frame, text="Password",bg="#1d46c2", font=custom_font, padx=10, pady=10)
password_label.grid(row=2, column=0, sticky='w')

password_entry = tk.Entry(login_frame, show="*", bg="#d6c8a3", width=20)
password_entry.grid(row=2, column=1, padx=10)

#Login button
login_button = tk.Button(login_frame, text="Login", command=auth_details, bg="#5f79c7")
login_button.grid(row=3, column = 1)

window.mainloop()
