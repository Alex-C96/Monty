# -*- coding: utf-8 -*-
"""
monitor.py opens all the monitoring pages for
Field Support - EMS
"""
import webbrowser
import os
import getpass

def get_user_id():
    return getpass.getuser()

class Monitor:
    website_list = list()
    root_exists = False
    file_path = "C:/Users/" + get_user_id() + "/AppData/Local/Monitor/"
    group_name = "Websites.txt"
    
    def open_sites(self):
        with open(self.file_path + self.group_name, 'r') as reader:
            sites = reader.readlines()
            for site in sites:
                url = site.split(',')  # read a comma delimited line
                webbrowser.open(url[1])
                
    def create_group_dir(self):
        if os.path.exists(self.file_path) is True:
            self.root_exists = True
        else:
            os.mkdir(self.file_path)
            self.root_exists = True
            
    def create_group_file(self, group_name):
        group_name = group_name + ".txt"
        if os.path.exists(self.file_path + group_name):
             print("File already exists")
        else:
            with open(os.path.join(self.file_path, group_name), 'w+') as file:
                file.write("")
                
    
    def add_website_to_group(self, file_name, site_name, site_url):
        path = self.file_path + file_name + ".txt"
        if (os.path.exists(path)):
            with open(path, 'a') as file:
                file.write("Alex")
            
    
    # FIX ME: Not finished
    def remove_website_from_group(self, group_name, site_name):
        path = self.file_path + group_name
        #if os.path.exists(path):
    
if __name__ == "__main__":
    monty = Monitor()
    monty.add_website_to_group("Websites", "sites", "www.walmart.com")
    
    
    
    """ 
    Structure idea is to create a dictionary. Read dict that reads from
    file and stores it to easily manipulate files. Or just manipulate
    file from within txt files.
    """
    
    