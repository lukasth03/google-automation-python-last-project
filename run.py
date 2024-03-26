#! /usr/bin/env python3

import os
import requests

def get_fruit_catalog():
    files_path = '/home/student/supplier-data/descriptions'
    fruit_catalog = []

    for file in os.listdir(files_path):
        file_path = os.path.join(files_path, file)
        if file.lower().endswith('.txt'):
            with open(file_path, 'r') as file:
                fruit = {}
                file_name = os.path.basename(file.name)
                parts = file_name.split('.')
                new_file_name = '.'.join(parts[:-1]) + '.jpeg'
                
                fruit['name'] = file.readline().strip()
                fruit['weight'] = int(file.readline().strip().split()[0])
                fruit['description'] = file.readline().strip()
                fruit['image_name'] = os.path.join(files_path, new_file_name)
                fruit_catalog.append(fruit)
    
    return fruit_catalog

fruit_catalog = get_fruit_catalog()
url = 'http://34.168.221.147/fruits/'

for fruit in fruit_catalog:
    response = requests.post(url, json=fruit)
    if response.status_code == 201:
            print("Feedback uploaded successfully.")
    else:
            print("Error uploading feedback. Status code:", response.status_code)

