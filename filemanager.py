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

    file_path = "C:/Users/" + get_user_id() + "/AppData/Local/Monitor/"
    group_name = "Websites.txt"
         
    def path_exists(self, file=""):
        return os.path.exists(self.file_path + file)
    
    def create_group_dir(self):
        os.mkdir(self.file_path)
            
    def create_group_file(self):
        with open(os.path.join(self.file_path, self.group_name), 'w') as file:
            file.write("")