# LED-christmas-tree-webui

This is a web interface to control the 
RGB-Christmas-Tree sold by ThePiHut here:
https://thepihut.com/products/3d-rgb-xmas-tree-for-raspberry-pi

## What do you need

- You need a Raspberry Pi
- You need an [RGB-Christmas-Tree](https://thepihut.com/products/3d-rgb-xmas-tree-for-raspberry-pi)
- you need the Pi to be up and running some linux distro and you need python3 installed

## How to setup

WARNING: This setup is not meant to be run on
the a public pi accessable from the internet or on a larger network. In this case
it is highly recommended setting up a reverse proxy.

For a little setup at home for Christmas, you can
easily use this:

- `git clone git@github.com:JonasBernard/led-christmas-tree-webui.git`
- `cd led-christmas-tree-webui`
- `python3 -v venv venv`
- `source venv/bin/activate`
- `pip install -r requirements.txt`
- `pip install gpiozero`
- `flask --app src/app run --host 0.0.0.0`

Now, you should be able to see the web interface
when entering the IP address of the PI in your
browser from the same network with the port 5000 attached, for example

```
http://192.168.1.110:5000
```

## For testing on a laptop or dektop

Just follow the setup above but leave the installation
of "gpiozero". The actions that would be performed on
the christmas tree will just be printed to the console.

## Setup the server up to start on boot

If you want the server to start on boot, just create the following file in your home directory.
Name it for example `tree.sh`. Maybe you need to change
the path in the `cd` command, if you cloned the
repository somewhere else than your home directory.

```
#!/bin/bash
cd led-christmas-tree-webui
source venv/bin/activate
flask --app src/app run --host 0.0.0.0
```

Then, make it executable:

```
chmod +x tree.sh
```

Now, run

```
./home/pi/tree.sh > /home/pi/christmas-tree-log.txt &
```

Do not forget the `&` at the end of the line if you want to detach the process.
