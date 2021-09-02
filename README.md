# stardraw
python Driver for starLC20 matrix printer with SVG emulation mode

# License 
everything in the lib folder is MIT licensed, would love to see other people use it
everything in the examples and output folder is my IP if you want to use it contact me

## the parts
# starLC20.py
the actual driver
talks to the starLC20 in IBM mode (jumper 1-1 off)
I couldn't get my RPi to talk to it in Epson mode
I disabled cups because it was interfering, and I used a:
Bus 001 Device 004: ID 067b:2305 Prolific Technology, Inc. PL2305 Parallel Port
USB to parralel port adapter to cennect it to my RPi3


# staremulator.py
emulates as good as possible the driver, rendering the same results in SVG as you can see on paper...
depends on SVGwrite > pip3 install svgwrite (or similar)

# stardraw 
library of convenient ascii elements ready to be printed


# activate
. bin/activate stardraw

