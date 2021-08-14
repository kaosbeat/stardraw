#!/usr/bin/python3

import lib.starLC20 as p
import lib.staremulator as s
import random
import datetime
import lib.starDraw as sd
import lib.tweetprint as tweet

printit = False
tweetit = True
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


########################
### strategies page ####
########################
def strategies():
    s.openfile('strategies.svg')
    strategies = [ "(Organic) machinery", "A line has two sides", "A very small object: Its center", "Abandon desire", "Abandon normal instructions", "Abandon normal instruments", "Accept advice", "Accretion", "Adding on", "Allow an easement (an easement is the abandonment of a stricture)", "Always first steps", "Always give yourself credit for having more than personality (given by Arto Lindsay)", "Always the first steps", "Are there sections?  Consider transitions", "Ask people to work against their better judgement", "Ask your body", "Assemble some of the elements in a group and treat the group", "Balance the consistency principle with the inconsistency principle", "Be dirty", "Be extravagant", "Be less critical", "Breathe more deeply", "Bridges   -build   -burn", "Bridges -build -burn", "Cascades", "Change ambiguities to specifics", "Change instrument roles", "Change nothing and continue consistently", "Change nothing and continue with immaculate consistency", "Change specifics to ambiguities", "Children   -speaking     -singing", "Cluster analysis", "Consider different fading systems", "Consider transitions", "Consult other sources   -promising   -unpromising", "Convert a melodic element into a rhythmic element", "Courage!", "Cut a vital conenction", "Cut a vital connection", "Decorate, decorate", "Define an area as `safe' and use it as an anchor", "Destroy  -nothing   -the most important thing", "Destroy nothing; Destroy the most important thing", "Discard an axiom", "Disciplined self-indulgence", "Disconnect from desire", "Discover the recipes you are using and abandon them", "Discover your formulas and abandon them", "Display your talent", "Distort time", "Distorting time", "Do nothing for as long as possible", "Do something boring", "Do something sudden, destructive and unpredictable", "Do the last thing first", "Do the washing up", "Do the words need changing?", "Do we need holes?", "Don't avoid what is easy", "Don't be frightened of cliches", "Don't break the silence", "Don't stress on thing more than another [sic]", "Don't stress one thing more than another", "Dont be afraid of things because they're easy to do", "Dont be frightened to display your talents", "Emphasize differences", "Emphasize repetitions", "Emphasize the flaws", "Faced with a choice, do both (from Dieter Rot)", "Faced with a choice, do both (given by Dieter Rot)", "Feed the recording back out of the medium", "Fill every beat with something", "Find a safe part and use it as an anchor", "Get your neck massaged", "Ghost echoes", "Give the game away", "Give the name away", "Give way to your worst impulse", "Go outside.  Shut the door.", "Go outside. Shut the door.", "Go slowly all the way round the outside", "Go to an extreme, come part way back", "Honor thy error as a hidden intention", "Honor thy mistake as a hidden intention", "How would someone else do it?", "How would you have done it?", "Humanize something free of error", "Idiot glee (?)", "Imagine the piece as a set of disconnected events", "In total darkness, or in a very large room, very quietly", "Infinitesimal gradations", "Intentions   -nobility of  -humility of   -credibility of", "Into the impossible", "Is it finished?", "Is something missing?", "Is the information correct?", "Is the style right?", "Is there something missing", "It is quite possible (after all)", "It is simply a matter or work", "Just carry on", "Left channel, right channel, center channel", "Listen to the quiet voice", "Look at the order in which you do things", "Look closely at the most embarrassing details & amplify them", "Lost in useless territory", "Lowest common denominator", "Magnify the most difficult details", "Make a blank valuable by putting it in an exquisite frame", "Make a sudden, destructive unpredictable action; incorporate", "Make an exhaustive list of everything you might do & do the last thing on the list", "Make it more sensual", "Make what's perfect more human", "Mechanicalize something idiosyncratic", "Move towards the unimportant", "Mute and continue", "Not building a wall but making a brick", "Not building a wall; making a brick", "Once the search has begun, something will be found", "Only a part, not the whole", "Only one element of each kind", "Openly resist change", "Overtly resist change", "Pae White's non-blank graphic metacard", "Put in earplugs", "Question the heroic", "Question the heroic approach", "Reevaluation (a warm feeling)", "Remember quiet evenings", "Remember those quiet evenings", "Remove a restriction", "Remove ambiguities and convert to specifics", "Remove specifics and convert to ambiguities", "Repetition is a form of change", "Retrace your steps", "Reverse", "Short circuit (example; a man eating peas with the idea that they will improve  his virility shovels them straight into his lap)", "Simple Subtraction", "Simple subtraction", "Simply a matter of work", "Slow preparation, fast execution", "Spectrum analysis", "State the problem as clearly as possible", "State the problem in words as clearly as possible", "Take a break", "Take away the elements in order of apparent non-importance", "Take away the important parts", "Tape your mouth (given by Ritva Saarikko)", "The inconsistency principle", "The most easily forgotten thing is the most important", "The most important thing is the thing most easily forgotten", "The tape is now the music", "Think - inside the work -outside the work", "Think of the radio", "Tidy up", "Towards the insignificant", "Trust in the you of now", "Try faking it (from Stewart Brand)", "Turn it upside down", "Twist the spine", "Use 'unqualified' people", "Use `unqualified' people", "Use an old idea", "Use an unacceptable color", "Use cliches", "Use fewer notes", "Use filters", "Use something nearby as a model", "Use your own ideas", "Voice your suspicions", "Water", "What are the sections sections of?    Imagine a caterpillar moving", "What are you really thinking about just now?", "What context would look right?", "What is the reality of the situation?", "What is the simplest solution?", "What mistakes did you make last time?", "What to increase? What to reduce? What to maintain?", "What were you really thinking about just now?", "What would your closest friend do?", "What wouldn't you do?", "When is it for?", "Where is the edge?", "Which parts can be grouped?", "Work at a different speed", "Would anyone want it?", "You are an engineer", "You can only make one dot at a time", "You don't have to be ashamed of using your own ideas"]
    if printit:
        p.setOnLine()
        p.reset()
        # p.beep()
        p.noMargins()
        # p.beep()
    for i in range(80):
        # print(strategies[i%len(strategies)])
        strategie = strategies[random.randint(0,len(strategies))-1]
        if printit:
            p.printXY(strategie, i%10, i)
        if svg:
            s.printXY(strategie, i%10, i)
    s.closefile()
    # tweet.convertSVGtoTweet(s.svgfile, "strategies")

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
    s.closefile()
    tweet.convertSVGtoTweet(s.svgfile, "shapefill")



##########################
### landscape fill page ###
##########################
def landscape():
    s.openfile('landscape.svg')
    signature = signstring("landscape")
    p.setOnLine()
    p.reset()
    # p.beep()
    p.noMargins()
    # p.beep()

    columns = 80
    height = 72

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
            for x in range(columns - c2 - c1):
                line = line + l3
            if (i == height-1):
                line = line[0:columns-len(signature)] + signature
            print(line)
            p.printXY(line, 0, i)
            s.printXY(line, 0, i+1)
            c1 = c1 - direction
            # c3 = c3 + direction
            i = i +1
            if i >= height:
                break

        direction = direction * -1
        C1 = random.randint(0, random.randint(0, int(columns / 2)) +1)
        # c1 = random.randint(0, int(columns / 2)) +1
        c2 = random.randint(0, int((columns - c1)/2))
        # c3 = columns - c1 - c2
    # sign("landscape",70)
    s.closefile() 
    tweet.convertSVGtoTweet(s.svgfile, "landscapes")


#########################
### A BILLION PLANETS ###
#########################

import math

def planet(radius, proportion, char):
    step = 180/radius
    padlength = 2 * radius * proportion * 1.4
    #print(padlength)
    planettxt = ''
    for i in range(radius):
        line = ''
        # x = math.sin(math.radians(step*i)) * proportion * math.cos(math.radians(step*i))
        # x = math.sin(math.radians(step*i)) * proportion * math.sin(math.radians(step/2*i))
        # x = math.sin(math.radians(step*i)) * proportion * math.sin(math.radians(step*2*i))

        x = math.sin(math.radians(step*i)) * proportion 
        # print(x)
        for s in range(int(x*radius )):
            line = line + char
        prelinelength = int((padlength - len(line)*2) / 2)
        bufferline = ' ' * prelinelength
        endline = '' + bufferline + line + line + bufferline + ''
        planettxt = planettxt + endline + '\n'
    return planettxt


def someplanets():
    p.reset()
    s.openfile('planet.svg')
    pl = planet(10,1, '%')
    p.setLineSpace(10)
    s.setLineSpace(10)
    for i,line in enumerate(pl.splitlines()):
        print(line)
        s.printXY(line, 0, i+11)
        p.printXY(line, 0, i+11)

    pl = planet(20,1, '^')
    p.setLineSpace(4)
    s.setLineSpace(4)
    for i,line in enumerate(pl.splitlines()):
        print(line)
        s.printXY(line, 0,  20 + i+1)
        p.printXY(line, 0,  20 + i+1)

    p.setTopAtCurrent()
    s.setTopAtCurrent()

    pl = planet(25,1, '3')
    s.setLineSpace(14)
    p.setLineSpace(14)
    for i,line in enumerate(pl.splitlines()):
        print("printing line at ", i)
        # print(line)
        s.printXY(line, 0, i-5)
        p.printXY(line, 0, i-5)
    s.closefile() 
    tweet.convertSVGtoTweet(s.svgfile, "a billion planets")


########################
#### stardraw test #####
########################
def lotsalines():
    columns = 80
    height = 69
    s.openfile('stardraw.svg')

    # import random.randint as ri
    chars = ['!','#','%','^', '&', '}', "o", ">", "~"]
    for i in range(15):
        x1 = random.randint(1,columns)
        x2 = random.randint(1,columns)
        y1 = random.randint(1,height)
        y2 = random.randint(1,height)
        char = chars[random.randint(0,len(chars)-1)]
        buffer = sd.line(x1,y1,x2,y2,char)
        for i,l in enumerate(buffer.splitlines()):
            print(l)
            s.printXY(l, 0, i)
            p.printXY(l, 0, i)
    signature = signstring("lines")
    p.printXY(signature, columns-len(signature) , height)
    s.printXY(signature, columns-len(signature) , height)
    s.closefile() 
    tweet.convertSVGtoTweet(s.svgfile, "testing some more lines")




##########################
#### squares #############
##########################

def squares():
    s.svgfile = 'squares.svg'
    columns = 80
    height = 69
    s.openfile(s.svgfile)
    chars = ['!','#','%','^', '&', '}', "o", ">", "~"]
    for i in range(15):
        x1 = random.randint(1,columns)
        x2 = random.randint(1,columns)
        y1 = random.randint(1,height)
        y2 = random.randint(1,height)
        charh = chars[random.randint(0,len(chars)-1)]
        charv = chars[random.randint(0,len(chars)-1)]
        bufferlist = sd.square(x1,y1,x2,y2,charh,charv)
        for buffer in bufferlist:
            for i,l in enumerate(buffer.splitlines()):
                print(l)
                s.printXY(l, 0, i)
                p.printXY(l, 0, i)
    signature = signstring("lines")
    p.printXY(signature, columns-len(signature) , height)
    s.printXY(signature, columns-len(signature) , height)
    s.closefile() 
    tweet.convertSVGtoTweet(s.svgfile, "testing squares")



#######################
#### 80ties ########
#######################

def eighties():
    s.svgfile = '80ties.svg'
    columns = 80
    height = 69
    s.openfile(s.svgfile)
    horizon = 30
    #    s.setLineSpace(12)
    divs = 20
    for i in range(divs):
        inc = int(columns/divs)
        print (int(columns/2) , horizon, i*inc , height)
        buffer = sd.brokenline(int(columns/2) , horizon+1, i*inc , height+1, '!')
        for i,l in enumerate(buffer.splitlines()):
            # print(l)
            s.printXY(l, 0, i)
    s.printXY('.', 0, horizon)
    for i in range(18):
        s.setLineSpace(3+i*4)
        s.printXY(columns * '-', 0 , horizon + i)
    # s.currentTop()
 
       

    s.closefile() 
    # tweet.convertSVGtoTweet(s.svgfile, "back in the 80ties")



def linetest():
    s.svgfile = 'linetest.svg'
    s.openfile(s.svgfile)
    xoff = 4
    yoff = 4

    s.printXY("000000000011111111112222222222", 0+xoff, 1)
    s.printXY("012345678901234567890123456789", 0+xoff, 2)
    s.setLineSpace(7.5)
    y=0
    for y in range(30):
        s.printXY(str(y),0, y + yoff)
        y = y + 1
    bufferlist = []
    # bufferlist.append(sd.line(0+xoff,0+yoff,10+xoff,10+yoff,'1'))
    # bufferlist.append(sd.line(20+xoff,20+yoff,10+xoff,10+yoff,'2'))
    # bufferlist.append(sd.line(10+xoff,0+yoff,0+xoff,0+yoff,'3'))
    # bufferlist.append(sd.line(10+xoff,0+yoff,20+xoff,0+yoff,'4'))
    # bufferlist.append(sd.line(0+xoff,0+yoff,0+xoff,10+yoff,'5'))
    # bufferlist.append(sd.line(0+xoff,20+yoff,0+xoff,10+yoff,'6'))
    # bufferlist.append(sd.line(20+xoff,0+yoff,10+xoff,10+yoff,'7'))
    # bufferlist.append(sd.line(0+xoff,20+yoff,10+xoff,10+yoff,'8'))
    # bufferlist.append(sd.line(20+xoff,0+yoff,20+xoff,10+yoff,'9'))
    # bufferlist.append(sd.line(20+xoff,20+yoff,20+xoff,10+yoff,'0'))
    bufferlist.append(sd.line(0+xoff,0+yoff,10+xoff,10+yoff,'auto'))
    bufferlist.append(sd.line(20+xoff,20+yoff,10+xoff,10+yoff,'auto'))
    bufferlist.append(sd.line(10+xoff,0+yoff,0+xoff,0+yoff,'auto'))
    bufferlist.append(sd.line(10+xoff,0+yoff,20+xoff,0+yoff,'auto'))
    bufferlist.append(sd.line(0+xoff,0+yoff,0+xoff,10+yoff,'auto'))
    bufferlist.append(sd.line(0+xoff,20+yoff,0+xoff,10+yoff,'auto'))
    bufferlist.append(sd.line(20+xoff,0+yoff,10+xoff,10+yoff,'auto'))
    bufferlist.append(sd.line(0+xoff,20+yoff,10+xoff,10+yoff,'auto'))
    bufferlist.append(sd.line(20+xoff,0+yoff,20+xoff,10+yoff,'auto'))
    bufferlist.append(sd.line(20+xoff,20+yoff,20+xoff,10+yoff,'auto'))
    bufferlist.append(sd.line(10+xoff,20+yoff,0+xoff,20+yoff,'auto'))
    bufferlist.append(sd.line(10+xoff,20+yoff,20+xoff,20+yoff,'auto'))

    print (bufferlist)
    for buffer in bufferlist:
        for i,l in enumerate(buffer.splitlines()):
            s.printXY(l, 0, i)
        s.closefile() 






###################################
#####   81ties!!!!!!!!!!  #########]
###################################





def eighty1ties():
    s.svgfile = '81ties.svg'
    columns = 80
    height = 69
    s.openfile(s.svgfile)
    horizon = 40
    s.setLineSpace(12)
    divs = 20
    for i in range(divs):
        inc = int(columns/divs)
        # print (int(columns/2) , horizon, i*inc , height)
        buffer = sd.line(int(columns/2) , horizon+1, 4 * columns - 8 * i * inc  , height+1, 'auto')
        for i,l in enumerate(buffer.splitlines()):
            # print(l)
            s.printXY(l, 0, i)
    s.printXY('.', 0, horizon)
    for i in range(15):
        s.setLineSpace(3+i*4)
        s.printXY(columns * '-', 0 , horizon + i)
    s.currentTop()
    s.setLineSpace(12)
    ch = 0
    maxheight =35
    # prefilledbuffer = ""
    # for i in range(maxheight):
    #     prefilledbuffer = prefilledbuffer + columns * " " + "\n"

    while ch < columns+10:
        w = random.randint(3,6)
        h = random.randint(w*2, w*4)
        if h > maxheight:
            h = maxheight
        b = sd.building(w,h)
        # print (b)
        for i,l in enumerate(b):
            printheight = horizon - h + i
            # print(printheight)
            s.printXY(l,ch,printheight)
        ch = ch + w + 2

    s.currentTop()
    s.setLineSpace(12)
    for i in range(20):
        px = random.randint(0,70)
        py = random.randint(0,45)-5
        char = ["^","o", "O", "x"]
        c = char[random.randint(0,len(char)-1)]
        pl = planet(random.randint(10,25),1.5-random.random()*2, c)
        p.setLineSpace(4)
        s.setLineSpace(4)
        for i,line in enumerate(pl.splitlines()):
            print(line)
            s.printXY(line, px,  py + i+1)
            p.printXY(line, px,  py + i+1)
        # px = 5
    # py = 10
    # pl = planet(20, 0.8, 'o')
    # p.setLineSpace(6)
    # s.setLineSpace(6)
    # for i,line in enumerate(pl.splitlines()):
    #     print(line)
    #     s.printXY(line, px,  py + i+1)
    #     p.printXY(line, px,  py + i+1)


    s.closefile()
    if tweetit:
        tweet.convertSVGtoTweet2(s.svgfile, "skysc(r)aping eighty1ties")


#############################    
######  overlapscape     ####
#############################

def overlapscape():
    s.svgfile = 'overlapscapes.svg'
    columns = 80
    height = 69
    pages = 1
    s.openfile(s.svgfile)
    layers  = 3
    char = ["+","!", "X", "x"]
    # char = ["1","2","3","4"]
    for l in range(layers):    
        c = char[random.randint(0,len(char)-1)]
        # c = char[l]
        lbuffer= ""
        density = random.randint(3,15)
        s.currentTop()
        p.setLineSpace(density)
        s.setLineSpace(density)  
        maxheight = random.randint(columns/2,columns)
        minheight = random.randint(0,maxheight)
        prevheight = random.randint(minheight,maxheight)
        direction = random.randint(0,10)-5
        for x in range(0,int(height*pages*(12/density))):
            line = prevheight * c
            lbuffer = lbuffer + line + "\n"
            prevheight = prevheight + direction
            if prevheight > maxheight:
                direction = direction = random.randint(0,5) * -1
            if prevheight < minheight:
                direction = direction = random.randint(0,5) * 1
            for i,line in enumerate(lbuffer.splitlines()):
                print(line)
            s.printXY(line, 0,  x+1)
            p.printXY(line, 0,  x+1)
        print(lbuffer)
    s.closefile()
    if tweetit:
        tweet.convertSVGtoTweet(s.svgfile, "overlapscape")

###########################
### feed me weird texts ###
###########################

def feedmeweirdtxt():
    s.svgfile = 'feedmeweirdtxt.svg'
    columns = 80
    invert = True
    height = 69
    pages = 1
    s.openfile(s.svgfile)
    density = 6
    p.setLineSpace(density)
    s.setLineSpace(density) 
    xcounter = 0
    # dirty hack, append "" as first element in cols if not... troubles
    cols = ["","feed","me","weird","music","and","I","will","grow","a","beard","filled","with","riddles"]
    cols = ["", "a", "landscape", "unfolds", "by", "making", "walks", "and", "speaking", "with", "passersby", "about", "the","state","of","the","weather"]
    cols = ["]","[","q","w","5","%","#","^","&","O","]","[","q","w","5","%","#","^","&","O","]","[","q","w","5","%","#","^","&","O","]","[","q","w","5","%","#","^","&","O","]","[","q","w","5","%","#","^","&","O","]","[","q","w","5","%","#","^","&","O","]","[","q","w","5","%","#","^","&","O","]","[","q","w","5","%","#","^","&","O"]
    cols = []
    colssentence = "I wish I had duck feet, so I could swim like a pro"
    for c in colssentence:
        cols.append(c)
    # the sume of the cols words should be <= to columns
    colsstate = []
    for w in cols:
        xcounter = xcounter + len(w)
        colsstate.append(1)
    # print(xcounter)
    for row in range(1,int(height*12/density)):
        line = ""
        for col in range(len(cols)):
            # print("col = ", col)
            # print(cols[row%(col+1)])
            if (row%(col+1) == 0):
                if (colsstate[col] == 1):
                    colsstate[col] = 0
            elif (colsstate[col] == 0):
                colsstate[col] = 1
            # print(colsstate)
            if (colsstate[col] == 0):
                # print(cols[col])
                if invert:
                    line = line + cols[col]
                else:
                    line = line + " " * len(cols[col])
            if (colsstate[col] == 1):
                if invert:
                    line = line + " " * len(cols[col])
                else:
                    line = line + cols[col]
        print (line)

        s.printXY(line,0,row)
    print(xcounter)
    s.closefile() 
    if tweetit:
        tweet.convertSVGtoTweet(s.svgfile, "weird texts")

###########################
### perspective squares ###
###########################


def perspsquares():
    s.svgfile = 'perspsquares.svg'
    columns = 80
    height = 69
    s.openfile(s.svgfile)
    chars = ['!','#','%','^', '&', '}', "o", ">", "~"]
    # chars= ["o"]
    density = 8
    p.setLineSpace(density)
    s.setLineSpace(density) 
    height = int(height*12/density)
    for k in range(15):
        sx = random.randint(1,columns)
        sy =  random.randint(1,height)
        size =  random.randint(8,18)
        # size = 10
        dx = random.randint(0,4) - 2
        dy = random.randint(0,4) - 2
        ds = random.randint(0,4) - 2

        for i in range(size):
            x1 = sx + i*dx
            x2 = sx + i + i*dx 
            y1 = sy + i*dy
            y2 = sy + i + i*dy
            print (x1,y1,x2,y2)
            # szie = size - 1
            charh = chars[random.randint(0,len(chars)-1)]
            charv = chars[random.randint(0,len(chars)-1)]
            # this here 
            charh = "-"
            charv = "|"
            bufferlist = sd.square(x1,y1,x2,y2,charh,charv)
            for buffer in bufferlist:
                # print(buffer)
                for i,l in enumerate(buffer.splitlines()):
                    if (i<=height-1):
                        if (l != ""):
                            s.printXY(l, 0, i)
                            p.printXY(l, 0, i)
    signature = signstring("squares")
    p.printXY(signature, 0, int(height))
    s.printXY(signature, 0, int(height))
    s.closefile() 
    if tweetit:
        tweet.convertSVGtoTweet(s.svgfile, "testing squares")

def perspsquares2():
    s.svgfile = 'perspsquares.svg'
    columns = 80
    height = 69
    s.openfile(s.svgfile)
    chars = ['!','#','%','^', '&', '}', "o", ">", "~"]
    # chars= ["o"]
    density = 8
    p.setLineSpace(density)
    s.setLineSpace(density)
    height = int(height*12/density)
    # flip = True
    flip = False
    for k in range(2):
        sx = 1 + k
        sy =  1 + k
        size =  40
        dx = 2 
        dy = 2 - k
        ds = random.randint(0,4) - 2
        for i in range(size):
            x1 = sx + i*dx
            x2 = sx + i + i*dx 
            y1 = sy + i*dy
            y2 = sy + i + i*dy
            # szie = size - 1
            charh = chars[random.randint(0,len(chars)-1)]
            charv = chars[random.randint(0,len(chars)-1)]
            bufferlist = sd.square(x1,y1,x2,y2,charh,charv)
            for buffer in bufferlist:
                for i,l in enumerate(buffer.splitlines()):
                    if (i<=height):
                        if (l != ""):
                            if flip:
                                l = l[:80]
                                l = "{:<80}".format(l)[::-1]
                            s.printXY(l, 0, i)
                            p.printXY(l, 0, i)
    signature = signstring("squares")
    p.printXY(signature, 80-len(signature), int(height))
    s.printXY(signature, 80-len(signature), int(height))
    s.closefile()
    if tweetit:
        tweet.convertSVGtoTweet(s.svgfile, "looking for perspective")


def intersect():
    s.svgfile = 'intersect.svg'
    columns = 80
    height = 69
    s.openfile(s.svgfile)
    buffer1 = sd.parallelogram(8, 30,6, "O")
    buffer2 = sd.parallelogram(7, 45,3, "!")
    buffer3 = sd.parallelogram(5, 10,0, "8")
    buffer4 = sd.parallelogram(3, 25,10, "+")

    sd.consoleBuffer(buffer1)
    sd.consoleBuffer(buffer2)

    # s.printBuffer(buffer1,0,0,height)
    # s.printBuffer(buffer2,10,2,height)
    # s.printBuffer(buffer3,20,0,height)    
    # s.printBuffer(buffer4,10,10,height)
    
    b1 = sd.padBuffer(buffer1,10,5,11,12)
    b2 = sd.padBuffer(buffer2,3,4,3,4)

    sd.consoleBuffer(b1)
    sd.consoleBuffer(b2)

    s.printBuffer(b1,0,0,height)
    s.printBuffer(b2,0,0,height)
    

    b3 = sd.mergeBuffers(b1,b2,20)

    s.printBuffer(b3,0,30,height)


    # print(sd.padBuffer(buffer1,10,10, 4,4))

   
    signature = signstring("intersect study")
    p.printXY(signature, 80-len(signature), int(height))
    s.printXY(signature, 80-len(signature), int(height))
    s.closefile()
    if tweetit:
        tweet.convertSVGtoTweet(s.svgfile, "looking for perspective")

 
def intersect2():
    s.svgfile = 'intersect2.svg'
    columns = 80
    height = 69
    s.openfile(s.svgfile)
    # bufferlist=[]
    charlist1 = ["O","|","-","+","/"]
    charlist2 = ['!','#','%','^', '&', '}', "o", ">", "~"]
    maxx = 0
    maxy = 0
    ra = random.randint(3,8)
    b1 = sd.parallelogram(random.randint(6,19), random.randint(40,60),ra, charlist1[len(charlist1)-1])
    # print(b1)
    pb1 = sd.padMidMax(b1,columns,height)
    # print(pb1)
    b2w = random.randint(6,35)
    b2 = sd.parallelogram(random.randint(30,50),b2w, random.randint(3,8), charlist2[len(charlist2)-1])
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


 
# shapes()
# eighties()
# lotsalines()
# squares()
# someplanets()
# landscape()
# linetest()
# eighty1ties()
# overlapscape()
# feedmeweirdtxt()
# perspsquares()
# perspsquares2()
# intersect()
intersect2()

# prefilledbuffer = ""
# for i in range(maxheight):
#     prefilledbuffer = prefilledbuffer + columns * " " + "\n"

