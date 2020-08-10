# Function to display DELAY data on the InkyPHAT

# Boiler plate setup code for the display

from inky import InkyPHAT

inky_display = InkyPHAT("red")
inky_display.set_border(inky_display.WHITE)
inky_display.h_flip = True
inky_display.v_flip = True

from PIL import Image, ImageFont, ImageDraw
img = Image.new("P", (inky_display.WIDTH, inky_display.HEIGHT))
draw = ImageDraw.Draw(img)

from font_fredoka_one import FredokaOne
font = ImageFont.truetype(FredokaOne, 13)
font_header = ImageFont.truetype(FredokaOne, 13)
font_large = ImageFont.truetype(FredokaOne, 18)

######### #########

def display (trains):
    inky_display.set_border(inky_display.WHITE)
    img = Image.new("P", (inky_display.WIDTH, inky_display.HEIGHT))
    draw = ImageDraw.Draw(img)

    i = 0
    row = i
    count = 0

    header = "Pem & Wigan to Manchester Stns" # This needs to be created dynamically in future releases

    w, h = font_header.getsize(header) # works out width of header so it can be centred
    draw.text((((inky_display.WIDTH / 2) - (w / 2)), 0), header, inky_display.BLACK, font_header) # displays header

    for t in trains: # iterates through each train service with data and displays information in two columns
        name = t["origin"] + "-" + t["destination"]
        x_left = 0
        x_right = inky_display.WIDTH / 2
        if i % 2 == 0:
            if t["delay"] == 1:
                row = row + 1
                y = row*16
                draw.text((x_left, y), name, inky_display.BLACK, font)
                i = i+1
                count = count + 1
            elif t["delay"] == 0:
                row = row + 1
                y = row*16
                draw.text((x_left, y), name + " (" + str(t["delayMinutes"]) + ")", inky_display.RED, font)
                i = i+1
                count = count + 1
            else:
                pass
        else:
            if t["delay"] == 1:
                y = row*16
                draw.text((x_right, y), name, inky_display.BLACK, font)
                i = i+1
                count = count + 1
            elif t["delay"] == 0:
                y = row*16
                draw.text((x_right, y), name + " (" + str(t["delayMinutes"]) + ")", inky_display.RED, font)
                i = i+1
                count = count + 1
            else:
                pass

    # If there is no data (ie. the count of iterations is 0) then there must be no trains due in the next two hours.
    if count == 0:
        message_notrains = "No services in the\n  next two hours."
        w_notrains, h_notrains = font_large.getsize(message_notrains)
        x_notrains = (inky_display.WIDTH / 2) - (w_notrains / 4)
        y_notrains = (inky_display.HEIGHT / 2) - (h_notrains / 4)
        draw.text((x_notrains, y_notrains), message_notrains, inky_display.RED, font_large)

    # update display & wait
    inky_display.set_image(img)
    inky_display.show()