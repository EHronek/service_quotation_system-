""" import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from tkcalendar import DateEntry
from datetime import datetime
import sqlite3
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# Database setup
def setup_db():
    conn = sqlite3.connect('projects.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS projects (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            client_id TEXT,
            client_name TEXT,
            client_email TEXT,
            project_title TEXT,
            project_start TEXT,
            project_end TEXT,
            project_deadline TEXT,
            project_updates TEXT
        )
    ''')
    conn.commit()
    conn.close()

# Insert data into database
def insert_data(client_id, client_name, client_email, project_title, project_start, project_end, project_deadline, project_updates):
    conn = sqlite3.connect('projects.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO projects (client_id, client_name, client_email, project_title, project_start, project_end, project_deadline, project_updates)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', (client_id, client_name, client_email, project_title, project_start, project_end, project_deadline, project_updates))
    conn.commit()
    conn.close()
    load_data()

# Load data from database
def load_data():
    conn = sqlite3.connect('projects.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM projects')
    rows = cursor.fetchall()
    for row in tree.get_children():
        tree.delete(row)
    for row in rows:
        tree.insert("", "end", values=row[1:])
    conn.close()

# Calculate and display the deadline
def calculate_deadline():
    try:
        start_date = cal_start.get_date()
        end_date = cal_end.get_date()
        if start_date and end_date and start_date <= end_date:
            deadline = end_date.strftime('%Y-%m-%d')
            entry_deadline.config(state=tk.NORMAL)
            entry_deadline.delete(0, tk.END)
            entry_deadline.insert(0, deadline)
            entry_deadline.config(state=tk.DISABLED)
        else:
            messagebox.showerror("Input Error", "End date must be after start date.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Submit button action
def submit_action():
    client_id = entry_client_id.get()
    client_name = entry_client_name.get()
    client_email = entry_client_email.get()
    project_title = entry_project_title.get()
    project_start = cal_start.get_date().strftime('%Y-%m-%d')
    project_end = cal_end.get_date().strftime('%Y-%m-%d')
    project_deadline = entry_deadline.get()
    project_updates = entry_project_updates.get("1.0", tk.END)

    if not client_id or not client_name or not client_email or not project_title or not project_start or not project_end or not project_deadline or not project_updates:
        messagebox.showerror("Input Error", "All fields are required.")
        return

    insert_data(client_id, client_name, client_email, project_title, project_start, project_end, project_deadline, project_updates)
    messagebox.showinfo("Success", "Project details saved successfully.")
    generate_pdf(client_id, client_name, client_email, project_title, project_start, project_end, project_deadline, project_updates)
    send_email(client_email, client_name, "Project Details", "Please find the attached project details.", "project_details.pdf")
    clear_inputs()

# Clear input fields
def clear_inputs():
    entry_client_id.delete(0, tk.END)
    entry_client_name.delete(0, tk.END)
    entry_client_email.delete(0, tk.END)
    entry_project_title.delete(0, tk.END)
    cal_start.set_date(datetime.today())
    cal_end.set_date(datetime.today())
    entry_deadline.config(state=tk.NORMAL
 """

import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os
import datetime
from new_base_model import Organization, Quotation, Client
from new_session import setup_db
from create_quote import generate_pdf_from_client

session = setup_db('root', 'root', 'sysdb')


def load_quote():
    try:
        quote_num = load_entry.get()
        quote = session.query(Quotation).filter(Quotation.quotation_number == quote_num).first()
        client = session.query(Client).filter(Client.client_name == quote.client_name).first()
        messagebox.showinfo("Success", "Successful retrieval of data")
        return quote, client

    except Exception as e:
        messagebox.showerror("Error", "Error loading quotation, input correct quote_num")

    finally:
        session.close()
def gen_quote():
    quote, client = load_quote()
    generate_pdf_from_client("quotation_e.pdf", client, quote)


# Function to send email with attachment
def send_email():
    recipient = entry_recipient.get()
    subject = entry_subject.get()
    message = text_message.get("1.0", tk.END)

    if not recipient or not subject or not message:
        messagebox.showerror("Error", "Please fill in all fields.")
        return

    try:
        # Create message container
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient
        msg['Subject'] = subject

        # Add message body
        body = message
        msg.attach(MIMEText(body, 'plain'))

        # Add attachment
        attachment_path = attachment_var.get()
        if attachment_path:
            attachment_name = os.path.basename(attachment_path)
            attachment = open(attachment_path, "rb")
            part = MIMEBase('application', 'octet-stream')
            part.set_payload((attachment).read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', "attachment; filename= %s" % attachment_name)
            msg.attach(part)

        # Send the email
        server.sendmail(sender_email, recipient, msg.as_string())
        messagebox.showinfo("Success", "Email sent successfully.")

    except Exception as e:
        messagebox.showerror("Error", str(e))

# Function to generate receipt file
""" def generate_receipt():
    client_name = entry_client_name.get()
    project_title = entry_project_title.get()
    start_date = entry_start_date.get()

    if not client_name or not project_title or not start_date:
        messagebox.showerror("Error", "Please fill in all fields.")
        return

    # Create filename based on client name and project title
    filename = f"Receipt_{client_name}_{project_title}.txt"
    receipt_path = os.path.join(os.getcwd(), filename)

    # Generate receipt content
    receipt_content = f"Client Name: {client_name}\nProject Title: {project_title}\nStart Date: {start_date}\n"

    # Write receipt content to file
    with open(receipt_path, 'w') as f:
        f.write(receipt_content)

    messagebox.showinfo("Success", f"Receipt generated successfully: {receipt_path}")
 """
# Function to browse and select attachment file
def browse_file():
    filename = filedialog.askopenfilename()
    if filename:
        attachment_var.set(filename)

# Main application
root = tk.Tk()
root.title("Email Client")
root.geometry("500x400")

# Email Settings
try:
    org = session.query(Organization).filter(Organization.organization_id == 1).one_or_none()
    sender_email = org.organization_email
    password = org.email_password
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, password)
except Exception as e:
    messagebox.showerror(title="Email Error", message=f"something went wrong while trying to communicate: {e}")
finally:
    session.close()

# Entry Fields
tk.Label(root, text="Recipient Email:").grid(row=0, column=0, padx=10, pady=5)
entry_recipient = tk.Entry(root)
entry_recipient.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Subject:").grid(row=1, column=0, padx=10, pady=5)
entry_subject = tk.Entry(root)
entry_subject.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Message:").grid(row=2, column=0, padx=10, pady=5)
text_message = tk.Text(root, width=30, height=10)
text_message.grid(row=2, column=1, padx=10, pady=5)

attachment_var = tk.StringVar()
tk.Label(root, text="Attachment:").grid(row=3, column=0, padx=10, pady=5)
entry_attachment = tk.Entry(root, textvariable=attachment_var, width=40)
entry_attachment.grid(row=3, column=1, padx=10, pady=5)
tk.Button(root, text="Browse", command=browse_file).grid(row=3, column=2, padx=5, pady=5)

# Receipt Details
""" tk.Label(root, text="Client Name:").grid(row=4, column=0, padx=10, pady=5)
entry_client_name = tk.Entry(root)
entry_client_name.grid(row=4, column=1, padx=10, pady=5) """

""" tk.Label(root, text="Project Title:").grid(row=5, column=0, padx=10, pady=5)
entry_project_title = tk.Entry(root)
entry_project_title.grid(row=5, column=1, padx=10, pady=5)
 """
""" tk.Label(root, text="Start Date:").grid(row=6, column=0, padx=10, pady=5)
entry_start_date = tk.Entry(root)
entry_start_date.insert(0, datetime.datetime.now().strftime("%Y-%m-%d"))
entry_start_date.grid(row=6, column=1, padx=10, pady=5) """

# Buttons
tk.Button(root, text="Send Email", command=send_email).grid(row=4, column=2, padx=10, pady=5)
#tk.Button(root, text="Generate Receipt", command=generate_receipt).grid(row=7, column=1, padx=10, pady=5)
tk.Button(root, text="Generate quotation", command=gen_quote).grid(row=5, column=0)
tk.Button(root, text="loadquotation", command=load_quote).grid(row=6, column=0, pady=10)
load_entry = tk.Entry(root, width=40)
load_entry.grid(row=6, column=1, pady=10)
root.mainloop()
