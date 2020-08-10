# Displays an image passed as a variable on the InkyPHAT.

from inky import InkyPHAT

inky_display = InkyPHAT("red")
inky_display.h_flip = True
inky_display.v_flip = True

from PIL import Image, ImageFont, ImageDraw
img = Image.new("P", (inky_display.WIDTH, inky_display.HEIGHT))
draw = ImageDraw.Draw(img)

def image (file):
    inky_display.set_border(inky_display.BLACK)
    img = Image.open(file)
    inky_display.set_image(img)
    inky_display.show()
