import os
import sys
from PIL import Image

# folder names can be changed appropriately
IMAGE_FOLDER = sys.argv[1]
NEW_FOLDER = sys.argv[2]

image_files = os.listdir(IMAGE_FOLDER)

if not os.path.exists(NEW_FOLDER):
    os.mkdir(NEW_FOLDER)
    
for image in image_files:
    name, extension = os.path.splitext(image)
    new_image = name + ".png"
    if image != new_image:
        try:
            with Image.open(f'{IMAGE_FOLDER}/{image}') as im:
                im.save(f'{NEW_FOLDER}/{new_image}')
                print(f'Processed image {image} into image {new_image}')
        except OSError:
            print("cannot convert", image)