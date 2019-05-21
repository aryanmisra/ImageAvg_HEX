import numpy as np
from colormap import rgb2hex
from PIL import Image
from tkinter import Canvas, Tk
image = Image.open("image.jpg")
root = Tk()
def getAverageRGB(image):
  im = np.array(image)
  w,h,d = im.shape
  im.shape = (w*h, d)
  return tuple(np.average(im, axis=0))
rgb = getAverageRGB(image)
hex = rgb2hex(int(rgb[0]),int(rgb[1]),int(rgb[2]))
print(hex)
canvas = Canvas(width=400, height=400, bg=hex)
canvas.pack()
root.mainloop()
