import cv2
import os
from tqdm import tqdm
from pytesseract import image_to_data, Output
import pandas as pd
import pytesseract
from PIL import Image, ImageDraw, ImageFont



# tesseract models for different languages
terms = {
    'bengali': 'ben',
    'gujarati': 'guj',
    'gurumukhi': 'pan',
    'hindi': 'hin',
    'kannada': 'kan',
    'malayalam': 'mal',
    'odia': 'ori',
    'tamil': 'tam',
    'telugu': 'tel',
    'urdu': 'urd'
}



img = cv2.imread('/home/ganesh/BADRI/MANUSCRIPTS/project/sample_data/images/RE4084/processed/p-27_1.jpg')
d = image_to_data(img, output_type=Output.DICT, lang='tam')
data = []
for i in range(len(d['level'])):
    if d['level'][i]==5:
        (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
        (x1, y1, w, h) = (int(x), int(y), int(w), int(h))
        cv2.rectangle(img, (x1, y1), (x1+w, y1+h), (0, 0, 255), 2)
        text = d['text'][i]
        data.append([text,x1, y1, x1+w, y1+h])
        
    
height, width, _ = img.shape
# width, height = 1024, 1024
background_color = "white"
img2 = Image.new("RGB", (width, height), background_color)
draw = ImageDraw.Draw(img2)

# try:
font = ImageFont.truetype('/usr/share/fonts/truetype/lohit-tamil/Lohit-Tamil.ttf', 30) 
for text, x1, y1, x2, y2 in data:
    draw.text((x1, y1), text, font=font, fill="black")
    
img2.save('temp2.png')
        
# # img = cv2.imread(os.path.join(args.input_folder,image))
# img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
# text = pytesseract.image_to_string(img, lang = 'tam')
# with open(os.path.join('temp.txt'), 'w') as f:
#     f.write(text)
    
    
        
cv2.imwrite('out.png', img)
    
    

    