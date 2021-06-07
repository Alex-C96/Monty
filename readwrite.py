# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 14:03:35 2021

@author: a0c08w6
"""
import getpass
import os
from filemanager import file_management

def get_user_id():
    return getpass.getuser()

class storage():
    def __init__(self, name):
        self.dict = {}
        self.name = name
    
    def print_all(self):
        for pair in self.dict.items():
            print(pair)

class read_write:
    file_path = "C:/Users/" + get_user_id() + "/AppData/Local/Monitor/"
    groups = []

    def path_exists(self, file=""):
        return os.path.exists(self.file_path + file)

    #def add_website_to_group(self, group_name, url):
        
    #def remove_website_from_group(self, group_name, site_name):

    def load_group(self, group_name):
        store = storage(group_name)
        group_name = group_name + ".txt"

        path = os.path.join(self.file_path, group_name)
        if (self.path_exists(group_name)):
            with open(path, 'r') as file:
                lines = file.read().splitlines()
                for line in lines:
                    vars = line.split('|')
                    store.dict[vars[0]] = vars[1]

        self.groups.append(store)
