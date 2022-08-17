import os
import sys
import time
import lib.starDraw as sd
from pyfiglet import Figlet
import random

columns, lines = os.get_terminal_size() 
line = 0 # 0 is bottom line
col = 0 # 0 is left

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
    global line,col
    gotoline(y)
    print(f"\033[{x}G" + text, end='',  flush=False)
    # print(f"\b", flush=True)
    col = 0


def printFiglet(text, font):
    # figtext = ''''''
    # print(text)
    # figtext = pyfiglet.print_figlet(text,font)
    f = Figlet(font='big')
    figtext = f.renderText(text)
    if len(figtext) > 0:
        # print(")))))")
        figtext = str(sd.padBuffer(figtext,1, 1, 1, 1))
        # print(figtext)
        width, height = sd.dimensions(figtext)
        # print(width,height)
        x = random.randint(2,columns-width-2)
        y = random.randint(1,lines-height-2)
        # for line in figtext:
        for i,l in enumerate(figtext.splitlines()):
        #     print(line)
            printonstage(l, x, height+y)
            y -= 1



# initstage()

# s = 0
# while s < 10:
#     gotoline(s)
#     s += 1
#     time.sleep(0.1)


# while s > 5:
#     gotoline(s)
#     s -= 1
#     time.sleep(0.3)



# txt = "columns:" +  str(columns)
# printonstage(txt, 20, 18)

