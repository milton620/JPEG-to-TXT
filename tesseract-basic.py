'''import cv2

import pytesseract

img = CV2.imread("mm.jpg")

pyt.pytesseract.tesseract_cmd = "C:\\Users\\Milton\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe"


text = pyt.image_to_string(img)

print(text)
'''


import pytesseract
from PIL import Image
import os

input_folder = 'images/'
output_folder = 'text/'
pytesseract.pytesseract.tesseract_cmd = r"C:\Users\Milton\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"

for image_name in os.listdir(input_folder):
    print(f"Processing {image_name}") 
    
    image_path = os.path.join(input_folder, image_name)
    image = Image.open(image_path)

    text = pytesseract.image_to_string(image)
    
    output_path = os.path.join(output_folder, image_name.replace(".jpg", ".txt"))
    
    with open(output_path, "w") as text_file:
        text_file.write(text)
        

print("OCR extraction completed!")