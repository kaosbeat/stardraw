# imagegen

from ldm.generate import Generate
from lib.obliquestartegies import obstrat
from lib.tweetprint import tweetimg

# textgen link to home/kaos/Documents/AI/InvokeAI/ldm/
from transformers import pipeline
generator = pipeline('text-generation', model='EleutherAI/gpt-neo-1.3B')
out = generator("with this transformer, getting text is easy", do_sample=True, min_length=50)
print(out)

import random
random.shuffle(obstrat)


# Create an object with default values
gr = Generate('stable-diffusion-1.4')

# do the slow model initialization
gr.load_model()
outputs = gr.prompt2png(prompt="a musician in a music studio, 1980s science fiction movie, cinematic", outdir="./outputs/",width=1280, height=720)
tweet = "obliquestrategies in stable diffusion, run 7, outputimag goes to nextinit: \n a musician in a music studio, 1980s science fiction movie, cinematic"
tweetimg(outputs[0][0], tweet)


lastimg = outputs[0][0]

for i,strat in enumerate(obstrat):
    outputs = gr.prompt2png(prompt="((("+strat+"))), "+"[letters, words, text]"+","+"1980s science fiction movie, cinematic, contol room, buttons and knobs, spacecraft, technicolor",
                        outdir="./outputs/",
                        width=1280, 
                        height=720,
                        cfg_scale = 15,
                        strength = 0.7,
                        init_img = lastimg)
    print("gneration ", str(i) , " of " , str(len(obstrat)))
    print(outputs)
    tweet = "obliquestrategies in stable diffusion, run 7 , outputimag goes to nextinit, neg bias for chars: \n" + strat
    try:
        tweetimg(outputs[0][0], tweet)
    except:
        pass
    lastimg = outputs[0][0]





