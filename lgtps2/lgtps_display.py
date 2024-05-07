

from pythonosc.osc_server import AsyncIOOSCUDPServer
from pythonosc.dispatcher import Dispatcher
import asyncio
import screens as s
import lib.asciistage as ast
import lib.promptqueriesfake as pq
from lib.asciitools import strip2ascii
import asciiart as aa
import time
# import db
import re
from itertools import cycle




state = "lips" 
ip = "0.0.0.0"
port = 1337

def lgtps(address, *args):
    global state
    # print(f"{address}: {args}")
    state = args[0]
    command = args[1]
    text = args[2]
    # print(state)


mouthframes = cycle((aa.mouth, aa.mouth1,aa.mouth2, aa.mouth3, aa.mouth4, aa.mouth5, aa.mouth6))

def multilinemouth(text):
    licycle = cycle(list(text))
    multilinebuffer = """"""
    for c in next(mouthframes):
        # char =
        if (c == " " or c == "\n"):
            char = c
            multilinebuffer = multilinebuffer + char
        else:
            char = "x"
            char = next(licycle)
            multilinebuffer = multilinebuffer + char
    # print(multilinebuffer)
    return multilinebuffer



# multilinemouth("This is supposed to be somewhat readable text", 0,0)

async def boot():
    global bootstates, state
    # ast.printonstage("boot seq started", 0,1)
    if bootstates["command"] == "init":
        s.bootseq(bootstates["framewait"])
    elif bootstates["command"] == "noise":
        ast.doNoise(2, ast.columns-2 , 1 , ast.lines-1, 0.01, 100)
    state = "done"



async def lips():
    testword = "sdfghjk"
    while(True):
        ast.printMultilineonstage(aa.logo1,0, 0, center=True)
        

async def loop():
    """main loop"""
    global i, state
    print(state)
    while True:
        if state == "done":
            # print(f"Loop {i}")
            i+=1
            await asyncio.sleep(0.01)
        elif state == "lips":
            ast.clearstage()
            repeater = 0
            while repeater < 20:
                ast.printMultilineonstage( multilinemouth("Lets Get This Party Started"), 0, 20, center=True)
                repeater += 1
                await asyncio.sleep(0.05)
            repeater = 0
            while repeater < 2:
                ast.clearstage()
                ast.printFigletAtRandomLoc("Let's", font="big")
                await asyncio.sleep(1)
                ast.clearstage()
                ast.printFigletAtRandomLoc("Get", font="big")
                await asyncio.sleep(1)
                ast.clearstage()       
                ast.printFigletAtRandomLoc("This", font="big")
                await asyncio.sleep(1)
                ast.clearstage()
                ast.printFigletAtRandomLoc("Party", font="big")
                await asyncio.sleep(1)
                ast.clearstage()
                ast.printFigletAtRandomLoc("Started", font="big")
                await asyncio.sleep(1)
                ast.clearstage()
                repeater += 1
            
        # elif state == "signal":
        #     await signal()
        else:
            # print(f"WrongLoop {i}")
            await asyncio.sleep(0.01)

dispatcher = Dispatcher()

dispatcher.map("/lgtps", lgtps)


async def init_main():
    server = AsyncIOOSCUDPServer((ip, port), dispatcher, asyncio.get_event_loop())
    transport, protocol = await server.create_serve_endpoint()  # Create datagram endpoint and start serving
    global i
    i = 0
    await loop()  # Enter main loop of program
    transport.close()  # Clean up serve endpoint
asyncio.run(init_main())
