#!/usr/bin/python3

#from itertools import count
########################
####  imports ##########
########################
# own libraries
import lib.starLC20 as p
import lib.staremulator as s
import lib.starDraw as sd
import lib.tweetprint as tweet
import lib.font_anomaly as fa
import lib.recaptcha as rc
import lib.timers as tim
import lib.asciistage as ast
import faarasciiart as aa

# other libs
from pyfiglet import Figlet, figlet_format, print_figlet
import random
from perlin_noise import PerlinNoise
import datetime
import db
import time
import mido

########################################
########  options ######################
########################################
printit = False
printit = True
# tweetit = True
tweetit = False
global screenit
screenit = False
screenit = True
ast.screenit = screenit
global debug
debug = True
debug = False
s.debug = debug
p.debug = debug
db.debug = debug
# screenit = True
svg = True
sign = True
title = "starLC20"
midicontrol = True
# midicontrol = False

######################################
############ globals #################
######################################
global printing
printing = False
global state
state = "init"

######################################
########## quicktests ################
######################################

# w,h,text1 = ast.figProps("DATA", "big")
# w,h,text2 = ast.figProps("INTERSECT", "big")
# ast.mergeFiglets (text1,text2, 2,12,12,-5)
# time.sleep(20)



########################################
###########  MIDI INIT #################
########################################
# start rtpmidi for connections over network
# listen to MIDI from AXO
# if debug: print(mido.get_input_names())
# inport = mido.open_input('Axoloti Core:Axoloti Core MIDI 1 24:0')
# if debug: print(mido.get_output_names())
if midicontrol:
    portslist = mido.get_output_names()
    inportslist = mido.get_input_names()
    print("output", portslist  )
    print("input", inportslist  )
    axodevlist = [axo for axo in portslist if "Axoloti" in axo]
    pddevlist = [pd for pd in portslist if "Pure Data" in pd]
    if debug: print(axodevlist)
    if debug: print(pddevlist)
    
    if len(axodevlist) > 0 :
        outport = mido.open_output(axodevlist[0])
    else:
        # outport = mido.open_output('Midi Through:Midi Through Port-0 14:0')
        # outport = mido.open_output('Pure Data:Pure Data Midi-Out 1 130:1')
        outport = mido.open_output(pddevlist[0])
        # outport= mido.open_output(portslist[-1])
    # inport = mido.open_input('Midi Through:Midi Through Port-0 14:0')
    # inport = mido.open_input('Pure Data:Pure Data Midi-In 1 130:0')
    # inport = mido.open_input(inportslist[4])
    inport = mido.open_input(inportslist[0])
    # inport = mido.open_input('Pure Data:Pure Data Midi-Out 1 128:1')

##########################################
############ MIDI messages ###############
##########################################
#########
## OUT ##
#########

def midi_playsample(sample=41):
    """
    41 = explsh1
    42 = Soyuz3commando
    """
    if midicontrol:
        msg = mido.Message('note_on', channel=0, note=sample, velocity=127, time=0)
        outport.send(msg)

def midi_sawglitch():
    if midicontrol:
        msg = mido.Message('note_on', channel=0, note=43, velocity=127, time=0)
        outport.send(msg)


def midi_printnoise():
    if midicontrol:
        msg = mido.Message('note_on', channel=0, note=41, velocity=127, time=0)
        outport.send(msg)

def midi_datanoise():
    if midicontrol:
        msg = mido.Message('note_on', channel=0, note=42, velocity=127, time=0)
        outport.send(msg)  

##########
### IN ###
##########

def midiparse(msg):
    global data
    # if debug: print(msg)
    if msg.note > 2:
        if debug: print(data[random.randint(0,len(data)-1)][2])




############################################
#####   defs PAGES to print ################
############################################

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
            # if debug: print(len(line))
            for x in range(c2):
                line = line + l2
            # if debug: print(len(line))
            for x in range(c3):
                line = line + l3
            line = line[0:80]
            if debug: print(line)

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
            # if debug: print(len(line))
            for x in range(c2):
                line = line + names[count]
                count = count + 1
            # if debug: print(len(line))
            for x in range(c3):
                line = line + " "
            line = line[0:80]
            if debug: print(line)

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
    if debug: print(title)
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
            # if debug: print(len(line))
            for x in range(c2):
                try: 
                    names1[count1]
                except IndexError:
                    count1 = 0
                line = line + names1[count1]
                count1 = count1 + 1
            # if debug: print(len(line))
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
            # if debug: print(len(line))
            for x in range(c2):
                try: 
                    names2[count2]
                except IndexError:
                    count2 = 0

                line = line + names2[count2]
                count2 = count2 + 1
            # if debug: print(len(line))
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
    signature = sd.signstring(title)
    sigX = 80-len(signature)
    p.printXY(signature, sigX, int(height)+2)
    s.printXY(signature, sigX, int(height)+2)
    s.closefile()
    if tweetit:
        tweet.convertSVGtoTweet(s.svgfile, "shapefill")




###############################
##### do stuff with data ######
###############################

# if "datastuff" == "needed":\
if True:
    data1 = db.GetMostFRequentNameInRelationstatus("\"In a relationship\"")
    data2 = db.GetMostFRequentNameInRelationstatus("\"It\'s complicated\"")
    # data = db.getAllFromHometown("Antwerp")
    # random.shuffle(data)
    # data1 = db.GetMostFRequentNameInRelationstatusInCity("\"In a relationship\"", "Antwerp")
    # data2 = db.GetMostFRequentNameInRelationstatusInCity("\"It\'s complicated\"", "Antwerp")

    names1 = ""
    for name in data1:
        names1 = names1 + " " + name[0]
        x = random.randint(2,ast.columns-len(name[0]))
        y = random.randint(1, ast.lines-2)
        # ast.printonstage(str(x)+", "+str(y), 0 , ast.lines-1)
        # if debug: print(name[0])
        # ast.printFiglet(name[0],"big")
        # ast.printonstage(name[0], x, y)
        # time.sleep(0.1)
        
    names1 = list(names1)
    names2 = ""
    for name in data2:
        names2 = names2 + " " + name[0]
    names2 = list(names2)
    # rshapes(names1, names2, "it's a complicated relationship")


def printjob(kind):
    if debug: print("printing started", kind)
    # i = random.randint(0,len(jobs)-1)
    # jobs = [rshapes]
    # arguments =[[names1,names2,"it's a complicated relationship"]]
    # i = random.randint(0,len(jobs)-1)
    # jobs[i](arguments[i])
    dice = random.randint(0,6)
    msg = mido.Message('note_on', channel=0, note=dice, velocity=127, time=0)
    outport.send(msg)
    if dice == 0:
        rshapes(names1,names2, "it's a complicated relationship")
    if dice == 1:
        rshapes(names1,names2, "it's a kind of a relationship")
    if dice == 3:
        rshapes(names1,names2, "it's a very complicated relationship")
    if dice == 4:
        rshapes(names1,names2, "it's somekind of a relationship")
    if dice == 5:
        rshapes(names1,names2, "it's a simplified relationship")
    if dice == 6:
        rshapes(names1,names2, "it's a one of a kind relationship")

    # p.setNewDensityAndGotoTop(12,p.pageheight,p.linefeed)
    # p.nextTop()
    # p.lf()
    if debug: print("printing stopped, sleeping 120 sec")
    time.sleep(10)
    if debug: print("ready for new job")


def imnotarobot(blah):
    global printing
    if not printing:
        #make some sound
        printing = True
        if debug: print("trying to make sound")
        msg = mido.Message('note_on', channel=0, note=41, velocity=127, time=0)
        outport.send(msg)
        time.sleep(10)
        if debug: print("stopping sound")
        msg = mido.Message('note_off', channel=0, note=41, velocity=127, time=0)
        outport.send(msg)
        # msg = mido.Message('control_change', channel=0, control=126, value=0)
        # outport.send(msg)
        printjob("from robot") ##blocking
        printing = False
        # rt = RepeatedTimer(30, imnotarobot, "World")


def startprintwithdata(blagh):
    global printing
    if not printing:    
        printing = True
        if debug: print("trying to make sound")
        printjob("from robot") ##blocking
        printing = False

# rt = tim.RepeatedTimer(5, startprintwithdata, "World") # it auto-starts, no need of rt.start()


# def app():
#     global printing
#     try:
#         while True:
#             pass
#             time.sleep(5)
#             print ("this ir sunning from the main")
#             # putPersonInTable()
#     except KeyboardInterrupt:
#         pass    

if midicontrol:
    inport.callback = midiparse
# app()

######################################
##### drawing data to the console ####
######################################


# ast.printonstage("hello at 20,20", 20, 20)
# ast.printonstage("hello at 30,20", 30, 20)
# ast.printonstage("hello at 20,40", 20, 40)
# ast.printonstage("hello at 20,10", 20, 10)
# for i in range (ast.columns-3):
#     for j in range(ast.lines-3):
#         ast.printonstage("!",i,j)


# ast.printFiglet("verymuchtoolongstringtooprint", "big", 1, 50)




# time.sleep(50)
# ast.scrollFiglet("welcome to data intersections", "big", 15, 0.01, 5)

# ast.printFiglet("DATA", "big", 2, 42)
# ast.printFiglet("INTERSECT", "big", 2, 32)
# ast.printFiglet("STUDY", "big", 2, 22)

# ast.doNoise(2, ast.columns-2 , 1 , ast.lines-1, 0.01)



########################################
####### scenes or soundscapes ##########
########################################
#########################
##### boot sequence #####
#########################

#1 Booting KaOS, bleeps and
def bootseq():
    global state
    state = "boot"
    framewait = 0.5
    ast.initstage("scroll")
    ast.printFiglet("DATA ", "big", 2, ast.lines-2)
    time.sleep(framewait)
    ast.printFiglet("INTERSECT", "big", 8, ast.lines-11)
    ast.printFiglet("#@7@", "big", 2, ast.lines-2)
    time.sleep(framewait)
    ast.printFiglet("DATA ", "big", 2, ast.lines-2)
    ast.printFiglet("/n13%$&CT", "big", 2, ast.lines-11)
    time.sleep(framewait)
    ast.printFiglet("INTERSECT", "big", 2, ast.lines-11)
    time.sleep(framewait)
    w,h,text1 = ast.figProps("DATA", "big")
    w,h,text2 = ast.figProps("INTERSECT", "big")
    # print(text1)
    for i in range(10):
        time.sleep(framewait)
        mergestep = ast.mergeFiglets (text1,text2, 0,0,8,11-i)
        # print(mergestep)
        ast.printMultilineonstage(mergestep, 2, ast.lines-2)
    ast.scrollFiglet("STUDY", "big", 10, 0.01, 2)
    #2 data intersect studies  ,
    #3  waiting for signal
    ast.initstage()
    ast.blinkFiglet(2,20,"waiting for","big", 2,20,"signal!",None,0.5,)
    time.sleep(framewait)
    ast.doNoise(1,ast.columns-1,1,ast.lines-1,0.01,100)
    ast.initstage
    state = "done"


# bootseq()
# time.sleep(10)

################
#### signal ####
################
def perspsquaressignal(times):
    global state
    state = "signal"
    s.svgfile = 'perspsquaressignal.svg'
    columns = max(80,ast.columns)
    height = max(ast.lines,69)
    s.openfile(s.svgfile)
    chars = ['!','#','%','^', '&', '}', "o", ">", "~"]
    # chars= ["o"]
    density = 8
    p.setLineSpace(density)
    s.setLineSpace(density) 
    height = int(height*12/density)
    for k in range(times):
        midi_playsample(random.randint(1,8))
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
            # prevbuffer=""""""
            x1 = sx + i*dx
            x2 = sx + i + i*dx 
            y1 = sy + i*dy
            y2 = sy + i + i*dy
            # print (x1,y1,x2,y2)
            # szie = size - 1
            charh = chars[random.randint(0,len(chars)-1)]
            charv = chars[random.randint(0,len(chars)-1)]
            # this here 
            # charh = "-"
            # charv = "|"
            buffer = sd.square2(x1,y1,x2,y2,charh,charv)
            # w,h = sd.dimensions(prevbuffer)
            if printit:
                for i,l in enumerate(buffer.splitlines()):
                    if (i<=height-1):
                        if (l != ""):
                            s.printXY(l, 0, height-h+i)
                            p.printXY(l, 0, height-h+i)
            if screenit:
                prevbuffer = ast.mergeFiglets (prevbuffer,buffer,0,0,0,0)
                ast.printMultilineonstage(prevbuffer, 0, h)
                time.sleep(0.1)
                


        midi_playsample(9)
        # time.sleep(5*random.random())
    signature = sd.signstring("signal squares")
    p.printXY(signature, 0, int(height))
    s.printXY(signature, 0, int(height))
    s.closefile() 
    # time.sleep(5)
    if tweetit:
        tweet.convertSVGtoTweet(s.svgfile, "signal received")
    state = "done"

############################
##### repeating signal #####
############################

def repSignal():
    global state
    state = "signal"
    # ast.blinkFiglet(10, ast.lines-10, "incoming signal", "big", 10, ast.lines - 25, "processing ...", "big", 0.5, 3)
    ### generate 1 row
    s.svgfile = 'repSignal.svg'
    columns = 80
    height = 69
    s.openfile(s.svgfile)
    s.setLineSpace(12)
    # s.setLineSpace(7)
    p.setLineSpace(12)
    # p.setLineSpace(7)
    x = 6
    y = 5 # y=5 fits page with setLineSpace 12, when using setLinespace(7), y can be 8 
    size = int(columns/(x+1))
    margin = int((columns - (x*size)) / x)
    chars = ["*","X", "#","+", "=", "-", "<", ">" ,".", "*","X", "#","+", "=", "-", "<", ">" ,"."]
    # chars = ["1","2", "3","4", "5", "6", "7", "8" ,"9", "0","a", "b","c", "d", "e", "f", "g" ,"h"]
    count=0 
    buffer = ""
    pagebuffer = ""
    screenbuffer = []
    noise = PerlinNoise()
    for l in range(y):
        # size = 30
        anomalyx = [random.randint(0,size),random.randint(0,size) ,random.randint(0,size) ,random.randint(0,size),random.randint(0,size),random.randint(0,size) ,random.randint(0,size) ,random.randint(0,size),random.randint(0,size),random.randint(0,size) ,random.randint(0,size) ,random.randint(0,size)]
        anomalyy = [random.randint(0,size),random.randint(0,size) ,random.randint(0,size) ,random.randint(0,size),random.randint(0,size),random.randint(0,size) ,random.randint(0,size) ,random.randint(0,size),random.randint(0,size),random.randint(0,size) ,random.randint(0,size) ,random.randint(0,size)]
        # size = int(columns/(x+1))
        for i in range(size):
            line=""
            for k in range(x):
                xstep = 1 / (anomalyy[k]+0.2)
                noisebuf = int(anomalyx[k] * noise(xstep*i))
                linebuf = noisebuf*chars[k+l] + (size-noisebuf)*chars[random.randint(0,len(chars)-1)]
                if anomalyx[k] < size:
                    anomalyx[k] = anomalyx[k] + 1
                line = line + linebuf + " "*int(margin) 
            buffer = buffer + line + "\n"
        for i in range(margin):
            line =""
            buffer = buffer + line + "\n"
            # buffer = buffer + "\n\n"
        # ast.printMultilineonstage(buffer, 3, ast.lines - size*l - count -2)
        screenbuffer.append(buffer)
        pagebuffer = pagebuffer + buffer
        buffer = ""
        count += 1
    # s.printBuffer(pagebuffer,0,5,int(height*12/p.linefeed))
    # p.printBuffer(pagebuffer,0,5,int(height*12/p.linefeed))
    l=0
    for b in screenbuffer:
        s.printBuffer(b,0,5+l*size+l,int(height*12/p.linefeed))
        p.printBuffer(b,0,5+l*size+l,int(height*12/p.linefeed))
        # ast.printMultilineonstage(b, 3, ast.lines - size*l - l -2, 0.1)
        for i,L in enumerate(b.splitlines()):
            ast.printonstage(L,3, ast.lines-size*l-l-2-i)
            midi_sawglitch()
            time.sleep(0.5)
        l += 1
        time.sleep(1)

    signature = sd.signstring("signalsquares")
    p.printXY(signature, 80-len(signature), int(height*12/p.linefeed)-int(1*12/p.linefeed))
    s.printXY(signature, 80-len(signature), int(height*12/p.linefeed)-int(1*12/p.linefeed))
    if tweetit:
        tweet.convertSVGtoTweet(s.svgfile, "anomaly squares")
    s.closefile()    

def finishSignalCapture():
    global state
    state = "signaldone"
    buffer = aa.phone
    ast.printMultilineonstage(aa.phone, 2,ast.lines - 3)
    # ast.blinkFiglet(buffer,1,2)


#1 receive trigger
# ast.initstage()
ast.quickinit()

perspsquaressignal(10)
# repSignal()
# ast.quickinit()
# repSignal()
# ast.quickinit()
# finishSignalCapture()
time.sleep(1)
# ast.printonstage("test", 23, 20)

#2 harsh noises emitted, they fade out into delay, meanwhile 
#3 printer starts printing
#3 print signal! (lines?, overlapscapes, perspsquares, shape)

###########################
#### signal processing ####
###########################

#1 saw
#2 2nd saw
#3 3rd saw
#4 LFOs to tune/detune
#5 printing of waves feedmeweirdtext(), interferencepatterns(), overlapstudy()  

###########################
##### signal or noise #####
###########################

#  fillingsquares()









########################
#### signal to data ####
########################



# cube()


# midi_printnoise


