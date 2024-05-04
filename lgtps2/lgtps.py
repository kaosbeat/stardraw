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
import argparse




state = "done" 
text = "lets get this party started"
ip = "0.0.0.0"
# ip = "localhost"


parser = argparse.ArgumentParser(description='oneservewr per screen')
parser.add_argument('oscport', type=int, nargs=1, action="store",
                    help='oscport to send info to')
args = parser.parse_args()
oscport = args.oscport[0]




def lgtps(address, *args):
    global state, text
    print(f"{address}: {args}")
    state = args[0]
    # command = args[1]
    text = args[1]
    # print(state)


mouthframes = cycle((aa.mouth, aa.mouth1,aa.mouth2, aa.mouth3, aa.mouth4, aa.mouth5, aa.mouth6))

def multilinemouth(text, frame):
    licycle = cycle(list(text))
    multilinebuffer = """"""
    for c in frame:
        # char =
        if (c == " " or c == "\n"):
            char = c
            multilinebuffer = multilinebuffer + char
        else:
            # char = "x"
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
    global i, state, text
    print(state)
    while True:
        if state == "done":
            # print(f"Loop {i}")
            i+=1
            await asyncio.sleep(0.01)
        elif state == "lips":
            ast.clearstage()
            ast.printMultilineonstage( multilinemouth(text, next(mouthframes)), 0, 20, center=True)
            await asyncio.sleep(0.05)
        elif state == "shut":
            ast.clearstage()
            ast.printMultilineonstage( multilinemouth(text, aa.mouth), 0, 20, center=True)
            await asyncio.sleep(0.05)    
        # elif state == "signal":
        #     await signal()
        else:
            # print(f"WrongLoop {i}")
            await asyncio.sleep(0.01)

dispatcher = Dispatcher()

dispatcher.map("/lgtps", lgtps)


async def init_main():
    print("starting OSC")
    server = AsyncIOOSCUDPServer((ip, oscport), dispatcher, asyncio.get_event_loop())
    transport, protocol = await server.create_serve_endpoint()  # Create datagram endpoint and start serving
    global i
    i = 0
    await loop()  # Enter main loop of program
    transport.close()  # Clean up serve endpoint
asyncio.run(init_main())