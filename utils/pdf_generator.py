from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import os

def generate_pdf(sender_name, sender_address, receiver_name, receiver_address, delivery_id, output_path="output"):
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    file_path = os.path.join(output_path, f"delivery_{delivery_id}.pdf")
    c = canvas.Canvas(file_path, pagesize=A4)
    width, height = A4

    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, height - 50, "Delivery Label")

    c.setFont("Helvetica", 12)
    c.drawString(50, height - 100, f"Delivery ID: {delivery_id}")

    c.drawString(50, height - 150, "Sender Information:")
    c.drawString(70, height - 170, f"Name: {sender_name}")
    c.drawString(70, height - 190, f"Address: {sender_address}")

    c.drawString(50, height - 240, "Receiver Information:")
    c.drawString(70, height - 260, f"Name: {receiver_name}")
    c.drawString(70, height - 280, f"Address: {receiver_address}")

    barcode_path = os.path.join(output_path, f"{delivery_id}.png")
    if os.path.exists(barcode_path):
        c.drawImage(barcode_path, 50, height - 400, width=200, preserveAspectRatio=True)

    c.showPage()
    c.save()
    return file_path
