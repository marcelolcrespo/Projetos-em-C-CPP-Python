"""import time

from PIL import Image
import pyautogui as pyag

def rgb(img_path, x, y):
    im = Image.open(img_path).convert('RGB')
    r, g, b = im.getpixel((x, y))
    a = (r, g, b)
    return a


img = 'HP100%'
print (rgb(img, 5, 0))
pixel = pyag.pixel(100, 0)
print(pixel)
#img = 'HP100%.png'
time.sleep(2)
im = pyag.screenshot('vidaTempoReal.png', region=(233, 77, 117, 2))
pix = im.getpixel((100, 0))

print(pix)   #Printar o pixel encontrado na img gerada nas cords (100, 0)
"""

