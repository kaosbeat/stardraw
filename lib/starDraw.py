import random
import math

def line(x1,y1,x2,y2, char):
    #draws line from.(x1,y1) to (x2,y2)  both points included using char
    #if char == 'auto' selects /\|- according to orientation 
    #if char is 'random' pick a random char!
    buffer = ''

    if x2 < x1:
        xoff = x2
    else: 
        xoff = x1
    if y2 < y1:
        yoff = y2
    else: 
        yoff = y1
    buffer = yoff * '\n'
    if (x2-x1 == 0):
        #vertical div by zero
        # print("vertical!")
        rc = 1000000
    else:
        rc = (y2-y1)/(x2-x1)
        # print("rico = ", rc)

    if rc < 0:
        # xoff = xoff + min(x1,x2)
        # print ("x1= " ,x1) 
        # print ("x2= " ,x2) 
        xoff = xoff + abs(x2-x1)

    if char == 'auto':
        if -4 < rc <= -0.25:
            char = "/"
        if -0.25 < rc <= 0.25:
            char = '-'
        if 0.25 < rc <= 4:
            char = '\\'
        if abs(rc) > 4:
            char = '|'
    
    if char == 'random':
        chars = ['!','#','%','^', '&', '}', "o", ">", "~"]
        char = chars[random.randint(len(chars))-1]

    if y2 > y1:
        for j in range(y2-y1+1):
            if rc == 0:
                x = x1
            else: 
                x = j/rc + xoff
            if x >= 0:
                line = int(x) * ' ' + char
            else:
                line = ''
            buffer = buffer + line + '\n'
    if y2 < y1:
        for j in range(y1-y2+1):
            if rc == 0:
                x = x1
            else:
                x = j/rc + xoff
            if x >= 0:
                line = int(x) * ' ' + char
            else:
                line = ''
            buffer = buffer + line + '\n'
    if y1 == y2:
        # print("horizontal!")
        if x1 < 1:
            x1 = 1
        if x2 < 1:
            x2 = 1
        line = ' ' * (xoff) + (abs(x2-x1)+1) * char
        buffer = buffer + line + '\n'

    # print("done")
    return buffer


# k = line(16,2, 10, 2, 'a')
# print(k)

def brokenline(x1,y1,x2,y2, char):
    #draws line from...to using char
    buffer = ''
    if (x2-x1 == 0):
        #vertical div by zero
        print("vertical!")
        rc = 0
        xoff = x1
    else:
        rc = (y2-y1)/(x2-x1)
        print("rico = ", rc)
    if x2 < x1 and rc < 0:
        xoff = x2
    if x2 < x1 and rc > 0: 
        xoff = x1
    if x2 > x1 and rc < 0:
        xoff = x1
    if x2 > x1 and rc > 0: 
        xoff = x2
    
    if y2 < y1:
        yoff = y2
    else: 
        yoff = y1
    buffer = yoff * '\n'


    if y2 > y1:
        for j in range(y2-y1):
            if rc == 0:
                x = x1
            else: 
                x = j/rc + xoff
            line = int(x) * ' ' + char
            buffer = buffer + line + '\n'
    if y2 < y1:
        for j in range(y1-y2):
            if rc == 0:
                x = x1
            else:
                x = j/rc + xoff
            line = int(x) * ' ' + char
            buffer = buffer + line + '\n'
    if y1 == y2:
        line = ' ' * xoff + abs(x2-x1) * char
        buffer = buffer + line + '\n'

    print("done")
    return buffer


def square(x1,y1,x2,y2,charh,charv):
    # returns a bufferlist of lines, print using
    a = line(x1,y1,x2,y1,charh)
    b = line(x1,y1,x1,y2,charv)
    c = line(x1,y2,x2,y2,charh)
    d = line(x2,y1,x2,y2,charv)
    return [a, b, c, d]

# def filledsquare(size, angle, char):
#     # 0 < angle < size/2 
#     buffer  = ""
#     for x in range(size+1):
#         if x < size/2:
#             line = " " * int(size/2-x) + char*int((x*4)/2+1)
#         elif x == size/2:
#             line = char*(size+1)
#         else:
#             line = " " * int(x-size/2) + char*int(((size-x)*4)/2+1)
#         buffer = buffer + line + "\n"
#     print(buffer)
#     return buffer

def building(w,h):
    vert = [["[", "]"], ["I"], ["|"],["!"],["(",")"], ["/","\\"],[":"]]
    wall=["#","o","H","U",".","O","="," ","±","+","-"]
    roof=["_", "=", "^","~"]
    buffer = []
    v = vert[random.randint(0,len(vert)-1)]
    wl = wall[random.randint(0,len(wall)-1)]
    r = roof[random.randint(0,len(roof)-1)]
    for i in range(h+1):
        line = ""
        for j in range(w+1):
            if i > 0:
                if (j == 0): 
                    v = v[0]
                    line = line + v
                elif (j == w):
                    if (len(v)==2):
                        v = v[1]
                    else:
                        v = v[0]
                    line = line + v
                else:
                    line = line + wl
            if i == 0:
                line = line + r                
        buffer.append(line)
    return buffer


    
def filledsquare(size, angle, char):
    # 0 < angle < size/2 
    buffer  = ""
    step = (size/2)/angle
    pre = (size/2) - angle
    for x in range(size+1):
        if x < size/2:
            x+1
            line = " " * int(pre - x*step) + char*int((x*4)/2+1)
        elif x == size/2:
            line = char*(size+1)
        else:
            line = " " * int(x-size/2 + angle * (x-size/2)/2 ) + char*int(((size-x)*4)/2+1)
        buffer = buffer + line + "\n"
    print(buffer)
    return buffer


# filledsquare(10,2,"d")

def parallelogram(height, dirchange, width, char):
    # parallelogram is (int(width/dirchange)+height high and width wide)
    buffer = ""
    h = height
    a = dirchange
    b = width
    c = char
    line =""
    if a == 0:
        r = h
        a = width
    else:
        r = int(b/a)+h+1
    for y in range(r):
        # print("y =", y)
        if (y > h):
            line = " "*a + line
        elif len(line) < b:
            line = line + a*c
        line = line[:b-1]
        if not line.isspace():
            buffer = buffer + line + "\n"
    return buffer

def dimensions(buffer):
    width = len(max(buffer.splitlines(), key = len))
    height = len(buffer.splitlines())
    return width, height

def padBuffer(buffer, xpad,ypad,Xpad, Ypad ):
    #pad multiline buffer
    print("padding buffer")
    #widest bufferline?
    maxlength = len(max(buffer.splitlines(), key = len))
    print(maxlength)
    buffer1 = ""
    for y in range(ypad):
        line = " "*(xpad+maxlength+Xpad)  +"\n"
        buffer1 = buffer1 + line
    for i,l in enumerate(buffer.splitlines()):
        l = l.ljust(maxlength, ' ')
        line = xpad*" " + l + Xpad*" " + "\n"
        buffer1 = buffer1 + line
    for y in range(Ypad):
        line = " "*(xpad+maxlength+Xpad) + "\n"
        buffer1 = buffer1 + line
    return buffer1


def mergeBuffers(buffer1,buffer2,xpos):
    # merge 2 buffers leaving buffer1 in front until xpos
    # pad until same height and width using padBuffer
    # buffers should have equal width/height
    print(dimensions(buffer1))
    print(dimensions(buffer2))
    
    buffer1 = buffer1.splitlines()
    buffer2 = buffer2.splitlines()
    buffer = ""
    for y in range(len(buffer1)):
        line = ""
        for x in range(len(buffer1[0])):
            if x < xpos:
                c = buffer1[y][x]
                if (c != " "):
                    c = buffer1[y][x]
                else:
                    c = buffer2[y][x]
            else:
                c = buffer2[y][x]
                if (c != " "):
                    c = buffer2[y][x]
                else:
                    c = buffer1[y][x]
            line = line + c
        print (line)
        buffer = buffer + line + "\n"
    return buffer


    for i,l in enumerate(buffer2):
        if l.isspace:
            buffer[i] = buffer1[i]
        else: 
            test = 1