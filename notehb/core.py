"""
file logic internal 
"""

""" ------------ MODULOS ------------"""
import os
import json
from os.path import isdir
import time

""" ------------ FUNCIONES GLOBALES ------------"""
# --- Funcion de configuracion inicial ---
def initial_config():
    # Tarea de testeo
    test_task_list = [{'name':'test', 'description':'test', 'date':'01/01/3000', 'status':False}]

    # Comprobar no existe notehb lo crea
    if os.path.isdir('~/.config/notehb') != True:
        os.mkdir('~/.config/notehb')

    # Comprobar no existe hb_list lo crea
    if os.path.isdir('~/.config/notehb/hb_list') != True:
        os.mkdir('~/.config/notehb/hb_list')

    # Comprobar no existe default.json lo crea
    if os.path.isdir('~/.config/notehb/hb_list/default.json') != True:
        with open('.config/notehb/hb_list/default.json', 'w', encoding="utf-8") as fileconf:
            fileconf.write(test_task_list)
