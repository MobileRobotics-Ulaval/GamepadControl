#GamepadControl

This project was created to launch linux command using a gamepad (shortcuts). The main file is GamepadDaemon.py. This script waits for input of the gamepad and executes the commands associated. This 


## Dependencies
- Python (2.7.3 used). 
    - If you use Ubuntu, Python is probably already installed on your system. 
    - You can check if by typing this command in the terminal : 
        - *python --version*
    - For more information on Python check their [website](https://www.python.org/)
- Pygame (1.9.1 from source used)
    - You will also need pygame library to use the gamepad functions
    - It is possible to install it using *apt-get install*, but I suggest to compile it directly from the source code (there is nasty debug output with the *apt-get install* version)
        1. Install pygame dependencies:
            - *sudo apt-get install mercurial python-dev python-numpy ffmpeg \
            libsdl-image1.2-dev libsdl-mixer1.2-dev libsdl-ttf2.0-dev libsmpeg-dev \
            libsdl1.2-dev  libportmidi-dev libswscale-dev libavformat-dev libavcodec-dev*
        2. You will need mercurial to get the source code:
            - *sudo apt-get install mercurial*
        3. Go to any desired folder (let's use the home folder) and clone the pygame source code
            - *cd ~/*
            - *hg clone https://bitbucket.org/pygame/pygame*
        4. Build and install the library
            - *cd pygame*
            - *python setup.py build*
            - *sudo python setup.py install*


## Launch the daemon at system startup

## Gamepad ID and button map

You can use the following application to check it !
jstest --event /dev/input/js0
