# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 08:49:29 2021

@author: a0c08w6
"""
import os
import getpass

def get_user_id():
    return getpass.getuser()

class file_management:
    def __init__(self):
        self.root_exists = False
        self.file_path = "C:/Users/" + get_user_id() + "/AppData/Local/Monitor/"
        self.group_name = "Websites.txt"
         
    def path_exists(self, file=""):
        return os.path.exists(self.file_path + file)
    
    def create_group_dir(self):
        if self.path_exists() is True:
            return
        else:
            os.mkdir(self.file_path)
            self.root_exists = True
            
    def create_group_file(self, group_name):
        group_name = group_name + ".txt"
        if self.path_exists(group_name):
             print("File already exists")
        else:
            with open(os.path.join(self.file_path, group_name), 'w+') as file:
                file.write("")
            print("file created")