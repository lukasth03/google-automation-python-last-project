#!/usr/bin/env python3

import os
import reports
import run
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


def generate_email(sender_email, receiver_email, subject, message_body, attachment_path=None):
    # Create a multipart message
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject

    # Add body to email
    message.attach(MIMEText(message_body, "plain"))

    # Add attachment if provided
    if attachment_path:
        with open(attachment_path, "rb") as attachment:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header(
            "Content-Disposition",
            f"attachment; filename= {attachment_path}",
        )
        message.attach(part)

    return message


def send_email(message):
    mail_server = smtplib.SMTP('localhost')
    mail_server.send_message(message)
    mail_server.quit()



if __name__ == "__main__":
    fruit_catalog = run.get_fruit_catalog()

    report = reports.generate_report(attachement='/tmp/processed.pdf', title='Processed Update on ', paragraph=fruit_catalog)

    sender_email = "automation@example.com"
    receiver_email = "student@example.com"
    subject = "Upload Completed - Online Fruit Store"
    message_body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
    attachment_path = '/tmp/processed.pdf'

    message = generate_email(sender_email, receiver_email, subject, message_body, attachment_path)
    send_email(message)

