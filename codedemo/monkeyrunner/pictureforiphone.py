from pytesser import *
import ImageEnhance

image = Image.open('C:/Users/Administrator/Desktop/snap.png')
enhancer = ImageEnhance.Contrast(image)
image_enhancer = enhancer.enhance(4)
str = image_to_string(image_enhancer)
print(str)