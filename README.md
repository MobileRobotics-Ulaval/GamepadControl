GamepadControl
==============

This script allows to launch linux command using a gamepad (by creating shortcuts)



## Required installation (pygame)
You need python to use this script (2.7.3 used on the Husky). You can check if you have Python installed by typing :
>> sudo python setup.py install

### Install dependencies
sudo apt-get install mercurial python-dev python-numpy ffmpeg \
    libsdl-image1.2-dev libsdl-mixer1.2-dev libsdl-ttf2.0-dev libsmpeg-dev \
    libsdl1.2-dev  libportmidi-dev libswscale-dev libavformat-dev libavcodec-dev
 
### Grab source
hg clone https://bitbucket.org/pygame/pygame
 
### Finally build and install
cd pygame
python setup.py build
sudo python setup.py install

## Button map
You can use the following application to check it !
jstest --event /dev/input/js0
