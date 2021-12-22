import string as stringlib
import time
# import pygame
from num2words import num2words

from gtts import gTTS

# from io import BytesIO

# mp3_fp = BytesIO()

mp3_fp = open("twelve.mp3", "wb")

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

def outputstr(string, end='\n'):
    print(string, end = end)
    if string in stringlib.punctuation or string in stringlib.whitespace:
        return
    tts = gTTS(string, lang='en')
    tts.write_to_fp(mp3_fp)

def ordinal(i):
    return num2words(i, to='ordinal')

def cardinal(i):
    return num2words(i)

for i in range(1,13):
    outputstr("On the {} day of Christmas my true love gave to me".format(ordinal(i)))
    for j in range(i, 1, -1 ):
        outputstr("{} {}".format(cardinal(j).capitalize(), presents[j-1]), end = '')
        if j > 2:
            outputstr(",")
        else:
            outputstr(" and")
    outputstr("A {}".format(presents[0]))
        
    outputstr("")
    
# mp3_fp.seek(0)
# pygame.mixer.init()
# pygame.mixer.music.load(mp3_fp)
# pygame.mixer.music.play()

mp3_fp.close()
