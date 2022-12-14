import time
from PIL import Image
import cv2
import sys
import pytesseract as pyt
import pyautogui as pyag


def checkGameOpen():
    while pyag.locateOnScreen('manaShield.png'):
        pyt.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-ocr\\tesseract.exe"

        im = pyag.screenshot('my_screenshot.png', region=(1304, 301, 54, 31))
        c = pyt.image_to_string(Image.open('my_screenshot.png'))
        print(c)
        time.sleep(2)


while True:
    checkGameOpen()


