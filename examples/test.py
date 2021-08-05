#!/usr/bin/python3



# def feedmeweirdmusic(posx,posy,rot,invert):
# 	xcounter = 0
# 	cols = ["feed","me","weird","music","and","I","will","grow","a","beard","filled","with","riddles","and","it","will","flow","and","grow","like","a","waterfall","grows","from","a","glacier","that","melts","like","it's","2019"]
# 	colsstate = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
# 	# colsstate = [1,1,0,1,1,0,1,1,0,1,1,0,1,0,1,1,0,1,1,1,1,1,1,1,0,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
# 	# feeder = dwg.add(dwg.g(id="feeder" ,  class_="feeder", transform="translate("+str(posx)+","+str(posy)+"), rotate("+str(rot)+")"))
#     # text = " "
# 	for row in xrange(1,350):
# 		for col in xrange(len(cols)):
# 			print(cols[row%(col+1)])
# 			if (row%(col+1) == 0):
# 				if (colsstate[col] == 1):
# 					colsstate[col] = 0
# 				elif (colsstate[col] == 0):
# 					colsstate[col] = 1
# 			# print(colsstate)
# 		# 	if invert:
# 		# 		if (colsstate[col] == 0):	
# 		# 			# feeder.add(dwg.text(cols[col], class_="fontww" , insert=(xcounter*printerboxfontsize/1.75, printerboxfontsize*row/2), fill='black'))

# 		# 	else:
# 		# 		if (colsstate[col] == 1):
# 		# 			feeder.add(dwg.text(cols[col], class_="fontww" , insert=(xcounter*printerboxfontsize/1.75, printerboxfontsize*row/2), fill='black'))
# 		# 	xcounter = xcounter + len(cols[col])
# 		# xcounter = 0	




# # feedmeweirdmusic(0,0,0,0)



import starLC20 as p
import staremulator as s
import random
import datetime
import starDraw as sd

printit = False
svg = True
sign = True
title = "starLC20"
strat = False
shape = False
landscape = False

def sign(dwg, title, y):
    s.setLineSpace(12)
    p.setLineSpace(12)
    string = '{0:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())
    string = "kaotec []<> " + title + " " + string
    s.printXY(dwg, string, s.columns - len(string), y) 


def signstring(title):
    string = '{0:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())
    string = "kaotec []<> " + title + " " + string
    return string


########################
### strategies page ####
########################
if strat:
    dwg = s.openfile('strategies.svg')
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
            s.printXY(dwg,strategie, i%10, i)
    s.closefile(dwg)


#######################
### shape fill page ###
#######################
if shape:
    dwg = s.openfile('shape.svg')
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
                s.printXY(dwg,line, 0, i+1)
            c1 = c1 - direction
            # c3 = c3 + direction
            i = i +1

        direction = direction * -1
        C1 = random.randint(0, random.randint(0, int(columns / 2)) +1)
        c1 = random.randint(0, int(columns / 2)) +1
        c2 = random.randint(0, int((columns - c1)/2))
        c3 = columns - c1 - c2
    s.closefile(dwg)




##########################
### lanscape fill page ###
##########################
def landscape():
    dwg = s.openfile('landscape.svg')
    signature = signstring("landscape")
    p.setOnLine()
    p.reset()
    # p.beep()
    p.noMargins()
    # p.beep()

    columns = 83
    height = 4

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
            s.printXY(dwg,line, 0, i+1)
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
    # sign(dwg,"landscape",70)
    s.closefile(dwg) 



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
    dwg = s.openfile('planet.svg')
    pl = planet(10,1, '%')
    p.setLineSpace(10)
    s.setLineSpace(10)
    for i,line in enumerate(pl.splitlines()):
        print(line)
        s.printXY(dwg,line, 0, i+11)
        p.printXY(line, 0, i+11)
        s.lf()
        p.lf()


    pl = planet(20,1, '^')
    p.setLineSpace(4)
    s.setLineSpace(4)
    for i,line in enumerate(pl.splitlines()):
        print(line)
        s.printXY(dwg,line, 0,  20 + i+1)
        p.printXY(line, 0,  20 + i+1)
        s.lf()
        p.lf()

    p.setTopAtCurrent()
    s.setTopAtCurrent()

    pl = planet(25,1, '3')
    s.setLineSpace(14)
    p.setLineSpace(14)
    for i,line in enumerate(pl.splitlines()):
        print("printing line at ", i)
        # print(line)
        s.printXY(dwg,line, 0, i-5)
        p.printXY(line, 0, i-5)
        s.lf()
        p.lf()
    s.closefile(dwg) 



 
# landscape()


########################
#### stardraw test #####
########################
dwg = s.openfile('stardraw.svg')

# import random.randint as ri
chars = ['!','#','%','^', '&', '}', "o", ">", "~"]




for i in range(100):
    x1 = random.randint(1,80)
    x2 = random.randint(1,80)
    y1 = random.randint(1,72)
    y2 = random.randint(1,72)
    char = chars[random.randint(0,len(chars)-1)]
    buffer = sd.line(x1,y1,x2,y2,char)
    for i,l in enumerate(buffer.splitlines()):
        print(l)
        s.printXY(dwg,l, 0, i)
        p.printXY(l, 0, i)
        s.lf()
        p.lf()
s.closefile(dwg) 

