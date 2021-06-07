# -*- coding: utf-8 -*-
"""
monitor.py opens all the monitoring pages for
Field Support - EMS
"""
import webbrowser
import os
from filemanager import file_management
from readwrite import read_write
import getpass

def get_user_id():
    return getpass.getuser()

class monitor():

    def open_sites(self, group_name):
        reader = read_write()
        for i in range(len(reader.groups)):
            if (reader.groups[i].name == group_name):
                for site in reader.groups[i].dict:
                    webbrowser.open(reader.groups[i].dict[site])
    
    
    
if __name__ == "__main__":
    monty = read_write()
    monty.load_group("Websites")
    mon = monitor()
    mon.open_sites("Websites")
    


    
    