#!/usr/bin/env python3

import requests
import os

url = "http://34.168.221.147/upload/"
images_path = '/home/student/supplier-data/images'

for file in os.listdir(images_path):
    if file.lower().endswith('.jpeg'):
        image_path = os.path.join(images_path, file)
        with open(image_path, 'rb') as opened:
            response = requests.post(url, files={'file': opened})
        if response.status_code == 201:
            print("Feedback uploaded successfully.")
        else:
            print("Error uploading feedback. Status code:", response.status_code)