import random

green = 1- random.random()
blue = green * random.random()
red = blue * random.random()
print(green,blue,red,green+blue+red, sep="\n")