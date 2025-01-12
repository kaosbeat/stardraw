from pythonosc.osc_server import AsyncIOOSCUDPServer
from pythonosc.dispatcher import Dispatcher
import asyncio
import lib.starDraw as sd
import lib.asciistage as ast
from lib.asciitools import strip2ascii
import time
from random import choice
from itertools import cycle
##########################
# globals
###############
state = "done"

soundstate = {
    "d1": 0.0,
    "d2": 0.0,
    "d3": 0.0,
    "d4": 0.0,
    "d5": 0.0,
    "d6": 0.0,
    "d7": 0.0,
    "d8": 0.0,
    }


##############3
###osc#########
############3

figfontlist = ["big", "banner3-D"]




def vumeter(soundstate):
    columns = ast.columns
    height = ast.lines
    multilinebuffer = ''''''
    baseline =  " D1 D2 D3 D4 D5 D6 D7 D8"        
    multilinebuffer += baseline + "\n"
    for drawcursorY in range(height-1):
        screenline =  ""
        for vu in soundstate:
            screenline += " "
            if int(soundstate[vu]*(height-2)) > drawcursorY:
                if drawcursorY > 0.8*(height-1):
                    screenline += "XX"
                elif drawcursorY > 0.6*(height-1):
                    screenline += "YY"
                else:
                    screenline += "UU"
            else:
                screenline += "  "
        multilinebuffer += screenline + "\n"

    multilinebufferlist = multilinebuffer.split("\n")
    multilinebufferlist.reverse()
    
    multilinebuffer = ''''''
    for l in multilinebufferlist:
        multilinebuffer +=  l  + '\n'
    return multilinebuffer
    

def rms(address, *args):
    buffers = ["d1","d2","d3","d4","d5","d6","d7","d8"]    # print(f"{address}: {args}")
    soundstate[buffers[args[2]]] = args[3]
    # print(soundstate)
    soundbuffer = vumeter(soundstate)
    ast.printMultilineonstage(soundbuffer,0, ast.lines)    
    pass



def statechange(address, *args):
    # print(f"{address}: {args}")
    global state
    state = args[0]
    

dispatcher = Dispatcher()
dispatcher.map("/rms", rms)


ip = "0.0.0.0"
port = 9130




async def loop():
    """main loop"""
    global i, state
    print(state)
    while True:
        # print("#waiting for data")
        await asyncio.sleep(1)
            


async def init_main():
    server = AsyncIOOSCUDPServer((ip, port), dispatcher, asyncio.get_event_loop())
    transport, protocol = await server.create_serve_endpoint()  # Create datagram endpoint and start serving
    global i
    i = 0
    await loop()  # Enter main loop of program
    transport.close()  # Clean up serve endpoint
asyncio.run(init_main())