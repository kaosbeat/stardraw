#!/usr/bin/python3

'''
generate layers of interference patterns ready for A3 printing
based on stardraw/examples/interferencepatterns.svg
'''



# from numpy import convolve  
import lib.starLC20 as p
import lib.staremulator as s
import random
from perlin_noise import PerlinNoise
import datetime
import lib.starDraw as sd
from lib.asciitools import sign, signstring
import lib.font_anomaly as fa
import lib.recaptcha as rc
from pyfiglet import Figlet, figlet_format

s.font = 'BPdotsUnicaseSquare'

separateLayers = False



def interferencepatterns():
    # globals
    columns = 80
    height = 69
    layers = ["V", "A","-", "I"]
    colors = ["red", "blue", "black", "yellow", "green"]
    #layers
    layer = 0
    s.fontcolor=colors[layer]
    s.svgfile = 'interferencepatterns'+str(layer)+'.svg'
    s.openfile(s.svgfile)
    buffer = ""
    size = height
    for x in range(size+1):
        line = (size - x)*layers[layer]
        # print(line)
        buffer = buffer + line + "\n"
    s.printBuffer(buffer,0,1,height)
    p.printBuffer(buffer,0,1,height)
    layer+=1
    s.fontcolor=colors[layer]
    if separateLayers:
        s.closefile()
        s.svgfile = 'interferencepatterns'+str(layer)+'.svg'
        s.openfile(s.svgfile)
    buffer = ""
    for x in range(size+1):
        line = x*layers[layer]
        # print(line)
        buffer = buffer + line + "\n"
    s.printBuffer(buffer,0,1,height)
    p.printBuffer(buffer,0,1,height)
    layer+=1    
    s.fontcolor=colors[layer]
    if separateLayers:
        s.closefile()
        s.svgfile = 'interferencepatterns'+str(layer)+'.svg'
        s.openfile(s.svgfile)
    buffer = ""
    size = int(height/2)
    for x in range(size):
        line = (size - x)*layers[layer]
        # print(line)
        buffer = buffer + line + "\n"
    s.printBuffer(buffer,0,1,height)
    p.printBuffer(buffer,0,1,height)
    layer+=1    
    s.fontcolor=colors[layer]
    if separateLayers:
        s.closefile()
        s.svgfile = 'interferencepatterns'+str(layer)+'.svg'
        s.openfile(s.svgfile)
    buffer = ""
    for x in range(size+1):
        line = x*layers[layer]
        # print(line)
        buffer = buffer + line + "\n"
    s.printBuffer(buffer,0,int(height/2),height)
    p.printBuffer(buffer,0,int(height/2),height)
    s.printBuffer(buffer,0,1,height)
    p.printBuffer(buffer,0,1,height)
    layer+=1    
    s.fontcolor=colors[layer]
    if separateLayers:
        s.closefile()
        s.svgfile = 'interferencepatterns'+str(layer)+'.svg'
        s.openfile(s.svgfile)
    signature = signstring("interference study")
    p.printXY(signature, 80-len(signature), int(height))
    s.printXY(signature, 80-len(signature), int(height))
    s.closefile()

    # print (buffer)
    
    
interferencepatterns()
 