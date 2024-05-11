import tkinter as tk
from tkinter import ttk
from Home_page import *


"""quote_notebook=ttk.Notebook(quotation_tab)
create_quote_tab=tk.Frame(quote_notebook)
Home_page.view_quote_tab=tk.Frame(quote_notebook)
edit_quote_tab=tk.Frame(quote_notebook)
response_tab=tk.Frame(quote_notebook)

quote_notebook.add(create_quote_tab,text='CreateNew')
quote_notebook.add(Home_page.view_quote_tab,text='Viewquotations')
quote_notebook.add(edit_quote_tab,text='Editexisting')
quote_notebook.add(response_tab,text="Responseandupdates")
quote_notebook.pack(expand=True,fill='both')"""

#createnewquotationsection
edit_quote_frame=tk.Frame(view_quote_tab)
edit_quote_frame.pack(side="left")

#creatinglabalsandEntriesforthenewquotation
#tk.Label(edit_quote_frame,text="CREATENEWQUOTATIONBELOW").pack(side='top')
tk.Label(edit_quote_frame,text="Quotationnumber").grid(row=0,column=0,pady=5)
tk.Label(edit_quote_frame,text="Clientname").grid(row=1,column=0,pady=5)
tk.Label(edit_quote_frame,text="Clientcontact").grid(row=2,column=0,pady=5)
tk.Label(edit_quote_frame,text="Clientemail").grid(row=3,column=0,pady=5)
tk.Label(edit_quote_frame,text="Applicationtype").grid(row=4,column=0,pady=5)

quote_num_entry=tk.Entry(edit_quote_frame,width=30)
quote_num_entry.grid(row=0,column=1,pady=5)
client_name_entry=tk.Entry(edit_quote_frame,width=30)
client_name_entry.grid(row=1,column=1,pady=5)
client_contact_entry=tk.Entry(edit_quote_frame,width=30)
client_contact_entry.grid(row=2,column=1,pady=5)
client_email_entry=tk.Entry(edit_quote_frame,width=30)
client_email_entry.grid(row=3,column=1,pady=5)

#dropdownfortheapplicationtype
app_types=["Selectapplicationtype","DesktopApplication","WebApplication","Web(Static)","Website(Dynamic)","MobileApplication"]
app_type_combo=ttk.Combobox(edit_quote_frame,value=app_types)
app_type_combo.current(0)
app_type_combo.bind("<<ComboboxSelected>>")
app_type_combo.grid(row=4,column=1,pady=5)

#Creatingatextareaforservicedescription
service_description=tk.Text(edit_quote_frame,bg='#edead5',height=15,width=25,padx=20,pady=20)
service_description.grid(row=5,column=0,columnspan=3)

tk.Label(edit_quote_frame,text="Servicecost").grid(row=6,column=0,pady=5)
service_cost=tk.Entry(edit_quote_frame,width=30)
service_cost.grid(row=6,column=1,pady=5)

#creatingatablethatshowdetailsofthequotationscreated
quote_table_frame=tk.Frame(create_quote_tab)
quote_table_frame.pack(side="right")

#createquotationbutton
create_quote_button=tk.Button(quote_table_frame,text="Createquotation")
create_quote_button.pack(side='top',pady=20,padx=20)


quote_tree=ttk.Treeview(quote_table_frame)

quote_tree['columns']=("quotation_number","client_name","service_description")
quote_tree.column("#0",width=0,stretch=tk.NO)
quote_tree.column("quotation_number",anchor=tk.W,width=150)
quote_tree.column("client_name",anchor=tk.W,width=150)
quote_tree.column("service_description",anchor=tk.W,width=150)

quote_tree.heading("#0",text='',anchor=tk.W)
quote_tree.heading("quotation_number",text="quotation_number",anchor=tk.W)
quote_tree.heading("client_name",text="client_name",anchor=tk.W)
quote_tree.heading("service_description",text="service_description",anchor=tk.W)

quote_tree.pack()


edit_quotation()