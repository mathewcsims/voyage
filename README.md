# Voyage
A better way of displaying UK train information, at home, using a Raspberry Pi.

## The Problem
I commute by train. There are three stations near where I live that I can start from, and four in the city I commute to, where I can end my journey. National Rail Eqnquiries ([nationalrail.co.uk](http://www.nationalrail.co.uk)) doesn't offer any way for me to view all of these possible journeys at once, making deciding which station to go to first thing in the morning a massive pain. Especially when I'm still half asleep!

## The Solution
A low-cost, at-home display - using a [Raspberry Pi Zero](https://shop.pimoroni.com/products/raspberry-pi-zero-wh-with-pre-soldered-header#show-accessories) WH (because I couldn't be bothered soldering) and an [InkyPHAT](https://shop.pimoroni.com/products/inky-phat?variant=12549254217811) display.

## Using the code
You're welcome to make use of this code any way you like. I'd appreciate an email (ms7963@ou.ac.uk) if you find it useful, or just to let me know what you do with it. At the moment, it's cumbersome, has little error handling, and is hard coded to my own commute. But, if you know a little Python, I'm sure you'll be able to work it out.

# Dependencies
This project makes use of:
- Pimoroni's [Inky](https://github.com/pimoroni/inky) code (MIT license)
- [Huxley2](https://github.com/jpsingleton/Huxley2) by jpsingleton (you'll need to implement this yourself if you want my code to work - there are full instructions accessible through the repo I've linked to.)
