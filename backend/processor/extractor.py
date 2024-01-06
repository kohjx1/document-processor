try:
    from PIL import Image
except ImportError:
    import Image
import cv2
import pytesseract
from pytesseract import Output
import os
import numpy as np
import pandas as pd
import re
from pdf2image import convert_from_bytes


def extractText(data):
    print(data)
    PATH = os.getcwd()
    file_list = [f for f in os.listdir(path=PATH) if f.endswith('.pdf') or f.endswith('.PDF')]
    print(file_list)
    for file in file_list:
        pdf_file = convert_from_bytes(pdf_file=open(os.path.join(PATH,file), 'rb').read(),output_folder="./",fmt="png",output_file="test", paths_only=True)
        img = cv2.imread(pdf_file[0])
        im = Image.open(pdf_file[0])
        # print(data.arr_normalized_bb[0]['tag'])
        # math function
        x = int(im.width * data.arr_normalized_bb[0]['left'] / 100)
        y = int(im.height * data.arr_normalized_bb[0]['top'] /100)
        width = int(im.width * data.arr_normalized_bb[0]['right'] / 100) - x 
        height = int(im.height * data.arr_normalized_bb[0]['bottom'] / 100) - y
        print(x,y,width,height)
        rgb = cv2.cvtColor(img[y:y+height, x:x+width], cv2.COLOR_BGR2RGB)
        text = pytesseract.image_to_string(rgb,config='--psm 12')
        print(text)
    return text

    


