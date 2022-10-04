from pythonosc.osc_server import AsyncIOOSCUDPServer
from pythonosc.dispatcher import Dispatcher
import asyncio
import faarscreens as fs
import lib.asciistage as ast
import lib.promptqueries as pq
from lib.asciitools import strip2ascii


import time
from random import choice
from itertools import cycle
##########################
# globals
###############
state = "done"
global invertedcatstates
invertedcatstates = {"word": "test", "masktype": "fill", "cyclepoint":0.5, "cyclewidth":0.2 }
bootstates = {"command":"next"}
signalstates = {"command":"next"}
global promptwordlist, words, prewords
prewords = cycle(pq.wordContext(invertedcatstates["word"]))
words = prewords
promptwordlist = pq.getrandomwordlist()


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
    width = args[4]
    if state == "boot":
        bootstates["command"] = command
        bootstates["framewait"] = size    
    if state == "signal":
        signalstates["command"] = command
        signalstates["option"] = option
        signalstates["framewait"] = size
        signalstates["amount"] = int(width)
    if state == "invertedcat":
        if command == "next":
            invertedcatstates["word"] =  strip2ascii(choice(promptwordlist))
            words = cycle(pq.wordContext(invertedcatstates["word"]))
            prewords = words
        invertedcatstates["masktype"] = option
        invertedcatstates["cyclepoint"] = size
        invertedcatstates["cyclewidth"] = width



dispatcher = Dispatcher()
dispatcher.map("/filter", filter_handler)
dispatcher.map("/state", statechange)
dispatcher.map("/piviz", piviz)

ip = "127.0.0.1"
port = 1337


##################################
######## boot stage ############
##################################
##init##

async def boot():
    global bootstates, state
    # ast.printonstage("boot seq started", 0,1)
    if bootstates["command"] == "init":

        fs.bootseq(bootstates["framewait"])
    elif bootstates["command"] == "wait":
        ast.blinkFiglet(15,20,"waiting \n for signal","big", 15,20," ",None,0.8,2)
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
        fs.perspsquaressignal(1)
    elif signalstates["command"] == "cube":
        fs.cuber()
    elif signalstates["command"] == "lines":
        fs.lines(signalstates["amount"] )
    elif signalstates["command"] == "wlines":
        fs.lines(signalstates["amount"], words )
    elif signalstates["command"] == "squares":
        fs.squares(signalstates["amount"])
    state = "done"


###################################
######## inverted CAT ############
##################################
##init##



async def invertcatstage():
    global invertedcatstates, state, prewords
    # testword = "cyborg"
    word = invertedcatstates["word"]
    mask = fs.cyclemask(word,invertedcatstates["cyclepoint"],invertedcatstates["cyclewidth"])
    if invertedcatstates["masktype"] == "none":
        mask = " "*len(word)
    buffer = fs.invertedHorizontalCat(word, prewords, mask, invertedcatstates["masktype"] , ast.columns, ast.lines)
    ast.printMultilineonstage(buffer, 0,ast.lines)
    # ast.printonstage(str(invertedcatstates), 0, 0)
    # time.sleep(0.1)
    state = "invertcatstagedone"








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