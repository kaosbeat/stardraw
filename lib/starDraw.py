import random

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
        print("vertical!")
        rc = 1000000
    else:
        rc = (y2-y1)/(x2-x1)
        print("rico = ", rc)

    if rc < 0:
        # xoff = xoff + min(x1,x2)
        print ("x1= " ,x1) 
        print ("x2= " ,x2) 
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
            line = int(x) * ' ' + char
            buffer = buffer + line + '\n'
    if y2 < y1:
        for j in range(y1-y2+1):
            if rc == 0:
                x = x1
            else:
                x = j/rc + xoff
            line = int(x) * ' ' + char
            buffer = buffer + line + '\n'
    if y1 == y2:
        print("horizontal!")
        line = ' ' * (xoff) + (abs(x2-x1)+1) * char
        buffer = buffer + line + '\n'

    print("done")
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


def square(x1,y1,x2,y2,charv,charh):
    a = line(x1,y1,x2,y1,charh)
    b = line(x1,y1,x1,y2,charv)
    c = line(x1,y2,x2,y2,charh)
    d = line(x2,y1,x2,y2,charv)
    return [a, b, c, d]