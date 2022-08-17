#!/usr/bin/python3

# from numpy import convolve  
import imp
from itertools import count
import lib.starLC20 as p
import lib.staremulator as s
import random
from perlin_noise import PerlinNoise
import datetime
import lib.starDraw as sd
import lib.tweetprint as tweet
import lib.font_anomaly as fa
import lib.recaptcha as rc
from pyfiglet import Figlet, figlet_format, print_figlet
import db
import time
import lib.asciistage as ast






printit = False
# tweetit = True
tweetit = False
screenit = False
screenit = True
svg = True
sign = True
title = "starLC20"

def sign(title, y):
    s.setLineSpace(12)
    p.setLineSpace(12)
    string = '{0:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())
    string = "kaotec []<> " + title + " " + string
    s.printXY(string, s.columns - len(string), y) 


def signstring(title):
    string = '{0:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())
    string = "kaotec []<> " + title + " " + string
    return string



#######################
### shape fill page ###
#######################
def shapes():
    s.openfile('shape.svg')
    if printit:
        p.setOnLine()
        p.reset()
        # p.beep()
        p.noMargins()
        # p.beep()

    columns = 80
    height = 64

    c1 = random.randint(0, int(columns / 2)) +1
    c2 = random.randint(0, int((columns - c1)/2))
    c3 = columns - c1 - c2
    l1 = "!"
    l2 = "o"
    l3 = "#"
    i = 0
    # for i in range(height):
    C1 = random.randint(0,c1)

    direction = 1
    while i < height:
        for k in range(C1):
            line = ""
            for x in range(c1):
                line = line + l1
            # print(len(line))
            for x in range(c2):
                line = line + l2
            # print(len(line))
            for x in range(c3):
                line = line + l3
            line = line[0:80]
            print(line)

            if printit:
                p.printXY(line, 0, i)
            if svg:
                s.printXY(line, 0, i+1)
            c1 = c1 - direction
            # c3 = c3 + direction
            i = i +1

        direction = direction * -1
        C1 = random.randint(0, random.randint(0, int(columns / 2)) +1)
        c1 = random.randint(0, int(columns / 2)) +1
        c2 = random.randint(0, int((columns - c1)/2))
        c3 = columns - c1 - c2


    c1 = random.randint(0, int(columns / 2)) +1
    c2 = random.randint(0, int((columns - c1)/2))
    c3 = columns - c1 - c2
    i = 0
    # for i in range(height):
    C1 = random.randint(0,c1)
    count = 0
    direction = 1
    while i < height:
        for k in range(C1):
            line = ""
            for x in range(c1):
                line = line + " "
            # print(len(line))
            for x in range(c2):
                line = line + names[count]
                count = count + 1
            # print(len(line))
            for x in range(c3):
                line = line + " "
            line = line[0:80]
            print(line)

            if printit:
                p.printXY(line, 0, i)
            if svg:
                s.printXY(line, 0, i+1)
            c1 = c1 - direction
            # c3 = c3 + direction
            i = i +1

        direction = direction * -1
        C1 = random.randint(0, random.randint(0, int(columns / 2)) +1)
        c1 = random.randint(0, int(columns / 2)) +1
        c2 = random.randint(0, int((columns - c1)/2))
        c3 = columns - c1 - c2

    s.closefile()
    tweet.convertSVGtoTweet(s.svgfile, "shapefill")


########################################
#### relation_shapes() #################
########################################

def rshapes(names1, names2, title):
    s.openfile('rshape.svg')
    if printit:
        p.setOnLine()
        p.reset()
        # p.beep()
        p.noMargins()
        # p.beep()

    columns = 80
    height = 64

    c1 = random.randint(0, int(columns / 2)) +1
    c2 = random.randint(0, int((columns - c1)/2))
    c3 = columns - c1 - c2
    l1 = "!"
    l2 = "o"
    l3 = "#"
    i = 0
    # for i in range(height):
    C1 = random.randint(0,c1)
    count1 = 0
    direction = 1
    while i < height:
        for k in range(C1):
            line = ""
            for x in range(c1):
                line = line + " "
            # print(len(line))
            for x in range(c2):
                try: 
                    names1[count1]
                except IndexError:
                    count1 = 0
                line = line + names1[count1]
                count1 = count1 + 1
            # print(len(line))
            for x in range(c3):
                line = line + " "
            line = line[0:80]
            i = i +1
            if (i < height):
                if printit:
                    p.printXY(line, 0, i)
                if svg:
                    s.printXY(line, 0, i+1)
            c1 = c1 - direction
            # c3 = c3 + direction

        direction = direction * -1
        C1 = random.randint(0, random.randint(0, int(columns / 2)) +1)
        c1 = random.randint(0, int(columns / 2)) +1
        c2 = random.randint(0, int((columns - c1)/2))
        c3 = columns - c1 - c2

    s.currentTop()
    p.currentTop()
    c1 = random.randint(0, int(columns / 2)) +1
    c2 = random.randint(0, int((columns - c1)/2))
    c3 = columns - c1 - c2
    i = 0
    # for i in range(height):
    C1 = random.randint(0,c1)
    count2 = 0
    direction = -1
    while i < height:
        for k in range(C1):
            line = ""
            for x in range(c1):
                line = line + " "
            # print(len(line))
            for x in range(c2):
                try: 
                    names2[count2]
                except IndexError:
                    count2 = 0

                line = line + names2[count2]
                count2 = count2 + 1
            # print(len(line))
            for x in range(c3):
                line = line + " "
            line = line[0:80]
            i = i +1
            if (i < height):

                if printit:
                    p.printXY(line, 0, i)
                if svg:
                    s.printXY(line, 0, i+1)
            c1 = c1 - direction
            # c3 = c3 + direction
            # i = i +1

        direction = direction * -1
        C1 = random.randint(0, random.randint(0, int(columns / 2)) +1)
        c1 = random.randint(0, int(columns / 2)) +1
        c2 = random.randint(0, int((columns - c1)/2))
        c3 = columns - c1 - c2
    signature = signstring(title)
    sigX = 80-len(signature)
    p.printXY(signature, sigX, int(height)+2)
    s.printXY(signature, sigX, int(height)+2)
    s.closefile()
    if tweetit:
        tweet.convertSVGtoTweet(s.svgfile, "shapefill")


# shapes()
# data = db.getAllFromHometown("Antwerp")
# data1 = db.GetMostFRequentNameInRelationstatusInCity("\"In a relationship\"", "Antwerp")
# data2 = db.GetMostFRequentNameInRelationstatusInCity("\"It\'s complicated\"", "Antwerp")

data1 = db.GetMostFRequentNameInRelationstatus("\"In a relationship\"")
data2 = db.GetMostFRequentNameInRelationstatus("\"It\'s complicated\"")

# random.shuffle(data)

ast.initstage()
# ast.printonstage("hello at 20,20", 20, 20)
# ast.printonstage("hello at 30,20", 30, 20)
# ast.printonstage("hello at 20,40", 20, 40)
# ast.printonstage("hello at 20,10", 20, 10)
# for i in range (ast.columns-3):
#     for j in range(ast.lines-3):
#         ast.printonstage("!",i,j)


# ast.printFiglet("verymuchtoolongstringtooprint", "big", 1, 50)




# time.sleep(50)
x=0
while True:
    x = x+1
    text = "svslsfv;sbalbffskb'sfdjb[arint"
    font = "big"
    w,h = ast.figProps(text, font)
    w = w+2
    h = h+2
    ast.printFiglet(text, font, -w+x%(ast.columns+w), 15)
    time.sleep(0.02)


names1 = ""
for name in data1:
    names1 = names1 + " " + name[0]
    x = random.randint(2,ast.columns-len(name[0]))
    y = random.randint(1, ast.lines-2)
    # ast.printonstage(str(x)+", "+str(y), 0 , ast.lines-1)
    # print(name[0])
    ast.printFiglet(name[0],"big")
    # ast.printonstage(name[0], x, y)
    time.sleep(0.1)
    ast.printFiglet("               ", ast.lines-1)
names1 = list(names1)
names2 = ""
for name in data2:
    names2 = names2 + " " + name[0]
names2 = list(names2)




rshapes(names1, names2, "it's a complicated relationship")






