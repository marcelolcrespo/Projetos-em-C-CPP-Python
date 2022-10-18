#from PIL import Image
#import numpy as np
#import matplotlib.pyplot as plt
from PIL import Image

barra = 117
conta = 0
i = 2
for c in range(50):
    Image1 = Image.open('C:/Users/Marcelo/Desktop/Calc Program/MP100%.png')
    conta = barra * i/100
    croppedIm = Image1.crop((conta.__ceil__(), 0, 116, 1))
    crop = croppedIm.save(f"MP{100 - i}%.png")
    i += 2

    #if i % 25 == 0:
        #print('\n')
    #print(f'{conta.__ceil__()}', end='  ')

    #https://www.geeksforgeeks.org/python-pil-image-save-method/