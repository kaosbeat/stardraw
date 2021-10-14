#!/usr/bin/python3

import lib.starLC20 as p
import lib.staremulator as s
import random

import time
import mido
import sqlite3

# showtime
con=sqlite3.connect('Belgium14.sqlite')
cur = con.cursor()
# cur.execute( 'SELECT * FROM db_sanitized14 WHERE relationshipstatus = "It\'s complicated"')
# cur.execute( 'SELECT relationshipstatus FROM db_sanitized14 WHERE relationshipstatus != ""' )

relationshipstatusses = ["\"In a relationship\"",  "\"It\'s complicated\"", "\"Divorced\"", "\"Engaged\"", "\"Widowed\"", "\"Single\"", "\"Married\"", "\"\""] 

global data
r = cur.fetchone()

data = list(cur)
# print (data)


# listen to MIDI from AXO
print(mido.get_input_names())
# inport = mido.open_input('Axoloti Core:Axoloti Core MIDI 1 20:0')
inport = mido.open_input('Pure Data:Pure Data Midi-Out 1 128:1')

def putPersonInTable():
    #print random persons name from the data in a hokje
    # data ik een hokje duwen

    # get 
    zone = random.randint(0,7)
    rs = relationshipstatusses[zone]
    statement = 'SELECT firstname FROM db_sanitized14 WHERE relationshipstatus =' + rs
    print(statement)
    cur.execute(statement)
    data = list(cur)
    # print(data[random.randint(0,len(data)-1)][0] + " is in"  + rs)
    # get random person 

    return (data[random.randint(0,len(data)-1)][0], zone)

def printsvg():
    s.svgfile = 'humansinbox.svg'
    s.openfile(s.svgfile)

    density = 6
    p.setNewDensityAndGotoTop(density, p.pageheight, p.linefeed)
    s.setNewDensityAndGotoTop(density, p.pageheight, p.linefeed)
    height = int(p.pageheight*12/p.linefeed)
    print ("heigth = ", height )
    # +--+--+
    # |  |  |
    # +--+--+
    # |  |  |
    # +--+--+
    margin = 10
    zones = [((0,39-margin),(0,34-margin)),((39,78-margin),(0,34-margin)),
             ((0,39-margin),(34,68-margin)),((39,78-margin),(34,68-margin)),
             ((0,39-margin),(68,102-margin)),((39,78-margin),(68,102-margin)),
             ((0,39-margin),(102,136-margin)),((39,78-margin),(102,136-margin))]
                 
    for z in range(500):
        buffer,zone = putPersonInTable()
        x = zones[zone][0]
        y = zones[zone][1]
        X = random.randint(x[0],x[1])
        Y = random.randint(y[0],y[1]) + 2
        s.printBuffer(buffer,X,Y,height)
        p.printBuffer(buffer,X,Y,height)





    # signature = signstring("anomaly squares")
    # p.printXY(signature, 80-len(signature), totalheight-int(2*12/p.linefeed))
    # s.printXY(signature, 80-len(signature), totalheight-int(2*12/p.linefeed))
    s.closefile()





def midiparse(msg):
    global data
    # print(msg)
    if msg.note > 2:
        print(data[random.randint(0,len(data)-1)][2])

# generate speech

printsvg()

def app():
    try:
        while True:
            pass
            time.sleep(1)
            # putPersonInTable()
    except KeyboardInterrupt:
        pass    


inport.callback = midiparse
app()