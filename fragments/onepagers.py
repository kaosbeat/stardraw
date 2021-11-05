import random
#!/usr/bin/python3

import lib.starLC20 as p
import lib.staremulator as s
import random
from perlin_noise import PerlinNoise
import datetime
import lib.starDraw as sd
# import tweetprint as tweet
# import font_anomaly as fa
import lib.recaptcha as rc
import lib.font_anomaly as fa
import lib.font_anomaly_phone as fap
from pyfiglet import Figlet


## all functions bvelow should print a onepager

#####################################################
#####################################################
'''
            _               
           | |              
  ___ _   _| |__   ___ _ __ 
 / __| | | | '_ \ / _ \ '__|
| (__| |_| | |_) |  __/ |   
 \___|\__,_|_.__/ \___|_|   
                            
'''
#####################################################
#####################################################



def cuber():
    # prints a full page when p.pageheight = 68
    p.setNewDensityAndGotoTop(7, p.pageheight, p.linefeed)
    height = int(p.pageheight*12/p.linefeed)
    print(height)
    charset1 = ["+","\\", "/", "|", ">", "<", ":" ]
    charset2 = ["Y","#", "%", "&", "^", "!", "}" ]
    charset3 = [")","`", "'", ".", "@", "*", "{" ]

    recaptchatitle = rc.recaptcha[1]['words'][random.randint(0,len(rc.recaptcha[1]['words'])-1)]
    f = Figlet(font='standard')
    # print (f.renderText('FACEBOOK SUCKS'))
    buffer = f.renderText(recaptchatitle)
    p.printBuffer(buffer,2,1,height)

    for c in range(5):
        w,h,d = random.randint(3,25), random.randint(3,25), random.randint(3,25)
        x,y = random.randint(0,45),random.randint(15,55)
        buffer = sd.cube(w,h,d,charset1[random.randint(0,len(charset1)-1)],charset2[random.randint(0,len(charset2)-1)],charset3[random.randint(0,len(charset3)-1)])
        p.printBuffer(buffer,x,y,height)

    p.printBuffer("_",0,height,height)
    p.lf()
    p.setTopAtCurrent()
    
####
    
def printbanner():
    rev = True
    mirror = False
    relationshipstatusses = [" In a relationship",  " It\'s complicated", " Divorced", " Engaged", " Widowed", " Single", " Married", ""] 
    zone = random.randint(0,6)
    rs = relationshipstatusses[zone]
    fap.getnewList(zone)
    
    words = rs
    # words = "tE"
    print(rs)
    s.svgfile = 'namebanner.svg'
    # # words = "No, I have no Facebook!"
    # wordlist=["your data", "data communism", "data capitalism", "algorithmic happiness"]
    # words = "data communism"
    if rev:
        words = words[::-1]
    print(words)
    pages = len(words)
    s.openmultipagefile(s.svgfile,pages)
    density = 7
    p.setNewDensityAndGotoTop(density, p.pageheight, p.linefeed)
    s.setNewDensityAndGotoTop(density, p.pageheight, p.linefeed)
    height = int(p.pageheight*12/p.linefeed)
    totalheight = height*pages
    x = 5
    y = 7
    size = int(p.columns/(x+1))
    margin = int((p.columns - (x*size)) / x)
    for i,l in enumerate(words):
        buffer = fap.letter2page(l, (x,y), margin, True)
        if rev:
            revbuffer = ""
            for line in reversed(buffer.splitlines()):
                if mirror:
                    line = line[::-1]
                revbuffer = revbuffer + line + "\n"
            buffer = revbuffer
        p.printBuffer(buffer,0,(height*i)+15,totalheight)
        s.printBuffer(buffer,0,(height*i)+15,totalheight)

    signature = signstring("anomaly squares")
    p.printXY(signature, 80-len(signature), totalheight-int(2*12/p.linefeed))
    s.printXY(signature, 80-len(signature), totalheight-int(2*12/p.linefeed))
    s.closefile()




#############################################
#############################################
notarobot = '''
+------------------------------------------------+
|                               /->              |
|  +--+                        /    \\            |
|  |  |   I'm not a robot           | recaptcha  |
|  +--+                        A    v            |
|                               \\-               |
+------------------------------------------------+
'''

confirm = '''

       /
    \\ /
     V   


'''

phone = '''
       _______||_________||_______
      /       ||         ||       \\
     /        ||         ||        \\
     \      //UUUUUUUUUUUUU\\\\      /
    & \-oo-//               \\\\-oo-/
  &        {=================} 
    &      | +-----+  O>  0  |
       & & | |Hello|  ^      |
           | +-----+  O   0 <----------- PRESS THE RED BUTTON
   /--\    |                 |           TO CONFIRM HUMAN STATUS
   |   ====|  ^   ^   ^   ^  |
   \--/    |  U   U   U   U  |
           |                 |
           +_________________+
'''

def signstring(title):
    string = '{0:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())
    string = "kaotec []<> " + title + " " + string
    return string

def captcha():
    p.setNewDensityAndGotoTop(10, p.pageheight, p.linefeed)
    height = int(p.pageheight*12/p.linefeed)
    
    p.printBuffer(notarobot,12,15,height)
    p.printBuffer(phone,12,35,height)
    p.printBuffer(confirm,12,15,height)


# captcha()






txt1 = '''


+----------------------------------------------------+
|     I'm not on Facebook, but I have your data.     |
+----------------------------------------------------+
| You're looking at badly obfuscated scraped data.   |
| Firstnames and their relationship status.          |
| Easy to obtain, because data capitalists want it   |
| that way. They share it, actually spill it, like   |
| oil in the sea where it becomes hard to clean up.  |
| They don't care about the person that created and  |
| strangely enough is created by the same data.      |
| Out of the available 16 fields I chose firstname & |
| relationship status as something triggering. But   |
| This is the just tip of the iceberg. Question your |
| data and who has access to it.                     |
+----------------------------------------------------+
|                               /->                  |
|  +--+                        /    \\                |
|  |  |   I'm not a robot           | recaptcha      |
|  +--+                        A    v                |
|                               \\-                   |
+----------------------------------------------------+
|  Kasper Jordaens    -   2021                       |
|  matrix printed ink on paper                       |
|  a piece of YOUR data (1500 of 533.000.000 records)|
|  my algorithms                                     |
+----------------------------------------------------+

'''

def printtxt(txt):
    s.svgfile = 'txt.svg'
    s.openfile(s.svgfile)
    s.setNewDensityAndGotoTop(12, p.pageheight, p.linefeed)
    p.setNewDensityAndGotoTop(12, p.pageheight, p.linefeed)
    height = int(p.pageheight*12/p.linefeed)
    p.printBuffer(txt,12,15,height)
    s.printBuffer(txt,12,15,height)
    s.closefile()

# printtxt(txt1)