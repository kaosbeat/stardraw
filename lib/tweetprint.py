import sys
import tweepy
from lib.tweetkeys import *
from wand.image import Image
import platform
import os
## for second version, because problems with Wand on OSX
#from svglib.svglib import svg2rlg
#from reportlab.graphics import renderPM
import subprocess               # May want to use subprocess32 instead


print("invoking TWEEEEEETING")
print(platform.system())
# ## get ourselves the image we need (convert svg to jpg)
# with Image(filename=sys.argv[2]) as img:
#     img.format = 'jpeg'
#     img.save(filename='out.jpg')


##### using wand on OSX renders erroneously, 

# def convertSVGtoTweet(svg, tweettext):
#     with Image(filename=svg) as img:
#         img.format = 'jpeg'
#         img.save(filename='tweet.jpg')
#         # authentication 
#         auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
#         auth.set_access_token(access_token, access_token_secret) 
#         api = tweepy.API(auth) 
#         tweet = tweettext
#         image_path = "tweet.jpg" # jpg created above
#         print(image_path, tweet)
#         # to attach the medicd /Ap  a file 
#         #status = 
#         api.update_with_media(image_path, tweet)  
#         # api.update_status(status = tweet) 




def convertSVGtoTweet(svg, tweettext):
    print(svg)
    pltfrm = platform.system()
    if (plftrm == 'Darwin'):
        cmd_list = [ '/Applications/Inkscape.app/Contents/MacOS/inkscape','--export-filename=tweet.png', svg ]
    else:
        cmd_list = [ '/usr/bin/inkscape','--export-filename=tweet.png', svg ]
    p = subprocess.Popen( cmd_list, stdout=subprocess.PIPE, stderr=subprocess.PIPE )
    out, err = p.communicate()
    if p.returncode:
        raise Exception( 'Inkscape error: ' + (err or '?')  )
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
    auth.set_access_token(access_token, access_token_secret) 
    api = tweepy.API(auth) 
    tweet = tweettext
    image_path = "tweet.png" # png created above
    print(image_path, tweet)
    # to attach the media file 
    #status = 
    api.update_with_media(image_path, tweet)  
    # api.update_status(status = tweet) 
