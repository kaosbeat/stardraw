import os
import sys
import time
import lib.starDraw as sd
from pyfiglet import Figlet
import random

columns, lines = os.get_terminal_size() 
line = 0 # 0 is bottom line
col = 0 # 0 is left
global screenit
screenit = True


def initstage():
    global columns, lines
    print("creating stage")
    print("#"*columns)
    # sleeptime = 0.1
    for i in range(lines-2):
        print("#" + " "*(columns-2) + "#")
        # time.sleep(sleeptime*0.5)
    print("#"*columns, end='',flush=False)


def gotoline(y):
    global screenit
    if screenit:
        ## value to print to go back a line: \033[F
        global line
        if (y > line):
            for i in range(y-line):
                print(f"\033[F", end='\r', flush=True)
        elif (y < line):
            for i in range(line-y):
                print(f"", flush=True)
        else:
            print('\b',end='',flush=True)
        line = y



def printonstage(text, x, y):
    global screenit
    global line,col
    if screenit:
        gotoline(y)
        print(f"\033[{x}G" + text, end='',  flush=False)
        # print(f"\b", flush=True)
        col = 0


def figProps(text, font):
    """returns the string width and height of rendered figlet"""
    global columns
    global screenit
    if screenit:
        f = Figlet(font=font, width=2000)
        figtext = f.renderText(text)
        width, height = sd.dimensions(figtext)
        return width, height

def printFiglet(text, font, x=1, y=1, trim=True):
    """print a figlet from 'text' in 'font' at x, y 
       output is trimmed by default if it's wider/heigher 
       than available terminal space.
       width of the figlet should be columns-2
    """

    global columns
    global screenit
    if screenit:
        f = Figlet(font=font, width=2000)
        figtext = f.renderText(text)
        if len(figtext) > 0:
            figtext = str(sd.padBuffer(figtext,1, 1, 1, 1))
            width, height = sd.dimensions(figtext)
            if x <= -width:
                figtext = ""
            elif 0 <= x + width <= columns:
                figtext = sd.trimbuffer(figtext, width+x, "l")
            elif width >= x + width >= columns:
                figtext = sd.trimbuffer(figtext, width+x, "l")
                figtext = sd.trimbuffer(figtext, columns, "r")
            elif 0 < x < columns:
                figtext = sd.trimbuffer(figtext, columns-x, "r")


            if y >= lines:
                figtext = sd.trimbuffer(figtext, height-y+lines, "t")
            if height > y: #cut of the bottom
                figtext = sd.trimbuffer(figtext, y, "b")
    
            for i,l in enumerate(figtext.splitlines()):
                printonstage(l, x, y)
                y -= 1

def printFigletAtRandomLoc(text, font):
    global lines, columns
    global screenit
    if screenit:
        f = Figlet(font=font)
        figtext = f.renderText(text)
        if len(figtext) > 0:
            figtext = str(sd.padBuffer(figtext,1, 1, 1, 1))
            width, height = sd.dimensions(figtext)
            x = random.randint(2,columns-width-2)
            y = random.randint(1,lines-height-2)
            for i,l in enumerate(figtext.splitlines()):
                printonstage(l, x, height+y)
                y -= 1


def scrollFiglet(text, font, y, speed, loop):
    """scroll text in font at height y at speed, loop it loop times """

    global screenit
    global columns, lines
    if screenit:
        x=0
        looping = True
        # 
        # for i in range(loop):
        while looping:
            x = x+1
            w,h = figProps(text, font)
            w = w+2
            h = h+2
            printFiglet(text, font, -w+x%(columns+w), y)
            if (-w+x%(columns+w) == 0):
                loop -= 1
            if loop <= 0:
                looping = False 
            time.sleep(speed)



def doNoise(x, X, y, Y, speed):
    global screenit
    if screenit:
        while True:
            chars = ["@", "!", "%"]
            i = random.randint(x,X)
            j = random.randint(y,Y)
            c = random.choice(chars)
            printonstage(c,i,j)
            time.sleep(speed)