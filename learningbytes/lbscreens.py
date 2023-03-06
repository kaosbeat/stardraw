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
import lbfasciiart as aa
import lib.promptqueriesfake as pq
from lib.asciitools import strip2ascii


### other imports

import random
import time
from perlin_noise import PerlinNoise
# tweetit = True


def bootseq(framewait = 5):
    ast.initstage("scroll")
    ast.printFiglet("LEARNING ", "big", 10, ast.lines-10)
    time.sleep(framewait)
    ast.printFiglet("BYTES", "big", 20, ast.lines-21)
    ast.printFiglet("L#@7@NIG", "big", 10, ast.lines-10)
    time.sleep(framewait)
    # ast.initstage("clear")
    ast.printFiglet("LEARNING ", "big", 10, ast.lines-10)
    ast.printFiglet("8Y1%$", "big", 10, ast.lines-21)
    time.sleep(framewait)
    ast.printFiglet("BYTES", "big", 10, ast.lines-21)
    time.sleep(framewait)
    w,h,text1 = ast.figProps("LEARNING", "big")
    w,h,text2 = ast.figProps("BYTES", "big")
    for i in range(10):
        time.sleep(framewait)
        mergestep = ast.mergeFiglets (text1,text2, 0,0,8,21-i)
        ast.printMultilineonstage(mergestep, 10, ast.lines-10)
    ast.scrollFiglet("FESTIVAL", "big", ast.lines-31, 0.01, 2)
    time.sleep(framewait)
    # ast.initstage()
   

def keynote1(framewait = 0.5):
    ast.initstage("scroll")
    ast.printFiglet("KEYNOTE ", "starwars", 10, ast.lines-10)
    time.sleep(2)
    ast.printFiglet("Annelies Raes", "big", 20, ast.lines-21)
    time.sleep(2)
    ast.printMultilineonstage(aa.raes2, 93, ast.lines-1, 0.1)
    time.sleep(2)

    
def coffee(framewait, noisestep):
    # buffersmoke = sd.padMidMax(aa.coffeesmoke, ast.columns, ast.lines)
    noisebuffer = noiser(aa.coffeesmoke, noisestep, 1112, "r", 4)
    buffercupsmoke = sd.padMidMax(noisebuffer, ast.columns, ast.lines)
    buffercup = sd.padMidMax(aa.coffee, ast.columns, ast.lines)
    total = sd.mergeBuffers(buffercup,buffercupsmoke,0)
    ast.printMultilineonstage(total,1,ast.lines)
    # ast.printMultilineonstage(mergedbuffer,1,ast.lines)



   





################
#### signal ####
################
def perspsquaressignal(times):
    columns = ast.columns
    height = ast.lines
    chars = ['!','#','%','^', '&', '}', "o", ">", "~"]

    for k in range(times):
        # midi_playsample(random.randint(1,8))
        size =  random.randint(8,18)
        sx = random.randint(1,columns-size-3)
        sy =  random.randint(1,height-size-3)
        h = random.randint(size+3,ast.lines-3)
        # size = 10
        dx = random.randint(0,4) - 2
        dy = random.randint(0,4) - 2
        ds = random.randint(0,4) - 2
        prevbuffer=""""""
        for i in range(size):
            x1 = sx + i*dx
            x2 = sx + i + i*dx
            y1 = sy + i*dy
            y2 = sy + i + i*dy
            charh = chars[random.randint(0,len(chars)-1)]
            charv = chars[random.randint(0,len(chars)-1)]
            buffer = sd.square2(x1,y1,x2,y2,charh,charv)
            prevbuffer = ast.mergeFiglets (prevbuffer,buffer,0,0,0,0)
            ast.printMultilineonstage(prevbuffer, 0, h)
            time.sleep(0.01)
        # midi_playsample(9)

def cuber():
    columns = ast.columns
    height = ast.lines
    charset1 = ["+","\\", "/", "|", ">", "<", ":" ]
    charset2 = ["Y","#", "%", "&", "^", "!", "}" ]
    charset3 = [")","`", "'", ".", "@", "*", "{" ]
    w,h,d = random.randint(3,24), random.randint(3,24), random.randint(3,24)
    buffer = sd.cube(w,h,d,charset1[random.randint(0,len(charset1)-1)],charset2[random.randint(0,len(charset2)-1)],charset3[random.randint(0,len(charset3)-1)])
    xdim,ydim = sd.dimensions(buffer)
    # if xdim <= 0: xdim = 1
    # if ydim <= 0: ydim = 1
    # dims = "xdim= ", xdim, " ydim = ", ydim
    # ast.printonstage(str(dims), 0,0)
    if (ydim > height):
        buff = ydim
        ydim = height
        height = buff
    if (columns-xdim < 0):
        xval = xdim - columns
    else:
        xval = columns - xdim

    x,y = random.randint(0,xval),random.randint(0+ydim,height)
    ast.printMultilineonstage(buffer, x, y)


def squares(amount):
    columns = ast.columns
    height = ast.lines
    chars = ['!','#','%','^', '&', '}', "o", ">", "~"]
    for k in range(amount):
        x1 = random.randint(1,columns)
        x2 = random.randint(1,columns)
        y1 = random.randint(1,height)
        y2 = random.randint(1,height)
        charh = chars[random.randint(0,len(chars)-1)]
        charv = chars[random.randint(0,len(chars)-1)]
        bufferlist = sd.square(x1,y1,x2,y2,charh,charv)
        for buffer in bufferlist:
            for i,l in enumerate(buffer.splitlines()):
                count = 0
                for j in l:
                    if j == " ":
                        count += 1
                    else:
                        count += 1
                        ast.printonstage(j,count,i)



def lines(amount, words = None):
    columns = ast.columns
    height = ast.lines
    chars = ['!','#','%','^', '&', '}', "o", ">", "~"]
    for i in range(amount):
        x1 = random.randint(1,columns)
        x2 = random.randint(1,columns)
        y1 = random.randint(1,height)
        y2 = random.randint(1,height)
        char = chars[random.randint(0,len(chars)-1)]
        buffer = sd.line(x1,y1,x2,y2,char)
        for i,l in enumerate(buffer.splitlines()):
            count = 0
            for j in l:
                if j == " ":
                    count += 1
            if words != None:
                 char = next(words)
            ast.printonstage(char,count,i)
 
def circle(circleradius = "", x ="",y ="", noisestep = "", seed = ""):
    columns = ast.columns
    height = ast.lines
    if seed == "":
        seed = random.randint(0,5000)
    # def noisecircle(circleradius="", x="", y="", density="", noisechar="", circlechar="", octaves="", seed=""):
    chars = ['!','#','%', "@", '&', '/', ">"]
    nchars = [".", "<", "'", "~", "^", "\\" ]
    # if circlechar ==  "":
    random.seed(seed)
    circlechar = chars[random.randint(0,len(chars)-1)]
    # if noisechar == "":
    noisechar = nchars[random.randint(0,len(nchars)-1)]
    # noiseoctaves = random.randint(1,10)
    if circleradius == "":
        # circleradius = random.randint(4,int(min(columns/6,height/6)))
        if columns > height:
            circleradius = random.randint(4,int(min(columns,height)/2)-1)
        else:
            circleradius = random.randint(4,12)

        # y = ast.lines+1
    # if density == "":
        # density = random.randint(6,16)
    # if octaves == "":
    octaves = random.randint(1,10)

    buffer = sd.circle(circleradius,12,12,circlechar)
    xnoise, ynoise = sd.dimensions(buffer)
    noise = PerlinNoise(octaves=octaves, seed=seed)
    if noisestep == "" : noisestep = 0.0
    noisebuffer = [[noise([i/xnoise + noisestep, j/ynoise + noisestep]) for j in range(xnoise)] for i in range(ynoise)]
    # noisechar = nchars[random.randint(0,len(nchars)-1)]
    mergedbuffer = ""
    for i,l in enumerate(buffer.splitlines()):
        line = ""
        for j,c in enumerate(l):
            if c != " ":
                if noisebuffer[i][j] > 0:
                    c = noisechar
            line = line + c
        mergedbuffer = mergedbuffer + line + "\n"
    if x =="":
        newx = columns-xnoise
        if newx < 0: newx = 0
        x = random.randint(0,newx)
    if x == "mid":
        x = int(columns/2 - xnoise/2)
    if y == "":
        y = random.randint(ynoise,height)
    if y == "mid":
        y = int(height/2 + ynoise/2)

    # ast.clearstage()
    # ast.quickinit()
    # ast.quickclear()
    ast.printMultilineonstage(mergedbuffer,x,y)


def intersect(size, framewait):
    columns = ast.columns
    height = ast.lines
    charlist1 = ["O","|","-","+","/"]
    charlist2 = ['!','#','%','^', '&', '}', "o", ">", "~"]
    ra = random.randint(3,8)
    b1 = sd.parallelogram(random.randint(6,19), random.randint(40,60),ra, charlist1[random.randint(0,len(charlist1)-1)])
    pb1 = sd.padMidMax(b1,columns,height)
    b2w = random.randint(6,35)
    b2 = sd.parallelogram(random.randint(30,50),b2w, random.randint(3,8), charlist2[random.randint(0,len(charlist2)-1)])
    pb2 = sd.padMidMax(b2,columns,height)
    size = min(columns/4, size)
    for x in range(int(columns/2) - size ,int(columns/2) + size):
        mb = sd.mergeBuffers(pb1, pb2, x )
        ast.printMultilineonstage(mb,0,ast.lines)
        time.sleep(framewait)



def rtext(font="big", word1 = "data", word2 = "intersect"):
    # ast.clearstage()
    ast.printonstage("", 0, 0)
    ast.printFigletAtRandomLoc(word1, font)
    # time.sleep(0.1)
    # ast.clearstage()
    ast.printFigletAtRandomLoc(word2, font)

def text(x,y,font="big", word1 = "data", word2 = "intersect"):
    
    # ast.printonstage(str(y),0,0)
    ast.printonstage("", 0, 0)
    w,h,t = ast.printFiglet(word1, font, x=x, y=y)
    ast.printFiglet(word2, font, x, y-h-2)







######################
###### inverted cat###
######################

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

def invertedHorizontalCat(word, words, mask, masktype , columns, height):
    """
    inverted cat writes cat by leaving out cat and filling 
    the rest of the page with charachters and words associated with the word
    scale scales the font
    returns multilinebuffer
    """    
    buffer = """"""
    partssize = int(columns/len(word))
    scale = int((partssize - 2)/5)
    if scale > 5 : scale = 5
    if scale < 1 : scale = 1
    blankrows = int((height - 7*scale)/ 2) 
    buffer += ("x"*columns+"\n")*blankrows
    c_row = 0
    while c_row < 9:
        sc = 0
        while sc < scale:
            bl = "x"*int(scale/2)
            # bl += "x"*int(partssize/2)
            for i,c in enumerate(word):
                if mask[i] == "x":
                    print("##################", word)
                    xline = fa.font5x9[c][c_row]
                else:
                    if masktype == "none":
                        xline = fa.font5x9[c][c_row]
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
                try:
                    print(words)
                    worderror = next(words)
                    letterline += strip2ascii(worderror)
                except StopIteration:
                    time.sleep(0.1) ## DIRTY HACK for co-routine error
                    letterline += ""
            else:
                letterline += " "
        letterbuffer +=letterline +"\n"
        
    return letterbuffer
# testword = "cyborg"

# while(True):
#     for i in range(len(testword)):
#         bf = invertedHorizontalCat (testword,cyclemask(testword, 1/len(testword)*i, 0.5) , "invert", 120, 40)
#         ast.printMultilineonstage(bf,0,40)
#         time.sleep(0.3)
#     # bf = invertedHorizontalCat ("cyborg", randomMask("cyborg", 0.1), "invert", 120, 40)
#     # ast.printMultilineonstage(bf,0,40)
#     # time.sleep(0.5*random.random())



########################
#### banner #############
########################

def banner(banner,x,y, noisestep=0.1, seed=1337, noisechar=".", octaves=8):
    """
    print and play with buffer
    """    
    if banner == "logo":
        buffer = aa.logo
        buffer = sd.padMidMax(buffer, ast.columns, ast.lines)
        ast.printMultilineonstage(buffer,x,y)
    elif banner == "banner":
        buffer = aa.banner
        buffer = sd.padMidMax(buffer, ast.columns, ast.lines)
        mergedbuffer = noiser(buffer, noisestep, seed, noisechar, octaves)
        ast.printMultilineonstage(mergedbuffer,x,y)
    elif banner == "lbf1":
        buffer = aa.lbf1
        buffer = sd.padMidMax(buffer, ast.columns, ast.lines)
        mergedbuffer = speckles(buffer, octaves/100 , ["L","B", "F"])
        ast.printMultilineonstage(mergedbuffer,x,y)
    elif banner == "lbf2":
        buffer = aa.lbf2
        buffer = sd.padMidMax(buffer, ast.columns, ast.lines)
        mergedbuffer = speckles(buffer, octaves/100 , ["l","b", "f"])
        ast.printMultilineonstage(mergedbuffer,x,y)
    elif banner == "lbf3":
        buffer = aa.lbf3
        buffer = sd.padMidMax(buffer, ast.columns, ast.lines)
        # mergedbuffer = speckles(buffer, octaves/100 , ["l","b", "f"])
        ast.printMultilineonstage(buffer,x,y)





def speckles(buffer, amount = 0.5, char = [ "%", "^", ";" ]):
    mergedbuffer = ""
    for i,l in enumerate(buffer.splitlines()):
        line = ""
        for j,c in enumerate(l):
            if random.random() < amount:
                c = random.choice(char) 
            line = line + c
        mergedbuffer = mergedbuffer + line + "\n" 
    return mergedbuffer


def noiser (buffer, noisestep, seed, noisechar, octaves):
    octaves = 4
    # seed = random.randint(0,123234)
    nchars = ["o"]
    xnoise, ynoise = sd.dimensions(buffer)
    noise = PerlinNoise(octaves=octaves, seed=seed)
    # noisestep = 0.1
    if noisestep == "" : noisestep = 0.0
    noisebuffer = [[noise([i/xnoise + noisestep, j/ynoise + noisestep]) for j in range(xnoise)] for i in range(ynoise)]
    # noisechar = nchars[random.randint(0,len(nchars)-1)]
    mergedbuffer = ""
    for i,l in enumerate(buffer.splitlines()):
        line = ""
        for j,c in enumerate(l):
            if c != " ":
                if noisebuffer[i][j] > 0:
                    c = noisechar
            line = line + c
        mergedbuffer = mergedbuffer + line + "\n" 
    return mergedbuffer