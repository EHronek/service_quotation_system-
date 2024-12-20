import customtkinter as ctk
import tkinter

def login():
    pass

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

root = ctk.CTk()
root.geometry("500x350")

frame = ctk.CTkFrame(master=root)
frame.pack(pady=20,padx=60, fill='both', expand=True)

def access_system_role():
    pass
access_role = ["Administrator", "User"]
selected_role = ctk.StringVar(frame)
login_as = ctk.CTkOptionMenu(master=frame, *access_role, command=access_system_role)

label = ctk.CTkLabel(master=frame, text="Login System")
label.pack(pady=12, padx=10)

entry1 = ctk.CTkEntry(master=frame, placeholder_text="Username")
entry1.pack(pady=12, padx=10)

entry2= ctk.CTkEntry(master=frame, placeholder_text="Password", show="*")
entry2.pack(pady=12, padx=10)

button = ctk.CTkButton(master=frame, text="Login", command=login)
button.pack(pady=12, padx=10)

checkbox = ctk.CTkCheckBox(master=frame, text='Remember Me')
checkbox.pack(pady=12, padx=10)

root.mainloop()
