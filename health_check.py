#!/usr/bin/env python3

import psutil
import socket
import report_email

sender_email = "automation@example.com"
receiver_email = "student@example.com"
message_body = "Please check your system and resolve the issue as soon as possible."

def check_cpu_usage():
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > 80:
        message = report_email.generate_email(sender_email, receiver_email, 'Error - CPU usage is over 80%', message_body)
        report_email.send_email(message)
    else:
        print('CPU is running fine.')

def check_disk_space():
    disk_usage = psutil.disk_usage('/')
    if disk_usage.percent > 80:
        message = report_email.generate_email(sender_email, receiver_email, 'Error - Available disk space is less than 20%', message_body)
        report_email.send_email(message)
    else:
        print('Disk space is sufficient.')

def check_memory():
    memory_usage = psutil.virtual_memory()
    if memory_usage.available < 100 * 1024 * 1024:  # Convert 100MB to bytes
        message = report_email.generate_email(sender_email, receiver_email, 'Error - Available memory is less than 100MB', message_body)
        report_email.send_email(message)
    else:
        print('Memory is sufficient.')

def check_hostname_resolution():
    try:
        ip_address = socket.gethostbyname('localhost')
        if ip_address != '127.0.0.1':
            message = report_email.generate_email(sender_email, receiver_email, 'Error - localhost cannot be resolved to 127.0.0.1', message_body)
            report_email.send_email(message)
        else:
            print('Hostname resolution is correct.')
    except socket.error:
        print('Error resolving hostname.')

if __name__ == "__main__":
    check_cpu_usage()
    check_disk_space()
    check_memory()
    check_hostname_resolution()