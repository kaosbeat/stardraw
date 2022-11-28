# To create a kiosk
# install rxvt-unicode 
# run this file in that terminal
# rxvt-unicode -name aterm-ws2 -tr  -fg yellow -bg [80]blue +sb --depth 32

########################
####  imports ##########
########################
# own libraries
# import lib.starLC20 as p
# import lib.staremulator as s
# import lib.stardisplay as d
from tracemalloc import start
import lib.starDraw as sd
import lib.tweetprint as tweet
import lib.font_anomaly as fa
import lib.recaptcha as rc
import lib.timers as tim
import lib.asciistage as ast
import faarasciiart as aa
import lib.promptqueriesfake as pq
from lib.asciitools import strip2ascii

### other imports

import random
import time
from perlin_noise import PerlinNoise
# tweetit = True


# def loopReclame():

buff = '''
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




 _     ____    ____   ___  _   _ ____  _____ ______     ___    _   _ 
| |   |  _ \  / ___| / _ \| \ | |  _ \| ____|  _ \ \   / / \  | \ | |
| |   | |_) | \___ \| | | |  \| | | | |  _| | |_) \ \ / / _ \ |  \| |
| |___|  __/   ___) | |_| | |\  | |_| | |___|  _ < \ V / ___ \| |\  |
|_____|_|     |____/ \___/|_| \_|____/|_____|_| \_\ \_/_/   \_\_| \_|
                                                                     
 ____  ____  _____ _   _ ____   ___  
|___ \| ___|| ____| | | |  _ \ / _ \ 
  __) |___ \|  _| | | | | |_) | | | |
 / __/ ___) | |___| |_| |  _ <| |_| |
|_____|____/|_____|\___/|_| \_\\___/ 

                                     



'''



buff2=  '''
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



 ____   ___  ____ _____ _____ ____  
|  _ \ / _ \/ ___|_   _| ____|  _ \ 
| |_) | | | \___ \ | | |  _| | |_) |
|  __/| |_| |___) || | | |___|  _ < 
|_|    \___/|____/ |_| |_____|_| \_\

 _  ___    _____ _   _ ____   ___  
/ |/ _ \  | ____| | | |  _ \ / _ \ 
| | | | | |  _| | | | | |_) | | | |
| | |_| | | |___| |_| |  _ <| |_| |
|_|\___/  |_____|\___/|_| \_\\___/ 


'''

buff3=  '''
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

 ____  _     ___ _____ 
|  _ \| |   / _ \_   _|
| |_) | |  | | | || |  
|  __/| |__| |_| || |  
|_|   |_____\___/ |_|  

 _  ___    _____ _   _ ____   ___  
/ |/ _ \  | ____| | | |  _ \ / _ \ 
| | | | | |  _| | | | | |_) | | | |
| | |_| | | |___| |_| |  _ <| |_| |
|_|\___/  |_____|\___/|_| \_\\___/ 


'''

while(True):
    ast.clearstage()
    ast.printMultilineonstage(buff, 0, ast.lines, lineForLine=0.1, overdrop=True )
  
    
    time.sleep(2)
    ast.clearstage()
    ast.printMultilineonstage(buff2, 0, ast.lines, lineForLine=0.1, overdrop=True )
  
    
    time.sleep(2)
    
    ast.clearstage()
    ast.printMultilineonstage(buff3, 0, ast.lines, lineForLine=0.1, overdrop=True )
  
    
    time.sleep(2)
    
    
 #   ast.blinkFiglet(10,90, "DATA_INTERSECT", "banner3-D", 10, 30, "MERCHANDISE", None, 0.6, 4)  
  #  time.sleep(3)
   # ast.blinkFiglet(10,10, "RISO_PRINT_POSTER", "epic", 10, 30, "10 EUROS", None, 1, 5)  
   # time.sleep(3)
   # ast.blinkFiglet(50,50, "LP_Sondervan", "epic", 50, 40, "25 EUROS", None, 0.6, 4)
    time.sleep(1)
    #for i in range(10):
     #   ast.blinkFiglet(10,10, "MODULAR_MOUNTAINS", "epic", 10, 30, "10 EUROS", None, 3, 1)  
      #  ast.blinkFiglet(10,10, "INLCUDES_DOWNLOAD_CODE", "epic", 10, 30, "S", None, 0.6, 4)  
