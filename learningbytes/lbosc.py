from pythonosc.osc_server import AsyncIOOSCUDPServer
from pythonosc.dispatcher import Dispatcher
import asyncio
import lbscreens as lbs
import lib.asciistage as ast
import lib.promptqueriesfake as pq
from lib.asciitools import strip2ascii
# import db


import time
from random import choice
from itertools import cycle
##########################
# globals
###############
state = "done"
global invertedcatstates
invertedcatstates = {"word": "test", "masktype": "fill", "cyclepoint":0.5, "cyclewidth":0.2 }
bootstates = {"command":"next", "noisestep" : 0.01}
printstates = {"command":"signalline", "option": "none"}
signalstates = {"command":"next", "option": "clear", "amount" : 1}
textstates = {"command": "clear", "font": "banner3-D", "word1":"data", "word2":"intersect", "x":10, "y":30}
datastates = {"datascroller":1}
intersectstates = {"size":5, "framewait":0.05}
circlestates = {"circleradius": 10, "x" :"", "y" :"", "noisestep" : 0.01, "seed" :1337, "framewait":0.05}
bannerstates = {"command":"banner","x" :"1", "y" :"1", "noisestep" : 0.01, "seed" :1337, "framewait":0.05}
global promptwordlist, words, prewords
prewords = cycle(pq.wordContext(invertedcatstates["word"]))
prewords = cycle(["words words"])
words = prewords
promptwordlist = pq.getrandomwordlist()
# data = cycle(db.getAntwerpNamesAndData())
data = cycle([[0,0,"K",0,0,0,0,0,0,"P"],[0,0,"L",0,0,0,0,0,0,"Q"]])
##############3
###osc#########
############3

def filter_handler(address, *args):
    # print(f"{address}: {args}")
    pass

def statechange(address, *args):
    # print(f"{address}: {args}")
    global state
    state = args[0]
    
def piviz(address, *args):
    # print(f"{address}: {args}")
    global state, promptwordlist, words, prewords
    state = args[0]
    command = args[1]
    option = args[2]
    size = args[3]
    speed = args[4]
    framewait = args[5]
    amount = args[6]
    word1 = args[7]
    word2 = args[8]
    vizx = int(args[9])
    vizy = int(args[10])

    if state == "boot":
        bootstates["command"] = command
        bootstates["framewait"] = framewait    
        bootstates["noisestep"] = float(speed)

    if state == "print":
        printstates["command"] = command
        printstates["option"] = size
    if state == "signal":
        signalstates["command"] = command
        signalstates["option"] = option
        signalstates["framewait"] = framewait
        signalstates["amount"] = int(amount)
    if state == "invertedcat":
        if command == "next":
            invertedcatstates["word"] =  strip2ascii(choice(promptwordlist))
            words = cycle(pq.wordContext(invertedcatstates["word"]))
            prewords = words
        invertedcatstates["masktype"] = option
        invertedcatstates["cyclepoint"] = size
        invertedcatstates["cyclewidth"] = speed
    if state == "rtext":
        if option == "none" : option = "big"
        textstates["command"] = command
        textstates["font"] = option
        # if word1 == "x": word1 = "" # weird bug
        textstates["word1"] = word1
        if word2 == "x": word2 = ""
        textstates["word2"] = word2
    if state == "text":
        textstates["command"] = command
        if option == "none" : option = "big"
        textstates["font"] = option
        # if word1 == "x": word1 = "" # weird bug
        textstates["word1"] = word1
        if word2 == "x": word2 = ""
        textstates["word2"] = word2
        textstates["x"] = vizx
        textstates["y"] = vizy
        
    if state == "data":
        textstates["word1"] = word1
        textstates["word2"] = word2
    if state == "intersect":
        intersectstates["size"] = int(size)
        intersectstates["framewait"] = framewait
    if state == "circle":
        circlestates["circleradius"] = int(size)
        circlestates["noisestep"] = float(speed)
        circlestates["seed"] = int(amount)
        circlestates["framewait"] = framewait
    if state == "banner":
        bannerstates["command"] = command
        bannerstates["x"] = vizx
        bannerstates["y"] = vizy
        bannerstates["octaves"] = size
        bannerstates["noisestep"] = float(speed)
        bannerstates["seed"] = int(amount)
        bannerstates["noisechar"] = word1

        # bannerstates["framewait"] = framewait    


    



dispatcher = Dispatcher()
dispatcher.map("/filter", filter_handler)
dispatcher.map("/state", statechange)
dispatcher.map("/piviz", piviz)

ip = "0.0.0.0"
port = 1337


##################################
######## boot stage ############
##################################
##init##

async def boot():
    global bootstates, state
    # ast.printonstage("boot seq started", 0,1)
    if bootstates["command"] == "init":
        lbs.bootseq(bootstates["framewait"])
    elif bootstates["command"] == "keynote1":
        lbs.keynote1(bootstates["framewait"])
    elif bootstates["command"] == "keynote2":
        lbs.keynote1(bootstates["framewait"])
    elif bootstates["command"] == "coffee":
        lbs.coffee(bootstates["framewait"], bootstates["noisestep"])
    
    elif bootstates["command"] == "wait":
        ast.blinkFiglet(15,20,"downloading keynote speaker\n","big", 15,20," ",None,0.8,2)
    elif bootstates["command"] == "noise":
        ast.doNoise(2, ast.columns-2 , 1 , ast.lines-1, 0.01, 100)

    state = "done"

#####################################
############# signal stage ##########
#####################################

async def signal():
    global signalstates, state, words
    # ast.printonstage("boot seq started", 0,1)
    if signalstates["option"] == "clear":
        ast.clearstage(" ")
    if signalstates["command"] == "init":
        ast.clearstage()
    elif signalstates["command"] == "perspsq":
        lbs.perspsquaressignal(signalstates["amount"] )
    elif signalstates["command"] == "cube":
        lbs.cuber()
    elif signalstates["command"] == "lines":
        lbs.lines(signalstates["amount"] )
    elif signalstates["command"] == "wlines":
        lbs.lines(signalstates["amount"], words )
    elif signalstates["command"] == "squares":
        lbs.squares(signalstates["amount"])
    elif signalstates["command"] == "circles":
        lbs.circle()    
    state = "done"


###################################
######## inverted CAT ############
##################################
##init##



async def invertcatstage():
    global invertedcatstates, state, prewords
    # testword = "cyborg"
    word = invertedcatstates["word"]
    mask = lbs.cyclemask(word,invertedcatstates["cyclepoint"],invertedcatstates["cyclewidth"])
    if invertedcatstates["masktype"] == "none":
        mask = " "*len(word)
    buffer = lbs.invertedHorizontalCat(word, prewords, mask, invertedcatstates["masktype"] , ast.columns, ast.lines)
    ast.printMultilineonstage(buffer, 0,ast.lines)
    # ast.printonstage(str(invertedcatstates), 0, 0)
    # time.sleep(0.1)
    state = "invertcatstagedone"



####################################
############ text #################
#####################################
async def textseq():
    global textstates, state
    status = str(textstates["font"] + " " + textstates["word1"] + " " + textstates["word2"])
    if textstates["command"] == "clear":
        ast.clearstage()
    lbs.text(textstates["x"], textstates["y"],textstates["font"],textstates["word1"],textstates["word2"])
    # ast.printonstage(status, 0,0)
    state = "done"

async def rtextseq():
    global textstates, state
    status = str(textstates["font"] + " " + textstates["word1"] + " " + textstates["word2"])
    if textstates["command"] == "clear":
        ast.clearstage()
    lbs.rtext(textstates["font"],textstates["word1"],textstates["word2"])
    # ast.printonstage(status, 0,0)
    state = "done"

###################################
##########  data   ################
###################################
async def dataseq():
    global datastates,state
    ast.clearstage()
    dpoint = next(data)
    status = strip2ascii(dpoint[9])
    if status == "": status  = " "
    name = strip2ascii(dpoint[2])
    ast.blinkFiglet(2, ast.lines-2,status, "big", 2, ast.lines-2," ","big",0.03,2)
    ast.blinkFiglet(2, ast.lines-10,name, "big", 2, ast.lines-10,"____________________________________________","big",0.01,4)
    ast.printFiglet(name,"big", 2, ast.lines-10)
    # midi_datascrollerbeat(cursor, status)
    state = "done"

async def interseq():
    global datastates,state
    ast.clearstage()

    lbs.intersect(intersectstates["size"],intersectstates["framewait"])
    state = "done"

async def circle():
    global datastates,state
    # ast.clearstage()
    radius = int(min(ast.columns/2, ast.lines/4))
    lbs.circle(radius, "mid", "mid" , circlestates["noisestep"],circlestates["seed"])
    # time.sleep(circlestates["framewait"])
    
    state = "done"


##########################
### banner ############
####################

async def banner():
    global datastates,state
    # ast.clearstage()
    if bannerstates["command"] == "banner":
        lbs.banner("banner", bannerstates["x"], ast.lines - bannerstates["y"], bannerstates["noisestep"],bannerstates["seed"], bannerstates["noisechar"],bannerstates["octaves"])
    elif bannerstates["command"] == "lbf1":
        lbs.banner("lbf1", bannerstates["x"], ast.lines - bannerstates["y"], bannerstates["noisestep"],bannerstates["seed"], bannerstates["noisechar"],bannerstates["octaves"])
    elif bannerstates["command"] == "lbf2":        
        lbs.banner("lbf1", bannerstates["x"], ast.lines - bannerstates["y"], bannerstates["noisestep"],bannerstates["seed"], bannerstates["noisechar"],bannerstates["octaves"])
    elif bannerstates["command"] == "lbf3":
        lbs.banner("lbf3", bannerstates["x"], ast.lines - bannerstates["y"], bannerstates["noisestep"],bannerstates["seed"], bannerstates["noisechar"],bannerstates["octaves"])
    elif bannerstates["command"] == "logo":
        lbs.banner("logo", bannerstates["x"], ast.lines - bannerstates["y"], bannerstates["noisestep"],bannerstates["seed"], bannerstates["noisechar"],bannerstates["octaves"])
    
    state = "done"
    



async def loop():
    """main loop"""
    global i, state
    print(state)
    while True:
        if state == "done":
            # print(f"Loop {i}")
            i+=1
            await asyncio.sleep(0.01)
        elif state == "boot":
            await boot()
        elif state == "signal":
            await signal()
        elif state == "invertedcat":
            await invertcatstage()
        elif state == "text":
            await textseq()
        elif state == "rtext":
            await rtextseq()
        elif state == "data":
            await dataseq()
        elif state == "intersect":
            await interseq() 
        elif state == "circle":
            await circle()
        elif state == "banner":
            await banner()
        else:
            # print(f"WrongLoop {i}")
            await asyncio.sleep(0.01)
            


async def init_main():
    server = AsyncIOOSCUDPServer((ip, port), dispatcher, asyncio.get_event_loop())
    transport, protocol = await server.create_serve_endpoint()  # Create datagram endpoint and start serving
    global i
    i = 0
    await loop()  # Enter main loop of program
    transport.close()  # Clean up serve endpoint
asyncio.run(init_main())