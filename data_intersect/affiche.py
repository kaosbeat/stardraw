#!/usr/bin/python3

import lib.starLC20 as p
import lib.staremulator as s
import random
from perlin_noise import PerlinNoise
import datetime
import lib.starDraw as sd
import lib.tweetprint as tweet
# import font_anomaly as fa
import lib.recaptcha as rc
import lib.font_anomaly as fa
import lib.font_anomaly_phone as fap
import db

from pyfiglet import Figlet


printit = False
tweetit = True
tweetit = False
svg = True
sign = True
title = "starLC20"


data = db.getAllFromHometown("Antwerp")
# print(data)


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





def intersect_text(text):
    # text should be a string of characters, one string as a whole
    print("intersecting")
    # global columns
    columns = 80
    height = 69
    cutpos = int(columns/2)
    s.svgfile = 'intersect'+str(cutpos)+'.svg'
    s.openfile(s.svgfile)
    # bufferlist=[]
    charlist1 = ["O","|","-","+","/"]
    charlist2 = ['!','#','%','^', '&', '}', "o", ">", "~"]
    maxx = 0
    maxy = 0
    ra = random.randint(3,8)
    b1 = sd.parallelogram(random.randint(6,19), random.randint(40,60),ra, charlist1[random.randint(0,len(charlist1)-1)])
    # print(b1)
    pb1 = sd.padMidMax(b1,columns,height)
    # print(pb1)
    b2w = random.randint(6,35)
    b2 = sd.parallelogram_charlist(random.randint(30,50),b2w, random.randint(13,28), text)
    pb2 = sd.padMidMax(b2,columns,height)

    b2start = int((columns - b2w)/2 )
    cutpos = random.randint(b2start+1,b2start+b2w-1)
    cutpos = int(columns/2)
    mb = sd.mergeBuffers(pb1, pb2, cutpos )
    # # print(mb)

    # print(sd.dimensions(b1))
    # print(b1)
    p.printBuffer(mb, 0, 0, height)
    s.printBuffer(mb, 0, 0, height)
    signature = signstring("intersect study")
    p.printXY(signature, 80-len(signature), int(height))
    s.printXY(signature, 80-len(signature), int(height))
    s.closefile()
    p.nextTop()
    if tweetit:
        tweet.convertSVGtoTweet(s.svgfile, "intersections")
    print(pb2)
    

#prepare data

# random.shuffle(data)
names = ""
for name in data:
    # print(name)
    names = names + " " + name[0]
names = list(names)
# print (names)
names.reverse()
# print(names)


# intersect_text(names)




def namefunction():
    # return iter(fap.getNextDiscordname()) 
    # a = iter(db.getRandomname(names))
    
    return iter(db.getRandomname(data))

def printFaarBanner():
    rev = False
    mirror = False
    rs = "DATA"
    words = rs
    # words = "tE"
    print(rs)
    s.svgfile = 'faarbanner.svg'
    # # words = "No, I have no Facebook!"
    # wordlist=["your data", "data communism", "data capitalism", "algorithmic happiness"]
    # words = "data communism"
    if rev:
        words = words[::-1]
    print(words)
    pages = len(words)
    s.openmultipagefile(s.svgfile,pages)
    density = 7
    p.setNewDensityAndGotoTop(density, p.pageheight, p.linefeed)
    s.setNewDensityAndGotoTop(density, p.pageheight, p.linefeed)
    height = int(p.pageheight*12/p.linefeed)
    totalheight = height*pages
    x = 5
    y = 7
    size = int(p.columns/(x+1))
    margin = int((p.columns - (x*size)) / x)
    for i,l in enumerate(words):
        buffer = fap.letter2page4versum(l, (x,y), margin, True, namefunction)
        if rev:
            revbuffer = ""
            for line in reversed(buffer.splitlines()):
                if mirror:
                    line = line[::-1]
                revbuffer = revbuffer + line + "\n"
            buffer = revbuffer
        p.printBuffer(buffer,0,(height*i)+15,totalheight)
        s.printBuffer(buffer,0,(height*i)+15,totalheight)

    signature = signstring("data anomaly squares - " + rs)
    p.printXY(signature, 80-len(signature), totalheight-int(2*12/p.linefeed)+ 10)
    s.printXY(signature, 80-len(signature), totalheight-int(2*12/p.linefeed)+ 10)
    s.closefile()


printFaarBanner()
print(db.getRandomname(data))
# namefunction()