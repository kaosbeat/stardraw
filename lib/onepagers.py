import random
#!/usr/bin/python3

import starLC20 as p
import staremulator as s
import random
from perlin_noise import PerlinNoise
import datetime
import starDraw as sd
# import tweetprint as tweet
# import font_anomaly as fa
import recaptcha as rc

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

    p.printBuffer(" ",0,height,height)
    p.lf()



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


def captcha():
    p.setNewDensityAndGotoTop(10, p.pageheight, p.linefeed)
    height = int(p.pageheight*12/p.linefeed)
    
    p.printBuffer(notarobot,12,15,height)
    p.printBuffer(phone,12,35,height)
    p.printBuffer(confirm,12,15,height)


# captcha()



