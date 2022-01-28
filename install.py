#!/usr/bin/python3
import os
import os.path
import shutil
os.system('pip install psutil py-cpuinfo datetime colorama && sudo cp tinyfetch /usr/bin/ && sudo chmod +x tinyfetch')

if not os.path.isdir(f'/home/{os.getlogin()}/.config/tinyfetch/') :
    os.mkdir(f'/home/{os.getlogin()}/.config/tinyfetch/')

shutil.copyfile(f'./config.ini', f'/home/{os.getlogin()}/.config/tinyfetch/config.ini')