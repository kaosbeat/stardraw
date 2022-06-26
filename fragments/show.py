#!/usr/bin/python3

from lib.starDraw import cube
import lib.starLC20 as p
import lib.staremulator as s
import random
from onepagers import cuber, printbanner, printVersumBanner
import time
import mido
import sqlite3
import threading 

class RepeatedTimer(object):
  def __init__(self, interval, function, *args, **kwargs):
    self._timer = None
    self.interval = interval
    self.function = function
    self.args = args
    self.kwargs = kwargs
    self.is_running = False
    self.next_call = time.time()
    self.start()

  def _run(self):
    self.is_running = False
    self.start()
    self.function(*self.args, **self.kwargs)

  def start(self):
    if not self.is_running:
      self.next_call += self.interval
      self._timer = threading.Timer(self.next_call - time.time(), self._run)
      self._timer.start()
      self.is_running = True

  def stop(self):
    self._timer.cancel()
    self.is_running = False


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
# print(mido.get_input_names())
# inport = mido.open_input('Axoloti Core:Axoloti Core MIDI 1 24:0')
# print(mido.get_output_names())
portslist = mido.get_output_names()
axodevlist = [axo for axo in portslist if "Axoloti" in axo]
print(axodevlist)
if len(axodevlist) > 0 :
    outport = mido.open_output(axodevlist[0])
else:
    outport = mido.open_output('Midi Through:Midi Through Port-0 14:0')
#inport = mido.open_input('Pure Data:Pure Data Midi-Out 1 128:1')

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
    margin = 12
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

# printsvg()
def hello(name):
    print ("Hello %s!" % name)

def printjob(kind):
    print("printing started", kind)
    jobs = [printbanner]
    i = random.randint(0,len(jobs)-1)
    jobs[i]()
    
    # p.setNewDensityAndGotoTop(12,p.pageheight,p.linefeed)
    # p.nextTop()
    # p.lf()
    print("printing stopped, sleeping 120 sec")
    time.sleep(120)
    print("ready for new job")


def imnotarobot(blah):
    global printing
    if not printing:
        #make some sound
        printing = True
        print("trying to make sound")
        msg = mido.Message('note_on', channel=0, note=41, velocity=127, time=0)
        outport.send(msg)
        time.sleep(10)
        print("stopping sound")
        msg = mido.Message('note_off', channel=0, note=41, velocity=127, time=0)
        outport.send(msg)
        # msg = mido.Message('control_change', channel=0, control=126, value=0)
        # outport.send(msg)
        printjob("from robot") ##blocking
        printing = False
        # rt = RepeatedTimer(30, imnotarobot, "World")
global printing
printing = False

# imnotarobot("blah")
# rt = RepeatedTimer(500, imnotarobot, "World") # it auto-starts, no need of rt.start()

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


# inport.callback = midiparse
# app()


printVersumBanner()



