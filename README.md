#GamepadControl

This project was created to launch linux command using a gamepad (shortcuts). The main file is GamepadDaemon.py. This script waits for input of the gamepad and executes the command associated. This 


## Dependencies
- Python (2.7.3 used). 
    - If you use Ubuntu, Python is probably already installed on your system. 
    - You can check if by typing this command in the terminal : 
        - *python --version*
    - For more information on Python check their [website](https://www.python.org/)
- Pygame (1.9.1 from source used)
    - You will also need pygame library to use the gamepad functions
    - It is possible to install it using *apt-get install*, but I suggest to compile it directly from the source code (there is nasty debug outputs with the *apt-get install* version)
        1. Install pygame dependencies:
            - *sudo apt-get install mercurial python-dev python-numpy ffmpeg \
            libsdl-image1.2-dev libsdl-mixer1.2-dev libsdl-ttf2.0-dev libsmpeg-dev \
            libsdl1.2-dev  libportmidi-dev libswscale-dev libavformat-dev libavcodec-dev*
        2. Go to any desired folder (let's use the home folder) and clone the pygame source code
            - *cd ~/*
            - *hg clone https://bitbucket.org/pygame/pygame*
        3. Build and install the library
            - *cd pygame*
            - *python setup.py build*
            - *sudo python setup.py install*

## Using the application
1. Check the gamepad input and button mapping
    - *sudo apt-get install joystick*
    - The joystick/gamepad device should be in */dev/input/js0*, check it with the command: 
        - *ls /dev/input*
    - You can check the gamepad button mapping using this command (press a button and the ID will be output):
        - *jstest --event /dev/input/js0*
2. Clone the code on your computer (let's use the home folder again)
    - *sudo apt-get install git-core*
    - *cd ~/*
    - *git clone https://github.com/MobileRobotics-Ulaval/GamepadControl.git*
3. Start the application
    - *cd ~/GamepadControl/*
    - *chmod +x GamepadDaemon.py*
    - *./GamepadDaemon.py*
4. Take a look at the code to see the different commands mapped
    - For instance: BACK+START (button 8 + button 9) will stop the application

## Launch the daemon at system startup
Since we use the application to reduce the use of a computer connected to the robot via ssh, the gamepad control application must be started at computer startup. I struggled to find a working solution for this...



## Note
Feel free to send me a email (sebastien.michaud.2@gmail.com) if you find any error or imcomplete information in the README or the code (I did it kind of fast and I didn't do the whole process to make sure it is all perfect).
