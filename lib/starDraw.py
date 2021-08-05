def line(x1,y1,x2,y2, char):
    #draws line from...to using char
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
        rc = 0
    else:
        rc = (y2-y1)/(x2-x1)
        print("rico = ", rc)

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


# k = line(16,2, 10, 2, 'a')
# print(k)



