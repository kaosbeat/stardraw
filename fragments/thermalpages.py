import random
#!/usr/bin/python3

import lib.starLC20 as p
import lib.staremulator as s
import random
from perlin_noise import PerlinNoise
import datetime
import lib.starDraw as sd
# import tweetprint as tweet
# import font_anomaly as fahttps://github.com/dmarx/deforum-stable-diffusion
import lib.recaptcha as rc
import lib.font_anomaly as fa
import lib.font_anomaly_phone as fap
from pyfiglet import Figlet

def signstring(title):
    string = '{0:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())
    string = "kaotec []<> " + title + " " + string
    return string

## all functions bvelow should print a onepager

#####################################################
#####################################################
'''
            _               
 
                            
'''
#####################################################
#####################################################


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
