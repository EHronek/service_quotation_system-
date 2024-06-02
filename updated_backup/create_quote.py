"""  from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.lib import colors
 """




def generate_pdf_from_client(output_path, client, quotation):
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib.units import inch
    from reportlab.pdfgen import canvas
    from reportlab.lib import colors

    


    c = canvas.Canvas(output_path, pagesize=A4)
    width, height = A4

    # Add organization name
    c.setFont("Helvetica-Bold", 28)
    c.setFillColor(colors.HexColor("#003366"))
    c.drawCentredString(width / 2, height - 50, "System Dev Solution")

    # Add mission statement
    c.setFont("Helvetica", 14)
    mission_text = "Our mission is to deliver high-quality software solutions and services to our clients."
    c.drawCentredString(width / 2, height - 80, mission_text)

    # Add basic services section with blue background
    c.setFillColor(colors.HexColor("#cfe2f3"))
    c.rect(30, height - 120, width - 60, 50, stroke=0, fill=1)
    c.setFillColor(colors.HexColor("#003366"))
    c.setFont("Helvetica-Bold", 16)
    basic_services = "Software Development, Web Hosting, Web Development, Hardware Services"
    c.drawCentredString(width / 2, height - 95, basic_services)

    # Add "Service Quotation for" section
    c.setFont("Helvetica", 12)
    c.setFillColor(colors.black)
    c.drawString(30, height - 170, f"Service Quotation for: {quotation.application_type}")

    # Add sections for "Quotation shipped to" and "Quotation details"
    c.setFont("Helvetica-Bold", 12)
    c.drawString(30, height - 210, "Quotation shipped to")
    c.line(30, height - 215, width / 2 - 20, height - 215)

    c.setFont("Helvetica", 12)
    c.drawString(30, height - 230, f"Name: {client.client_name}")
    c.drawString(30, height - 250, f"Contact: {client.contact}")
    c.drawString(30, height - 270, f"Email: {client.email}")

    c.setFont("Helvetica-Bold", 12)
    c.drawString(width / 2 + 20, height - 210, "Quotation details")
    c.line(width / 2 + 20, height - 215, width - 30, height - 215)

    c.setFont("Helvetica", 12)
    c.drawString(width / 2 + 20, height - 230, f"Quotation number: {quotation.quotation_number}")
    c.drawString(width / 2 + 20, height - 250, f"Quotation date: {quotation.quotation_date.strftime('%m/%d/%Y')}")
    c.drawString(width / 2 + 20, height - 270, f"Service cost: Ksh{quotation.service_cost}")

    # Add service description section
    c.setFont("Helvetica-Bold", 12)
    c.drawString(30, height - 310, "Service Description")
    c.line(30, height - 315, width - 30, height - 315)
    c.setFont("Helvetica", 12)
    text = c.beginText(30, height - 335)
    text.setFont("Helvetica", 12)
    text.setLeading(14)
    text.textLines(quotation.service_description)
    c.drawText(text)

    # Footer
    c.setFont("Helvetica-Oblique", 10)
    c.drawCentredString(width / 2, 30, "Application developed and maintained by System Dev Solutions")

    c.save()


if __name__ == "__main__":
    
    from new_base_model import Quotation, Client
    from new_session import setup_db

    session =setup_db("root", "root", "sysdb")

    quotation = session.query(Quotation).filter(Quotation.quotation_number == "QT_108").one_or_none()
    client = session.query(Client).filter(Client.client_name == quotation.client_name).one_or_none()

    print(quotation.client_name)
    #print(str(client.client_name))

    generate_pdf_from_client("a_new.pdf", client, quotation) 