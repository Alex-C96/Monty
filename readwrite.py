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

class read_write:
    file_path = "C:/Users/" + get_user_id() + "/AppData/Local/Monitor/"
    dicts = {}
    group_name = "Websites.txt"

    def path_exists(self, file=""):
        return os.path.exists(self.file_path + file)

    def add_website(self, site_name, url):
        self.dicts.update({site_name: url})
        self.update_file()
        return True

    def remove_website(self, site_name):
        for key in self.dicts:
            if key == site_name:
                self.dicts.pop(site_name)
                self.update_file()
                return True
        return False

    def load_group(self):
        path = os.path.join(self.file_path, self.group_name)
        if (self.path_exists(self.group_name)):
            with open(path, 'r') as file:
                lines = file.read().splitlines()
                for line in lines:
                    if line != "":
                        vars = line.split('|')
                        self.dicts[vars[0]] = vars[1]

    def display_all(self):
        for key in self.dicts:
            print("Site name: {}\n URL: {}\n".format(key,self.dicts[key]))
    
    def display_site_names(self):
        sites = self.dicts.keys()
        str = ""
        for site in sites:
            str = str + site + ', '
        
        print(str)

    def update_file(self):
        path = os.path.join(self.file_path, self.group_name)
        if (self.path_exists(self.group_name)):
            with open(path, 'w') as file:
                for key in self.dicts:
                    file.write(key + "|" + self.dicts[key] + "\n")

