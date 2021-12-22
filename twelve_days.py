import string as stringlib
import time
# import pygame
from num2words import num2words
import os
from tempfile import TemporaryFile
from gtts import gTTS
import io
# from IPython.display import Audio
import pyglet

# pyglet.options["audio"] = ("DirectSound",)
pyglet.options['search_local_libs'] = True

# options are DirectSound and OpenAL -- go for default, whatever that is.

# from io import BytesIO

# mp3_fp = BytesIO()

# mp3_filename = "twelve.mp3"
# 
# try: 
#     mp3_fp = open(mp3_filename, "wb")
# except:
#     os.remove(mp3_filename)
#     mp3_fp = open(mp3_filename, "wb")
    

presents = [
    "partridge in a pear tree.",
    "turtle doves",
    "French hens",
    "calling birds",
    "gold rings",
    "geese a-laying",
    "swans a-swimming",
    "maids a-milking",
    "ladies dancing",
    "lords a-leaping",
    "pipers piping",
    "drummers drumming"]

# this only works in an ipython notebook (I think)
def ispeak(my_text):
    with io.BytesIO() as f:
        gTTS(text=my_text, lang='en').write_to_fp(f)
        f.seek(0)
        return Audio(f.read(), autoplay=True, rate=100)
        
def speak(words: str, lang: str="en"):
    with io.BytesIO() as f:
        gTTS(text=words, lang=lang).write_to_fp(f)
        f.seek(0)
        
        player = pyglet.media.load('_.mp3', file=f).play()
        while player.playing:
            time.sleep(1)
            pyglet.app.platform_event_loop.dispatch_posted_events()
            pyglet.clock.tick()
# end speak()

            
first_line = "\n\nOn the {} day of Christmas my true love gave to me"

def old_outputstr(string, end='\n'):
    print(string, end = end)
    if string in stringlib.punctuation or string in stringlib.whitespace:
        return
    tts = gTTS(string, lang='en')
    tts.write_to_fp(mp3_fp)

def outputstr(string):
    print(string)
    speak(string)
    
def ordinal(i):
    return num2words(i, to='ordinal')

def cardinal(i):
    return num2words(i)

def sing_song(days):
    for i in range(1, min(12, days+1)):
        outputstr(first_line.format(ordinal(i)))
        for j in range(i, 1, -1 ):
            this_line = "{} {}, ".format(cardinal(j).capitalize(), presents[j-1])
            outputstr(this_line)
        last_line = "a {}".format(presents[0])
        if i > 1:
            last_line = "And "+last_line
        outputstr(last_line)
            
# mp3_fp.seek(0)
# pygame.mixer.init()
# pygame.mixer.music.load(mp3_fp)
# pygame.mixer.music.play()

# mp3_fp.close()

sing_song(12)
