from pytesser import *
import ImageEnhance

image = Image.open('C:/Users/Administrator/Desktop/result.png')
bg = Image.new("RGB", image.size, (255,255,255))
bg.paste(image,image)
str = image_to_string(bg)
print(str)