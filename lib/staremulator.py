import svgwrite

warnings = True  ## enable to see emulation problems at stdout

basefontsize = 16 # 4.233 mm 
linefeed = 16 # setLineSpace(12)  12 matches default 16
fontproportion = 0.6 #calculated from rules measurements
# font = 'Wonky Pins'
font = 'Courier New'
lineCursorY = 0 # pixel position of the cursor, because of changing linefeed this is not simply "linefeed * cursorY"
cursorY = 0   #integer line index
cursorYoffset = 0 # used for extending pages longer than 1 page setTopAtCurrent
svgfile = "page 0"
currentdwg = ""
pagecounter = 0

def openfile(filename):
    global svgfile
    global currentdwg
    svgfile = filename
    currentdwg = svgwrite.Drawing(filename, size=("210mm","297mm"), profile='full')
    currentdwg.defs.add(currentdwg.style('svg {background-color: white;'))
    currentdwg.defs.add(currentdwg.style('.txt {white-space: pre; }'))
    # return dwg

def lf():
    #linefeed
    global cursorY
    global lineCursorY
    cursorY = cursorY + 1
    lineCursorY = lineCursorY + linefeed
    # print (cursorY)

def rlf():
    #linefeed
    global cursorY
    global lineCursorY
    cursorY = cursorY - 1
    lineCursorY = lineCursorY - linefeed
    # print (cursorY)

def closefile():
    global currentdwg
    currentdwg.save()


def printXY(string,x,y):
    global cursorY
    if (len(string) + x > 80):
        if warnings:
            print("WARNING LINE WILL WRAP ON PRINTER!!!!")
            print("CUTTING LINE TO PREVENT WRAP")
            print("Line =" , str(len(string) + x) )
        string = string[0:80-x]
    if (y > cursorY):
        # print ("emu advancing ", y - cursorY) 
        for i in range(y-cursorY):
            lf()
    if (y < cursorY):
        # print ("emu reversing ", cursorY - y) 
        for i in range(cursorY-y):
            rlf()
    if (y == cursorY):
        # print ("emu not advancing")
        pass
    svg = currentdwg.add(currentdwg.g(id="txt", class_="txt", style="font-size:"+str(basefontsize)+";font-family:"+font+";"))
    svg.add(currentdwg.text(string, insert=(fontproportion*basefontsize*x,lineCursorY)))  #  n * 7.5 >>> from linefeed units to px
    lf()

def setLineSpace(n):
    # sets the distance the paper advances or reverses in subsequent linefeeds to n/72 inch, where n is between O and 255..  ## 0.35 * 12
    global linefeed
    linefeed = n/3*4   ### n = 12 should return 16 >> which corresponds with pixel size in svg
    return linefeed

def currentTop():
    # feeds paper to top of current page
    # we probably don't need this, as we use absolute printing coordinates and use rlf/lf accordingly
    global cursorY
    cursorY = 0

def setTopAtCurrent():
    global cursorY
    global cursorYoffset 
    cursorYoffset = cursorY
    cursorY = 0

def nextTop():
    #needs to init newsvg
    global pagecounter
    pagecounter = pagecounter + 1
    openfile("page" + pagecounter + ".svg")


def unitTest():
    global currentdwg
    printXY(currentdwg,"line1", 0, 1)
    printXY(currentdwg,"line2", 0, 2)
    printXY(currentdwg,"line3", 0, 3)
    printXY(currentdwg,"line4", 0, 4)

    setTopAtCurrent()
    printXY(currentdwg,"lineA", 10, 0)
    printXY(currentdwg,"lineB", 10, 2)
    printXY(currentdwg,"lineC", 10, 3)
    printXY(currentdwg,"lineD", 10, 4)

    printXY(currentdwg,"line1", 20, 0)
    printXY(currentdwg,"line2", 20, -2)
    printXY(currentdwg,"line3", 20, 3)
    printXY(currentdwg,"line4", 20, 4)