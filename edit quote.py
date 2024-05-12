""" import tkinter as tk
from tkinter import ttk
from Home_page import *


quote_notebook=ttk.Notebook(quotation_tab)
create_quote_tab=tk.Frame(quote_notebook)
Home_page.view_quote_tab=tk.Frame(quote_notebook)
edit_quote_tab=tk.Frame(quote_notebook)
response_tab=tk.Frame(quote_notebook)

quote_notebook.add(create_quote_tab,text='CreateNew')
quote_notebook.add(Home_page.view_quote_tab,text='Viewquotations')
quote_notebook.add(edit_quote_tab,text='Editexisting')
quote_notebook.add(response_tab,text="Responseandupdates")
quote_notebook.pack(expand=True,fill='both')

#createnewquotationsection
view_quote_frame=tk.Frame(view_quote_tab)
view_quote_frame.pack(side="left")

#creatinglabalsandEntriesforthenewquotation
#tk.Label(view_quote_frame,text="CREATENEWQUOTATIONBELOW").pack(side='top')
tk.Label(view_quote_frame,text="Quotationnumber").grid(row=0,column=0,pady=5)
tk.Label(view_quote_frame,text="Clientname").grid(row=1,column=0,pady=5)
tk.Label(view_quote_frame,text="Clientcontact").grid(row=2,column=0,pady=5)
tk.Label(view_quote_frame,text="Clientemail").grid(row=3,column=0,pady=5)
tk.Label(view_quote_frame,text="Applicationtype").grid(row=4,column=0,pady=5)

quote_num_entry=tk.Entry(view_quote_frame,width=30)
quote_num_entry.grid(row=0,column=1,pady=5)
client_name_entry=tk.Entry(view_quote_frame,width=30)
client_name_entry.grid(row=1,column=1,pady=5)
client_contact_entry=tk.Entry(view_quote_frame,width=30)
client_contact_entry.grid(row=2,column=1,pady=5)
client_email_entry=tk.Entry(view_quote_frame,width=30)
client_email_entry.grid(row=3,column=1,pady=5)

#dropdownfortheapplicationtype
app_types=["Selectapplicationtype","DesktopApplication","WebApplication","Web(Static)","Website(Dynamic)","MobileApplication"]
app_type_combo=ttk.Combobox(view_quote_frame,value=app_types)
app_type_combo.current(0)
app_type_combo.bind("<<ComboboxSelected>>")
app_type_combo.grid(row=4,column=1,pady=5)

#Creatingatextareaforservicedescription
service_description=tk.Text(view_quote_frame,bg='#edead5',height=15,width=25,padx=20,pady=20)
service_description.grid(row=5,column=0,columnspan=3)

tk.Label(view_quote_frame,text="Servicecost").grid(row=6,column=0,pady=5)
service_cost=tk.Entry(view_quote_frame,width=30)
service_cost.grid(row=6,column=1,pady=5)

#creatingatablethatshowdetailsofthequotationscreated
quote_table_frame=tk.Frame(create_quote_tab)
quote_table_frame.pack(side="right")

#createquotationbutton
create_quote_button=tk.Button(quote_table_frame,text="Createquotation")
create_quote_button.pack(side='top',pady=20,padx=20)


view_quote_tree=ttk.Treeview(quote_table_frame)

view_quote_tree['columns']=("quotation_number","client_name","service_description")
view_quote_tree.column("#0",width=0,stretch=tk.NO)
view_quote_tree.column("quotation_number",anchor=tk.W,width=150)
view_quote_tree.column("client_name",anchor=tk.W,width=150)
view_quote_tree.column("service_description",anchor=tk.W,width=150)

view_quote_tree.heading("#0",text='',anchor=tk.W)
view_quote_tree.heading("quotation_number",text="quotation_number",anchor=tk.W)
view_quote_tree.heading("client_name",text="client_name",anchor=tk.W)
view_quote_tree.heading("service_description",text="service_description",anchor=tk.W)

view_quote_tree.pack()


edit_quotation() """




    """ view_quote_frame = tk.Frame(view_quote_tab)
    view_quote_frame.pack(side="left")

    #creating labals and Entries for the new quotation
    #tk.Label(view_quote_frame, text="CREATE NEW QUOTATION BELOW").pack(side='top')
    tk.Label(view_quote_frame, text="Quotation number").grid(row=0, column=0, pady=5)
    tk.Label(view_quote_frame, text="Client name").grid(row=1, column=0, pady=5)
    tk.Label(view_quote_frame, text="Client contact").grid(row=2, column=0, pady=5)
    tk.Label(view_quote_frame, text="Client email").grid(row=3, column=0, pady=5)
    tk.Label(view_quote_frame, text="Application type").grid(row=4, column=0, pady=5)

    quote_num_entry = tk.Entry(view_quote_frame, width =30)
    quote_num_entry.grid(row=0, column=1, pady=5)
    client_name_entry = tk.Entry(view_quote_frame, width=30)
    client_name_entry.grid(row=1, column=1, pady=5)
    client_contact_entry = tk.Entry(view_quote_frame, width=30)
    client_contact_entry.grid(row=2, column=1, pady=5)
    client_email_entry = tk.Entry(view_quote_frame, width=30)
    client_email_entry.grid(row=3, column=1, pady=5)
    
    #drop down for the application type
    app_types = ["Select application type" ,"Desktop Application", "Web Application", "Web (Static)", "Website (Dynamic)", "Mobile Application"]
    app_type_combo = ttk.Combobox(view_quote_frame, value=app_types)
    app_type_combo.current(0)
    app_type_combo.bind("<<ComboboxSelected>>")
    app_type_combo.grid(row=4, column=1, pady=5)

    # Creating a text area for service description
    service_description = tk.Text(view_quote_frame, bg='#edead5', height=15, width=25, padx=20,pady=20)
    service_description.grid(row=5, column=0, columnspan=3)

    tk.Label(view_quote_frame, text="Service cost").grid(row=6, column=0, pady=5)
    service_cost = tk.Entry(view_quote_frame, width=30)
    service_cost.grid(row=6, column=1, pady=5)

    # creating a table that show details of the quotations created
    view_quote_table_frame = tk.Frame(view_quote_tab)
    view_quote_table_frame.pack(side="right")

    #create quotation button
    update_quote_button = tk.Button(view_quote_table_frame, text="Update quotation")
    update_quote_button.pack(side='top', pady=20, padx=20)


    view_quote_tree = ttk.Treeview(view_quote_table_frame)

    view_quote_tree['columns'] = ("quotation_number", "client_name","service_description", "status")
    view_quote_tree.column("#0", width=0, stretch=tk.NO)
    view_quote_tree.column("quotation_number", anchor=tk.W, width=150)
    view_quote_tree.column("client_name", anchor=tk.W, width=150)
    view_quote_tree.column("service_description", anchor=tk.W, width=150)
    view_quote_tree.column("status", anchor=tk.W, width=150)

    view_quote_tree.heading("#0", text='', anchor=tk.W)
    view_quote_tree.heading("quotation_number", text="quotation_number", anchor=tk.W)
    view_quote_tree.heading("client_name", text="client_name", anchor=tk.W)
    view_quote_tree.heading("service_description", text="service_description", anchor=tk.W)
    view_quote_tree.heading("status", text="status",anchor=tk.W)

 """

 load_emp_entry = tk.Entry(user_account_frame1, width=40)
    load_emp_entry.grid(row=1, column=1,pady=3)
    user_fullname_entry = tk.Entry(user_account_frame1, width=40)
    user_fullname_entry.grid(row=2, column=1,pady=3)
    transaction_id_entry = tk.Entry(user_account_frame1, width=40)
    transaction_id_entry.grid(row=3, column=1,pady=3)
    amount_entry = tk.Entry(user_account_frame1, width=40)
    amount_entry.grid(row=4, column=1,pady=3)
    password_entry = tk.Entry(user_account_frame1, width=40)
    password_entry.grid(row=5, column=1,pady=3)
    accesslevel_entry = tk.Entry(user_account_frame1, width=40)
    accesslevel_entry.grid(row=6, column=1,pady=3)



  other_activities_income["columns"] = ("transaction_id", "amount", "deposit_date")
    
    other_activities_income.column("#0", stretch=tk.NO, width=0)
    other_activities_income.column("transaction_id", anchor=tk.CENTER,  width=100)
    other_activities_income.column("amount", anchor=tk.CENTER,  width=100)
    other_activities_income.column("deposit_date",  anchor=tk.CENTER, width=100)

    other_activities_income.heading("#0", text="", anchor=tk.W)
    other_activities_income.heading("transaction_id", text="Transaction id", anchor=tk.W)
    other_activities_income.heading("amount", text="Amount", anchor=tk.W)
    other_activities_income.heading("deposit_date", text="Deposit dat", anchor=tk.W)

    other_activities_income.pack()
