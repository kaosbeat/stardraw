from pythonosc.osc_server import AsyncIOOSCUDPServer
from pythonosc.dispatcher import Dispatcher
import asyncio
import screens as s
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


##############3
###osc#########
############3

figfontlist = ["big", "banner3-D"]


def filter_handler(address, *args):
    print(f"{address}: {args}")
    pass

def statechange(address, *args):
    # print(f"{address}: {args}")
    global state
    state = args[0]
    

dispatcher = Dispatcher()
dispatcher.map("/filter", filter_handler)
dispatcher.map("/state", statechange)

ip = "0.0.0.0"
port = 1337



#####################################
############# signal stage ##########
#####################################

async def signal():
    
    state = "done"






###################################
##########  ear   ################
###################################
async def ear():
    ast.clearstage()
    if status == "": status  = " "
    ast.blinkFiglet(2, ast.lines-2,status, "big", 2, ast.lines-2," ","big",0.03,2)
    ast.blinkFiglet(2, ast.lines-10,name, "big", 2, ast.lines-10,"____________________________________________","big",0.01,4)
    ast.printFiglet(name,"big", 2, ast.lines-10)
    # midi_datascrollerbeat(cursor, status)
    state = "done"


##########################
### mouth ############
####################




async def mouth():
    ast.clearstage()
    state = "done"

async def loop():
    """main loop"""
    global i, state
    print(state)
    while True:
        print("#waiting for data")
        await asyncio.sleep(1)
            


async def init_main():
    server = AsyncIOOSCUDPServer((ip, port), dispatcher, asyncio.get_event_loop())
    transport, protocol = await server.create_serve_endpoint()  # Create datagram endpoint and start serving
    global i
    i = 0
    await loop()  # Enter main loop of program
    transport.close()  # Clean up serve endpoint
asyncio.run(init_main())