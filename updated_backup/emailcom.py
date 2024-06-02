""" import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os
import datetime
from fpdf import FPDF

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

# Function to generate receipt PDF file
def generate_receipt():
    client_name = entry_client_name.get()
    project_title = entry_project_title.get()
    start_date = entry_start_date.get()
    end_date = entry_end_date.get()
    deadline_date = entry_deadline_date.get()

    if not client_name or not project_title or not start_date or not end_date or not deadline_date:
        messagebox.showerror("Error", "Please fill in all fields.")
        return

    # Create filename based on client name and project title
    filename = f"Receipt_{client_name}_{project_title}.pdf"
    receipt_path = os.path.join(os.getcwd(), filename)

    # Generate receipt content
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt="Project Receipt", ln=True, align='C')
    pdf.ln(10)

    pdf.cell(200, 10, txt=f"Client Name: {client_name}", ln=True)
    pdf.cell(200, 10, txt=f"Project Title: {project_title}", ln=True)
    pdf.cell(200, 10, txt=f"Start Date: {start_date}", ln=True)
    pdf.cell(200, 10, txt=f"End Date: {end_date}", ln=True)
    pdf.cell(200, 10, txt=f"Deadline: {deadline_date}", ln=True)

    pdf.ln(20)
    pdf.cell(200, 10, txt="Project Details", ln=True)
    pdf.multi_cell(0, 10, txt="Here you can include the details about the project. This includes milestones, "
                               "current status, and any other relevant information for the client.")

    pdf.output(receipt_path)

    messagebox.showinfo("Success", f"Receipt generated successfully: {receipt_path}")

# Function to browse and select attachment file
def browse_file():
    filename = filedialog.askopenfilename()
    if filename:
        attachment_var.set(filename)

# Auto calculate the deadline based on start and end dates
def calculate_deadline():
    try:
        start_date = datetime.datetime.strptime(entry_start_date.get(), '%Y-%m-%d')
        end_date = datetime.datetime.strptime(entry_end_date.get(), '%Y-%m-%d')
        deadline_date = end_date + datetime.timedelta(days=30)
        entry_deadline_date.set(deadline_date.strftime('%Y-%m-%d'))
    except ValueError:
        messagebox.showerror("Error", "Please enter valid dates in YYYY-MM-DD format.")

# Main application
root = tk.Tk()
root.title("Project Management")
root.geometry("600x500")

# Email Settings
sender_email = "ehronek6608@stu.kemu.ac.ke"
password = "ppwn kute humf pbmk"
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(sender_email, password)

# Entry Fields
tk.Label(root, text="Recipient Email:").grid(row=0, column=0, padx=10, pady=5)
entry_recipient = tk.Entry(root)
entry_recipient.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Subject:").grid(row=1, column=0, padx=10, pady=5)
entry_subject = tk.Entry(root)
entry_subject.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Message:").grid(row=2, column=0, padx=10, pady=5)
text_message = tk.Text(root, width=50, height=10)
text_message.grid(row=2, column=1, padx=10, pady=5)

attachment_var = tk.StringVar()
tk.Label(root, text="Attachment:").grid(row=3, column=0, padx=10, pady=5)
entry_attachment = tk.Entry(root, textvariable=attachment_var, width=30)
entry_attachment.grid(row=3, column=1, padx=10, pady=5)
tk.Button(root, text="Browse", command=browse_file).grid(row=3, column=2, padx=5, pady=5)

# Receipt Details
tk.Label(root, text="Client Name:").grid(row=4, column=0, padx=10, pady=5)
entry_client_name = tk.Entry(root)
entry_client_name.grid(row=4, column=1, padx=10, pady=5)

tk.Label(root, text="Project Title:").grid(row=5, column=0, padx=10, pady=5)
entry_project_title = tk.Entry(root)
entry_project_title.grid(row=5, column=1, padx=10, pady=5)

tk.Label(root, text="Start Date:").grid(row=6, column=0, padx=10, pady=5)
entry_start_date = tk.Entry(root)
entry_start_date.insert(0, datetime.datetime.now().strftime("%Y-%m-%d"))
entry_start_date.grid(row=6, column=1, padx=10, pady=5)

tk.Label(root, text="End Date:").grid(row=7, column=0, padx=10, pady=5)
entry_end_date = tk.Entry(root)
entry_end_date.grid(row=7, column=1, padx=10, pady=5)
entry_end_date.bind("<FocusOut>", lambda event: calculate_deadline())

tk.Label(root, text="Deadline:").grid(row=8, column=0, padx=10, pady=5)
entry_deadline_date = tk.StringVar()
tk.Entry(root, textvariable=entry_deadline_date, state='readonly').grid(row=8, column=1, padx=10, pady=5)

# Buttons
tk.Button(root, text="Send Email", command=send_email).grid(row=9, column=0, padx=10, pady=5)
tk.Button(root, text="Generate Receipt", command=generate_receipt).grid(row=9, column=1, padx=10, pady=5)

root.mainloop()
 """









import fitz  # PyMuPDF
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from tkcalendar import DateEntry
from datetime import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os

# Email setup (replace with your details)
sender_email = "your_email@example.com"
password = "your_password"
smtp_server = "smtp.example.com"
smtp_port = 587

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
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, recipient, msg.as_string())
        server.quit()

        messagebox.showinfo("Success", "Email sent successfully.")

    except Exception as e:
        messagebox.showerror("Error", str(e))

# Function to customize and save PDF
def customize_pdf(template_path, output_path, details):
    doc = fitz.open(template_path)
    page = doc[0]  # Assuming details need to be added to the first page

    # Example coordinates, need to be adjusted based on your template
    page.insert_text((100, 150), f"Name: {details['name']}")
    page.insert_text((100, 170), f"Contact: {details['contact']}")
    page.insert_text((100, 190), f"Email: {details['email']}")
    page.insert_text((100, 210), f"Quote number: {details['quote_number']}")
    page.insert_text((100, 230), f"Quotation date: {details['quote_date']}")
    page.insert_text((100, 250), f"Service cost: {details['service_cost']}")
    page.insert_text((100, 270), f"Service description: {details['service_description']}")

    doc.save(output_path)
    messagebox.showinfo("Success", f"Customized PDF saved as: {output_path}")

# Function to generate and send customized PDF
def generate_and_send_pdf():
    client_details = {
        "name": entry_client_name.get(),
        "contact": entry_contact.get(),
        "email": entry_email.get(),
        "quote_number": entry_quote_number.get(),
        "quote_date": cal_quote_date.get_date().strftime('%Y-%m-%d'),
        "service_cost": entry_service_cost.get(),
        "service_description": entry_service_description.get()
    }

    if any(not value for value in client_details.values()):
        messagebox.showerror("Error", "Please fill in all fields.")
        return

    template_path = "Quotation.pdf"
    output_path = f"Quotation_{client_details['name']}.pdf"
    customize_pdf(template_path, output_path, client_details)

    attachment_var.set(output_path)
    send_email()

# Main application
root = tk.Tk()
root.title("Quotation Management System")
root.geometry("600x600")

# Labels and Entry fields
tk.Label(root, text="Client Name:").grid(row=0, column=0, padx=10, pady=5)
entry_client_name = tk.Entry(root)
entry_client_name.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Contact:").grid(row=1, column=0, padx=10, pady=5)
entry_contact = tk.Entry(root)
entry_contact.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Email:").grid(row=2, column=0, padx=10, pady=5)
entry_email = tk.Entry(root)
entry_email.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Quote Number:").grid(row=3, column=0, padx=10, pady=5)
entry_quote_number = tk.Entry(root)
entry_quote_number.grid(row=3, column=1, padx=10, pady=5)

tk.Label(root, text="Quotation Date:").grid(row=4, column=0, padx=10, pady=5)
cal_quote_date = DateEntry(root, width=12, background='darkblue', foreground='white', borderwidth=2)
cal_quote_date.grid(row=4, column=1, padx=10, pady=5)

tk.Label(root, text="Service Cost:").grid(row=5, column=0, padx=10, pady=5)
entry_service_cost = tk.Entry(root)
entry_service_cost.grid(row=5, column=1, padx=10, pady=5)

tk.Label(root, text="Service Description:").grid(row=6, column=0, padx=10, pady=5)
entry_service_description = tk.Entry(root)
entry_service_description.grid(row=6, column=1, padx=10, pady=5)

# Generate and Send PDF Button
generate_send_button = tk.Button(root, text="Generate and Send PDF", command=generate_and_send_pdf)
generate_send_button.grid(row=7, column=1, padx=10, pady=10)

# Email Fields
tk.Label(root, text="Recipient Email:").grid(row=8, column=0, padx=10, pady=5)
entry_recipient = tk.Entry(root)
entry_recipient.grid(row=8, column=1, padx=10, pady=5)

tk.Label(root, text="Subject:").grid(row=9, column=0, padx=10, pady=5)
entry_subject = tk.Entry(root)
entry_subject.grid(row=9, column=1, padx=10, pady=5)

tk.Label(root, text="Message:").grid(row=10, column=0, padx=10, pady=5)
text_message = tk.Text(root, width=40, height=5)
text_message.grid(row=10, column=1, padx=10, pady=5)

# Attachment
attachment_var = tk.StringVar()
tk.Label(root, text="Attachment:").grid(row=11, column=0, padx=10, pady=5)
entry_attachment = tk.Entry(root, textvariable=attachment_var)
entry_attachment.grid(row=11, column=1, padx=10, pady=5)

root.mainloop()
