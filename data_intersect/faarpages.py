########################
####  imports ##########
########################
# own libraries
import lib.starLC20 as p
import lib.staremulator as s
import lib.stardisplay as d
import lib.starDraw as sd
import lib.tweetprint as tweet
import lib.font_anomaly as fa
import lib.recaptcha as rc
import lib.timers as tim
import lib.asciistage as ast
import faarasciiart as aa
import lib.promptqueries as pq


### other imports
from itertools import cycle
import random

def invertedCat(word, scale, spacing, xmov):
    """
    inverted cat writes cat by leaving out cat and filling 
    the rest of the page with charachters and words associated with the word
    """    
    global state
    global height, columns 
    columns = 80
    height = 69
    state = "invertedCat"
    
    s.svgfile = 'invertedcat.svg'
    s.openfile(s.svgfile)
    s.setLineSpace(spacing)
    # s.setLineSpace(7)
    p.setLineSpace(spacing)
    words = cycle(pq.wordContext(word))
    # scale = 2
    
    times = 1
    t = 0
    while t < times:
        ycursor = 0
        sc = 0
        while sc < scale:
            line = "x"*columns
            letterline = ""
            for c in line:
                if c == "x":
                    letterline += next(words)
                else:
                    letterline += " "
            line = letterline 
            s.printXY(line,0,ycursor)
            p.printXY(line,0,ycursor)
            ycursor += 1 
            sc+=1
        for letter in word:
            xoffset = random.randint(0,columns - 5*scale) 
            for l in fa.font5x7[letter]:
                sc = 0
                while sc < scale:
                    bl = ""
                    for c in l:
                        if c == 1:
                            bl = bl + " "*scale
                        else:
                            bl = bl + "x"*scale 
                    # line = "x"*int(columns/2-len(bl)/2) + bl + "x"*int(columns/2-len(bl)/2)
                    line = "x"*xoffset + bl + "x"*int(columns-len(bl)-xoffset)
                    letterline = ""
                    for c in line:
                        if c == "x":
                            letterline += next(words)
                        else:
                            letterline += " "
                    line = letterline 
                    s.printXY(line,0,ycursor)
                    p.printXY(line,0,ycursor)
                    ycursor += 1 
                    sc+=1
            sc = 0
            while sc < scale:
                line = "x"*columns
                letterline = ""
                for c in line:
                    if c == "x":
                        letterline += next(words)
                    else:
                        letterline += " "
                line = letterline 
                s.printXY(line,0,ycursor)
                p.printXY(line,0,ycursor)
                ycursor += 1 
                sc+=1
        t += 1 
    s.closefile() 
    state = "done"

invertedCat("cyber", 3, 7, 0 )

# print(pq.wordContext("cat"))