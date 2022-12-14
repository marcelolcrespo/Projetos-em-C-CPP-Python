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