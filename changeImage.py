#!/usr/bin/env python3

from PIL import Image
import os

image_size = (600, 400)
images_path = '/home/student/supplier-data/images'
destination = '/home/student/supplier-data/images'

for file in os.listdir(images_path):
    image_path = os.path.join(images_path, file)
    if file.lower().endswith(('.tiff')):
        image = Image.open(image_path)
        new_image = image.convert('RGB').resize(image_size)
        new_image.save(os.path.join(destination, os.path.splitext(file)[0] + '.jpeg'))
    image.close()