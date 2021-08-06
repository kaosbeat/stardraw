import sys
import tweepy
from lib.tweetkeys import *
from wand.image import Image



print("invoking TWEEEEEETING")

# ## get ourselves the image we need (convert svg to jpg)
# with Image(filename=sys.argv[2]) as img:
#     img.format = 'jpeg'
#     img.save(filename='out.jpg')

def convertSVGtoTweet(svg, tweettext):
    with Image(filename=svg) as img:
        img.format = 'jpeg'
        img.save(filename='tweet.jpg')
        # authentication 
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
        auth.set_access_token(access_token, access_token_secret) 
        api = tweepy.API(auth) 
        tweet = tweettext
        image_path = "tweet.jpg" # jpg created above
        print(image_path, tweet)
        # to attach the media file 
        #status = 
        api.update_with_media(image_path, tweet)  
        # api.update_status(status = tweet) 