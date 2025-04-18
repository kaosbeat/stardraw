import datetime

def strip2ascii(str):
    if str.isascii() == False:
        asciistring = ""
        for c in str:
            if ord(c) < 128:
                asciistring+=c
            else:
                asciistring+="X"
    else:
        asciistring = str 
    return asciistring   

def sign(title, y):
    s.setLineSpace(12)
    p.setLineSpace(12)
    string = '{0:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())
    string = "kaotec []<> " + title + " " + string
    s.printXY(string, s.columns - len(string), y) 


def signstring(title):
    string = '{0:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())
    string = "kaotec []<> " + title + " " + string
    return string
