import tkinter as tk
from tkinter import ttk

# creating the root window
home_root = tk.Tk()
home_root.geometry("1000x600")
home_root.title("Pavilion information System")
home_root.config(background="#0d93bf")

#creating the main access panel tab
notebook = ttk.Notebook(home_root)

Main_panel_tab = tk.Frame(notebook)
Application_reg_tab = tk.Frame(notebook)

notebook.add(Main_panel_tab, text="Main access Panel")
notebook.add(Application_reg_tab, text="Application regeistration")
notebook.pack(expand=True, fill="both")


notebook2 = ttk.Notebook(Main_panel_tab)
quotation_tab = tk.Frame(notebook2)
registration_tab = tk.Frame(notebook2)
client_details_tab = tk.Frame(notebook2)
project_update_tab = tk.Frame(notebook2)
project_timeline_tab = tk.Frame(notebook2)
dashboard_tab = tk.Frame(notebook2)
client_finances_tab = tk.Frame(notebook2)
company_finances_tab = tk.Frame(notebook2)
user_account_setting_tab = tk.Frame(notebook2)
Database_setting_tab = tk.Frame(notebook2)

notebook2.add(quotation_tab, text="Service Quations")
notebook2.add(registration_tab, text="Client Registration")
notebook2.add(client_details_tab, text="Client Details")
notebook2.add(project_update_tab, text="Project update")
notebook2.add(project_timeline_tab, text="Project timeline")
notebook2.add(dashboard_tab, text="Dashboard")
notebook2.add(client_finances_tab, text="Client finances")
notebook2.add(company_finances_tab, text="Company Finances")
notebook2.add(user_account_setting_tab, text="User Account Settings")
notebook2.add(Database_setting_tab, text="Database Settings")
notebook2.pack(expand=True, fill="both")


home_root.mainloop()