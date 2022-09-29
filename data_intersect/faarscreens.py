########################
####  imports ##########
########################
# own libraries
# import lib.starLC20 as p
# import lib.staremulator as s
# import lib.stardisplay as d
from tracemalloc import start
import lib.starDraw as sd
import lib.tweetprint as tweet
import lib.font_anomaly as fa
import lib.recaptcha as rc
import lib.timers as tim
import lib.asciistage as ast
import faarasciiart as aa
import lib.promptqueries as pq
from lib.asciitools import strip2ascii

### other imports
from itertools import cycle
import random
import time
# tweetit = True


def randomMask(word, chance):
    mask = ""
    for l in word:
        if random.random() > chance:
            mask += "x"
        else:
            mask += " "
    return mask

def cyclemask(word, cyclepoint, width):
    """
    cyclemask is float between 0,1
    width is size of wordpart, float beween 0,1
    """
    masklength = int(len(word)*width)
    if masklength == 0: masklength = 1
    startpoint = int(len(word)*cyclepoint)-int(masklength/2)
    endpoint = startpoint+masklength-1
    # print (startpoint, endpoint)
    if startpoint < 0:
        startpoint = 0
    if startpoint > len(word)-1:
        startpoint = len(word)-1
    if endpoint >= len(word):
        endpoint = len(word)
    mask=""
    # print (startpoint, endpoint)
    for i in range(len(word)):
        if i < startpoint:
            mask+=" "
        elif i >= startpoint and i <= endpoint:
            mask+="x"
        else:
            mask+=" "
    return mask




def invertedHorizontalCat(word, mask, masktype , columns, height):
    """
    inverted cat writes cat by leaving out cat and filling 
    the rest of the page with charachters and words associated with the word
    scale scales the font
    returns multilinebuffer
    """    

    buffer = """"""
    words = cycle(pq.wordContext(word))
    partssize = int(columns/len(word))
    scale = int((partssize - 2)/5)
    if scale > 5 : scale = 5
    if scale < 1 : scale = 1
    blankrows = int((height - 7*scale)/ 2) 
    buffer += ("x"*columns+"\n")*blankrows
    c_row = 0
    while c_row < 7:
        sc = 0
        while sc < scale:
            bl = "x"*int(scale/2)
            # bl += "x"*int(partssize/2)
            for i,c in enumerate(word):
                if mask[i] == "x":
                    xline = fa.font5x7[c][c_row]
                else:
                    if masktype == "fill":
                        xline = [1,1,1,1,1]
                    elif masktype == "noise":
                        xline = [random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1)]
                    elif masktype == "invert":
                        xline = [0,0,0,0,0]
                for lc in xline:
                    if lc == 1:
                        bl = bl + " "*scale
                    else:
                        bl = bl + "x"*scale
                
                bl = bl + "x"*int(scale/2)
            # bl += "x"*int(partssize/2)
            pad = int((columns-len(bl))/2)
            bl = "x"*pad + bl + "x"*pad
            if len(bl) < columns:
                bl += "x"
            bl += "\n"
            buffer+=bl
            sc+=1
        
        c_row+=1
    buffer += ("x"*columns+"\n")*blankrows
    letterbuffer = """"""
    for line in buffer.splitlines():
        letterline = ""
        for c in line:
            if c == "x":
                letterline += strip2ascii(next(words))
            else:
                letterline += " "
        letterbuffer +=letterline +"\n"
        
    return letterbuffer
testword = "cyborg"

while(True):
    for i in range(len(testword)):
        bf = invertedHorizontalCat (testword,cyclemask(testword, 1/len(testword)*i, 0.5) , "invert", 120, 40)
        ast.printMultilineonstage(bf,0,40)
        time.sleep(0.3)
#     # bf = invertedHorizontalCat ("cyborg", randomMask("cyborg", 0.1), "invert", 120, 40)
#     # ast.printMultilineonstage(bf,0,40)
#     # time.sleep(0.5*random.random())