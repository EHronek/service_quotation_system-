#!/usr/bin/env python3
import tkinter as tk
import tkinter.font as tkfont
from tkinter import messagebox
from tkinter import ttk
from Home_page import design

def login():
    def on_menu_select(value):
        print("Selected:", value)



    window = tk.Tk()
    #window.geometry("400x200")
    window.resizable(False, False)
    window.title("Link Information System Login")
    window.config(background="#094a94")


    # Frame to contain login elements
    login_frame = tk.Frame(window, bg='#1d46c2', bd=2, relief="raised", pady=20, padx=20)
    login_frame.grid(row=0, column=0)
    window.grid_rowconfigure(0, weight=1)
    window.grid_columnconfigure(0, weight=1)

    # custom font
    custom_font = tkfont.Font(family='Arial', size=12)


    def access_system_as():
        pass

    def auth_details():

        from new_session import setup_db
        from new_base_model import User

        session = setup_db("root", "root", "sysdb")
        
        username = username_entry.get()
        password = password_entry.get()
        """ role = access_list.cget(sel_role)
        print(role) """
        role = access_dropdown.get()
        #role = "Administrator"

        users = session.query(User).all()

        for user in users:
            if role == user.access_level:
                if username == user.username and password == user.user_password:
                    messagebox.showinfo(title="User login", message="Login Successfull")
                    try:
                        username_entry.delete(0, tk.END)
                        password_entry.delete(0, tk.END)
                        access_dropdown.current(0)
                        design()
                    except Exception as e:
                        messagebox.showerror(title="loading Failure", message=f"Something went wrong while loading application, {e}")
                    finally:
                        session.close()
            
            else:
                messagebox.showerror(title="User Login", message="User enter does not exist")
                username_entry.delete(0, tk.END)
                password_entry.delete(0, tk.END)
                access_dropdown.current(0)
                session.close()




    """         if role == "Super Administrator":
            if username == "SuperAdm" and password == "@superAdmin":
                print("Login Successfull")
                messagebox.showinfo(title="Pavilion Information system", message="Super Administrator login successful")

                design()
            else:
                print("Login unsuccessful")
                messagebox.showerror(title="Pavilion information system", message="Super Adminstrator Login Unsuccessful")
        elif role == "Administrator":
            if username == "Admin" and password == "AdminPass":
                print("Login Successfull")
                messagebox.showinfo(title="Pavilion information system", message="Administrator Login successfull")

                design()
            else:
                messagebox.showerror(title="Pavilion information system", message="Adminstrator Login Unsuccesfull. TRY AGAIN")

                    
        elif role == "User":
            if username == "User01" and password == "UserPass":
                print("Login successful")
                messagebox.showinfo(title="Pavilion Information system", message="User Login Successful")
                
                design()


            else:
                print("Login Failure")
                messagebox.showerror(title="Pavilion Information System", message=" User Login Unsuccessful. TRY AGAIN!!!")
    """

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

if __name__ == "__main__":
    login()