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


#Create application registration tab
notebook3 = ttk.Notebook(Application_reg_tab)
app_reg_tab = tk.Frame(notebook3)
employee_reg_tab = tk.Frame(notebook3)

#adding company  reg tabb and Employee reg tab to notebook
notebook3.add(app_reg_tab, text="Company Registration")
notebook3.add(employee_reg_tab, text="Employee Registration")
notebook3.pack(expand=True, fill="both")

app_frame = tk.Frame(app_reg_tab)
app_frame.pack(side=tk.LEFT)
#creating labels and entry fields
tk.Label(app_frame, text="ENTER COMPANY DETAILS").grid(row=0, column=0)
tk.Label(app_frame, text="Organization Name").grid(row=1, column= 0)
tk.Label(app_frame, text="Organization contact").grid(row=3, column=0)
tk.Label(app_frame, text="Location").grid(row=5, column= 0)
tk.Label(app_frame, text="Organization email").grid(row=7, column=0)
tk.Label(app_frame, text="Email password").grid(row=9, column=0)
tk.Label(app_frame, text="Repeat Password").grid(row=11, column=0)

#creating entry fields for company details
org_name_entry = tk.Entry(app_frame, width=50)
org_name_entry.grid(row=2, column=0, pady=10, padx=20)

org_contact_entry = tk.Entry(app_frame, width=50)
org_contact_entry.grid(row=4, column=0, pady=10, padx=20)

location_entry = tk.Entry(app_frame, width=50)
location_entry.grid(row=6, column=0, pady=10, padx=20)

org_email_entry = tk.Entry(app_frame, width=50)
org_email_entry.grid(row=8, column=0, pady=10, padx=20)

email_password_entry = tk.Entry(app_frame, show='*', width=50)
email_password_entry.grid(row=10, column=0, pady=10, padx=20)

repeat_password_entry = tk.Entry(app_frame, show='*', width=50)
repeat_password_entry.grid(row=12, column=0, pady=10, padx=20)

save_register_button = tk.Button(app_frame, text="Save and Register", relief=tk.RAISED)
save_register_button.grid(row= 13, column =0, pady=10, padx=20)

cancel_button = tk.Button(app_frame, text="Cancel")
cancel_button.grid(row=14, column=0, pady=10, padx=20)

#creating a Frame for update Company details
app_frame2 = tk.Frame(app_reg_tab)
app_frame2.pack(side=tk.RIGHT)

#creating labels for Update company details
tk.Label(app_frame2, text="UPDATE COMPANY DETAILS").grid(row=0, column=0, padx=20)
tk.Label(app_frame2, text="Organization Name").grid(row=3, column= 0, padx=20)
tk.Label(app_frame2, text="Organization contact").grid(row=5, column=0, padx=20)
tk.Label(app_frame2, text="Location").grid(row=7, column= 0, padx=20)
tk.Label(app_frame2, text="Organization email").grid(row=9, column=0, padx=20)
tk.Label(app_frame2, text="Email password").grid(row=11, column=0, padx=20)
tk.Label(app_frame2, text="Repeat Password").grid(row=13, column=0, padx=20)

#creating entry for update company details
org_name_entry = tk.Entry(app_frame2, width=25 )
org_name_entry.grid(row=0, column=0)

org_name_entry = tk.Entry(app_frame2, width=50)
org_name_entry.grid(row=4, column=0, pady=10, padx=20)

org_contact_entry = tk.Entry(app_frame2, width=50)
org_contact_entry.grid(row=6, column=0, pady=10, padx=20)

location_entry = tk.Entry(app_frame2, width=50)
location_entry.grid(row=8, column=0, pady=10, padx=20)

org_email_entry = tk.Entry(app_frame2, width=50)
org_email_entry.grid(row=10, column=0, pady=10, padx=20)

email_password_entry = tk.Entry(app_frame2, show='*', width=50)
email_password_entry.grid(row=12, column=0, pady=10, padx=20)

repeat_password_entry = tk.Entry(app_frame2, show='*', width=50)
repeat_password_entry.grid(row=14, column=0, pady=10, padx=20)

load_button = tk.Button(app_frame2, text="Load details")
load_button.grid(row=0, column=1)

update_register_button = tk.Button(app_frame2, text="Update and Register", relief=tk.RAISED, width=30)
update_register_button.grid(row= 15, column =0)

delete_button = tk.Button(app_frame2, text="Delete Organization account")
delete_button.grid(row=16, column=0, pady=10, padx=20)

# Designing employee registration section

tk.Label(employee_reg_tab, text="REGISTER EMPLOYEE BELOW").pack(side="top")

emp_details_frame = ttk.Frame(employee_reg_tab)
emp_details_frame.pack(side=tk.LEFT)
# creating labels for employee personnal details
tk.Label(emp_details_frame, text="EMPLOYEE PERSONAL DETAILS").grid(row=0, column=0)
tk.Label(emp_details_frame, text="Employee Name").grid(row=1, column=0)
tk.Label(emp_details_frame, text="Employee Id").grid(row=3, column=0)
tk.Label(emp_details_frame, text="Employee Contact").grid(row=5, column=0)
tk.Label(emp_details_frame, text="Employees Email").grid(row=7, column=0)
tk.Label(emp_details_frame, text="Role").grid(row=9, column=0)

#creating Entries for employee details
emp_name_entry = tk.Entry(emp_details_frame, width=30)
emp_name_entry.grid(row=2, column=0)
emp_id = tk.Entry(emp_details_frame, width=30)
emp_id.grid(row=4, column=0)
emp_contact_entry = tk.Entry(emp_details_frame, width=30)
emp_contact_entry.grid(row=6, column=0)
emp_email_entry = tk.Entry(emp_details_frame, width=30)
emp_email_entry.grid(row=8, column=0)
emp_role_entry = tk.Entry(emp_details_frame, width=30)
emp_role_entry.grid(row=10, column=0)

#creating buttons for register and and update employee
reg_emp_button = tk.Button(emp_details_frame, text="Register employee")
reg_emp_button.grid(row=11, column=0, pady=10)

clear_button = tk.Button(emp_details_frame, text="Clear Fields")
clear_button.grid(row=12, column=0, pady=10)

update_employee_button = tk.Button(emp_details_frame, text="Update employee details")
update_employee_button.grid(row=13, column=0, pady=10)

delete_employee_button = tk.Button(emp_details_frame, text="Delete employee details")
delete_employee_button.grid(row=14, column=0, pady=10)

# Employee detail table
def emp_table_design():
    emp_table_frame = tk.Frame(employee_reg_tab)
    emp_table_frame.pack(side=tk.RIGHT )
    emp_tree = ttk.Treeview(emp_table_frame)

    #define employee columns
    emp_tree['columns'] = ("employee_id", "employee_name", "employee_contact", "employee_email", "employee_role")
    emp_tree.column("#0", width=0, stretch=tk.NO)
    emp_tree.column("employee_id", anchor=tk.CENTER, width=80)
    emp_tree.column("employee_name", anchor=tk.W, width=100)
    emp_tree.column("employee_contact", anchor=tk.W, width=100)
    emp_tree.column("employee_email", anchor=tk.W, width=100)
    emp_tree.column("employee_role", anchor=tk.W, width=100)

    #Creating column Headings
    emp_tree.heading("#0", text="", anchor=tk.W)
    emp_tree.heading("employee_id", text="employee_id", anchor=tk.CENTER)
    emp_tree.heading("employee_name", text="employee_name",anchor=tk.W)
    emp_tree.heading("employee_contact", text="employee_contact", anchor=tk.W)
    emp_tree.heading("employee_email", text="employee_email", anchor=tk.W)
    emp_tree.heading("employee_role", text="employee_role", anchor=tk.W)

    #insert data
    emp_tree.pack()

 

emp_table_design()



# CREATING A QUOTATION SECTION
def quotation():
    quote_notebook = ttk.Notebook(quotation_tab)
    create_quote_tab = tk.Frame(quote_notebook)
    view_quote_tab = tk.Frame(quote_notebook)
    edit_quote_tab = tk.Frame(quote_notebook)
    response_tab = tk.Frame(quote_notebook)

    quote_notebook.add(create_quote_tab, text='Create New')
    quote_notebook.add(view_quote_tab, text='View quotations')
    quote_notebook.add(edit_quote_tab, text='Edit existing')
    quote_notebook.add(response_tab, text="Response and updates")
    quote_notebook.pack(expand=True, fill='both')

    #create new quotation section
    reg_quote_frame = tk.Frame(create_quote_tab)
    reg_quote_frame.pack(side="left")

    #creating labals and Entries for the new quotation
    #tk.Label(reg_quote_frame, text="CREATE NEW QUOTATION BELOW").pack(side='top')
    tk.Label(reg_quote_frame, text="Quotation number").grid(row=0, column=0, pady=5)
    tk.Label(reg_quote_frame, text="Client name").grid(row=1, column=0, pady=5)
    tk.Label(reg_quote_frame, text="Client contact").grid(row=2, column=0, pady=5)
    tk.Label(reg_quote_frame, text="Client email").grid(row=3, column=0, pady=5)
    tk.Label(reg_quote_frame, text="Application type").grid(row=4, column=0, pady=5)

    quote_num_entry = tk.Entry(reg_quote_frame, width =30)
    quote_num_entry.grid(row=0, column=1, pady=5)
    client_name_entry = tk.Entry(reg_quote_frame, width=30)
    client_name_entry.grid(row=1, column=1, pady=5)
    client_contact_entry = tk.Entry(reg_quote_frame, width=30)
    client_contact_entry.grid(row=2, column=1, pady=5)
    client_email_entry = tk.Entry(reg_quote_frame, width=30)
    client_email_entry.grid(row=3, column=1, pady=5)
    
    #drop down for the application type
    app_types = ["Select application type" ,"Desktop Application", "Web Application", "Web (Static)", "Website (Dynamic)", "Mobile Application"]
    app_type_combo = ttk.Combobox(reg_quote_frame, value=app_types)
    app_type_combo.current(0)
    app_type_combo.bind("<<ComboboxSelected>>")
    app_type_combo.grid(row=4, column=1, pady=5)

    # Creating a text area for service description
    service_description = tk.Text(reg_quote_frame, bg='#edead5', height=15, width=25, padx=20,pady=20)
    service_description.grid(row=5, column=0, columnspan=3)

    tk.Label(reg_quote_frame, text="Service cost").grid(row=6, column=0, pady=5)
    service_cost = tk.Entry(reg_quote_frame, width=30)
    service_cost.grid(row=6, column=1, pady=5)

    # creating a table that show details of the quotations created
    quote_table_frame = tk.Frame(create_quote_tab)
    quote_table_frame.pack(side="right")

    #create quotation button
    create_quote_button = tk.Button(quote_table_frame, text="Create quotation")
    create_quote_button.pack(side='top', pady=20, padx=20)


    quote_tree = ttk.Treeview(quote_table_frame)

    quote_tree['columns'] = ("quotation_number", "client_name","service_description")
    quote_tree.column("#0", width=0, stretch=tk.NO)
    quote_tree.column("quotation_number", anchor=tk.W, width=150)
    quote_tree.column("client_name", anchor=tk.W, width=150)
    quote_tree.column("service_description", anchor=tk.W, width=150)

    quote_tree.heading("#0", text='', anchor=tk.W)
    quote_tree.heading("quotation_number", text="quotation_number", anchor=tk.W)
    quote_tree.heading("client_name", text="client_name", anchor=tk.W)
    quote_tree.heading("service_description", text="service_description", anchor=tk.W)

    quote_tree.pack()



quotation()

emp_frame = tk.Frame(employee_reg_tab, bg="#5b93a6")
emp_frame.pack()



home_root.mainloop() 