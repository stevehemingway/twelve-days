
When I was at school, back in the seventies, the computer science master, Steve Legg, 
set us an exercise in the last lesson of term before Christmas.
This was to generate the words of the carol 'The Twelve Days of Christmas', in BASIC.

I've started to teach myself Python, and I managed to write a version which spat out the lines
of the carol, in text. It occurred to me that Python has so many useful libraries that I could probably
do what would have been completely impossible in 1974, which was to actually get the computer to say the words
out loud.

After a few false starts, and a bit of digging around on Stack Overflow, I hit on a means which more or less works.
Really, the biggest problem was getting the program to play the sound directly, rather than just writing it to an mp3 file.
I ended up using a library called pyglet. It seems to be a rather fully-fledged thing for creating a proper GUI 
program in Python, but it has some audio methods which did the trick.

I started off by reading [this](https://github.com/pndurette/gTTS/issues/26) rather long thread.
It's still not clear to me why direct speaking is so tricky.
I had to add rather a lot of libraries to make this work, in a venv, including ffmpeg. 
It seems to work on Windows. I haven't tried it elsewhere.
