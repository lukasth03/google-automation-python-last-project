#!/usr/bin/env python3

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import datetime

def generate_report(title, paragraph, attachement):
    c = canvas.Canvas(attachement, pagesize=letter)
    width, height = letter
    
    # Set up fonts and sizes
    c.setFont("Helvetica", 12)
    
    # Title: Processed Update on <Today's date>
    today_date = datetime.date.today().strftime("%Y-%m-%d")
    title_text = title.format(today_date)
    c.drawString(50, height - 50, title_text)
    
    # Add blank line
    c.drawString(50, height - 70, "")
    
    # Iterate over items and add to the report
    y_offset = height - 90
    for item in paragraph:
        c.drawString(50, y_offset, f"name: {item['name']}")
        c.drawString(50, y_offset - 20, f"weight: {item['weight']} lbs")
        # Add blank line
        c.drawString(50, y_offset - 40, "")
        y_offset -= 60
    
    c.save()