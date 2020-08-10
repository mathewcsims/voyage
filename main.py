######### Setup Inky #########

# This is boilerplate code to setup the InkyPHAT display. It probably doesn't all need to be duplicated
# in the way it is in some of the modules, but this can be cleaned up in a later version.

from inky import InkyPHAT

inky_display = InkyPHAT("red")
inky_display.set_border(inky_display.WHITE)
# Flip the display because the Pi Zero power socket would otherwise be on the bottom.
inky_display.h_flip = True
inky_display.v_flip = True

from PIL import Image, ImageFont, ImageDraw
img = Image.new("P", (inky_display.WIDTH, inky_display.HEIGHT))
draw = ImageDraw.Draw(img)

from font_fredoka_one import FredokaOne
font = ImageFont.truetype(FredokaOne, 13)
font_header = ImageFont.truetype(FredokaOne, 13)
font_large = ImageFont.truetype(FredokaOne, 18)

#########   #########

## Import Modules
import time # needed for delaying re-fetches of the data
import sys # needed for error handling

# Modules from the /modules dir
from modules.get import get
from modules.display import display
from modules.clean import clean
from modules.image import image

# Set address of Huxley API (where to fetch the data from)
huxley = "voyagems.azurewebsites.net"

# Create lists of origin and arrival stations to be queried
# This will be made interactive in a later version, but for now can be edited here.
origin = ["PEM", "WGN", "WGW"]
destination = ["MCO", "MAN", "MCV"]

data = [] # creates an empty list to which data can be appended in the main loop
# necessary in order not to throw an error in the newdata/existing data comparison
n = 0 # counter for each iteration of the main loop to enable cleaning

# display the "Powered by National Rail Enquiries" logo on boot
image ("/home/pi/voyageDisplay/nre.png")
time.sleep(1)

print ("Initialised") # print for debugging

## MAIN LOOP
while True:

    n = n + 1 # count iterations
    print (str(n) + " iterations") # print for debugging

    # Run a cleaning cycle (to prevent burn-in on the Inky) after every 60 iterations (~ 30 minutes)
    if n == 60:
        n = 0
        clean ("phat", "red", 3)
        image("/home/pi/voyageDisplay/nre.png")
        data = []
        continue

    else:

        print ("Fetching New Data") # print for debugging
        try: # fetches new data from Huxley and stores it as 'newdata'
            time.sleep(2)
            newdata = get (origin, destination, huxley)
            print ("Fetch Successful") # print for debugging
        except: # Displays meaningful error message and prompts to reboot if there is a problem fetching the data
            print ("Fetch Error") # print for debugging
            message = "Fetch Error, Restart"
            w_notrains, h_notrains = font_large.getsize(message)
            x_notrains = (inky_display.WIDTH / 2) - (w_notrains / 4)
            y_notrains = (inky_display.HEIGHT / 2) - (h_notrains / 4)
            draw.text((x_notrains, y_notrains), message, inky_display.BLACK, font_large)
            inky_display.set_image(img)
            inky_display.show()
            sys.exit()


        if newdata == data: # compares newdata with data (old data)
            data = newdata # if no change, do nothing but sleep for 30 secs
            print ("No Change in Data") # print for debugging
            time.sleep(30)
            continue

        else:
            try:
                data = newdata # if change in data, update 'data' and display on Phat, then sleep for 30 seconds
                print ("Displaying Updated Data") # print for debugging
                img = Image.new("P", (inky_display.WIDTH, inky_display.HEIGHT))
                draw = ImageDraw.Draw(img)
                display (data)
                time.sleep(30)
            except: # display a meaningful error if there is a problem displaying the data & prompt to reboot
                print("Display Error") # print for debugging
                message = "Display Error, Restart"
                w_notrains, h_notrains = font_large.getsize(message)
                x_notrains = (inky_display.WIDTH / 2) - (w_notrains / 4)
                y_notrains = (inky_display.HEIGHT / 2) - (h_notrains / 4)
                draw.text((x_notrains, y_notrains), message, inky_display.BLACK, font_large)
                inky_display.set_image(img)
                inky_display.show()
                sys.exit()
