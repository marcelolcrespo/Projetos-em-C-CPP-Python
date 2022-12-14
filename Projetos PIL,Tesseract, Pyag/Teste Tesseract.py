import os

import pyautogui
import pytesseract
import sys
import argparse
import time
try:
    import Image
except ImportError:
    from PIL import Image

from subprocess import check_output
pytesseract.pytesseract.tesseract_cmd="C:\\Program Files\\Tesseract-ocr\\tesseract.exe"

#print(c)
name = 'Fora de Alcance'
while True:
    try:
        time.sleep(1)
        #im = pyautogui.screenshot('zer.png', region=(92, 149, 200, 363))
        c = pytesseract.image_to_string(Image.open('img7.png'))
        """if name in pytesseract.image_to_string(Image.open('foraAlcance.png')):
            print('True')"""
        print(c)
    except:
        print('Nova tentativa')