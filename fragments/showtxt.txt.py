txt1 = '''


+----------------------------------------------------+
|     I'm not on Facebook, but I have your data.     |
+----------------------------------------------------+
| You're looking at badly obfuscated scraped data.   |
| First names and their relationship status.         |
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
|  +--+                        /    \\               |
|  |  |   I'm not a robot           | recaptcha      |
|  +--+                        A    v                |
|                               \\-                  |
+----------------------------------------------------+
|  Kasper Jordaens    -   2021                       |
|  matrix printed ink on paper                       |
|  a piece of YOUR data (1500 of 533.000.000 records)|
|  my algorithms                                     |
+----------------------------------------------------+

'''


txt2 = '''


+----------------------------------------------------+
|     Starpraw printer studies                       |
+----------------------------------------------------+
| The matrix printer is an interesting device. It's  |
| a non-autonomous robot, waiting for instructions   |
| from the computer. Modern printers decide things   |
| themselves. I reverse engineered the instructions  |
| that came with the printer into an open modern     |
| printer driver so that it can be used with modern  |
| software. To test this, I made a lot of studies to |
| get the desired results. The process itself is a   |
| very important part of a creation process and is   |
| often hidden. I'm happy to show it to you here,    |
| you can also follow my processes on @kaoskode, a   |
| twitterbot that automatically posts intermediate   |
| results of a selection of my creative work.        |
+----------------------------------------------------+
 
+----------------------------------------------------+
|  Kasper Jordaens    -   2021                       |
|  matrix printed ink on paper                       |
|  printer driver and test files                     |
|  https://github.com/kaosbeat/stardraw              |
+----------------------------------------------------+

'''


txt3 = '''

+----------------------------------------------------+
|    I'm not on Facebook, but I have your data.      |
+----------------------------------------------------+
| Random names from 533 Million names and their      |
| relationship status.                               |
| The data is easy to obtain because data capitalists|
| want it that way. They share it, actually spill it,| 
| like oil in the sea where it becomes hard to clean |
| up. They don't care about the person that created  |
| the data.                                          |
| Out of the available 16 fields I chose firstname & |
| relationship status as something triggering. But   |
| This is the just tip of the iceberg. Question your |
| data and who has access to it.                     |
|                                                    |
|                                                    |
|             _______||_________||_______            |
|            /       ||         ||       \\           |
|           /        ||         ||        \\          |
|           \      //UUUUUUUUUUUUU\\\\      /          |
|          & \-oo-//               \\\\-oo-/           |
|        &        {=================}                |
|          &      | +-----+  O>  0  |                |
|             & & | |Gimme|  ^      |                |
|                 | |DATA |         |                |
|                 | +-----+  O   0  |                | 
|         /--\    |                 |                | 
|         |   ====|  ^   ^   ^   ^  |                |
|         \--/    |  U   U   U   U  |                |
|                 |                 |                |
|                 +_________________+                |
|                                                    |
|                                                    |
+----------------------------------------------------+

+----------------------------------------------------+
|  Kasper Jordaens    -   2021                       |
|  a piece of YOUR data (out of 533.000.000 records) |
|  my algorithms (15 minutes of my time & some help) |
|  CB tranceiver                                     |
|  Raspberry pi with custom software                 |
|  Matrix printer                                    |
|  Axoloti audio development board in custom case    |
|  modular synth                                     |
+----------------------------------------------------+

'''


txt4 = '''

+----------------------------------------------------+
|   Data landscapes    |                       |
+----------------------------------------------------+
| Data morphogenesis, or turning data into form, is 
| like using data as your canvas and you paintbrush. 
| algoritmically defined shapes and complex systems 
| arise from simple formulas. It can be applied to 
| both sound and images.
| 
+----------------------------------------------------+
        
+----------------------------------------------------+
|  Kasper Jordaens    -   2021                       |
|                                        |
+----------------------------------------------------+

'''


import lib.starLC20 as p

density = 12
# p.setNewDensityAndGotoTop(density, p.pageheight, p.linefeed)
# height = int(p.pageheight*12/p.linefeed)
p.printBuffer(txt4,20,15,120)
