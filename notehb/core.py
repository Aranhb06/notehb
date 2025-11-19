"""
file logic internal 
"""
# --- Imports ---
import time
import os

# --- Funtions globals ---
def init_default(dir_config,list_task):
    if os.system('ls ~/.config/ | grep notehb') != dir_config:
        os.system('mkdir ~/.config/notehb')
    else:
        if os.system('ls ~/.config/notehb/ | grep list') != dir_config:
            os.system('mkdir ~/.config/notehb/list')
        else:
            if os.system('ls ~/.config/notehb/list | grep default.json') != list_task:
                os.system('touch ~/.config/notehb/default.json')
            else:

