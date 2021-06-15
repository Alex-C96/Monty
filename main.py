# -*- coding: utf-8 -*-
"""
Monty is a website management tool
Intended use if for EMS to be able to pull up 
monitoring pages quickly and manage pages to be monitored
"""
import webbrowser
from os import system, name
from time import sleep
from filemanager import file_management
from readwrite import read_write
import getpass

def get_user_id():
    return getpass.getuser()

def clear():
  
    # for windows
    if name == 'nt':
        _ = system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def check_if_isdigit_or_q(input):
        if (input.isdigit()):
                return int(input)
        elif (input == 'q'):
            return input
        else:
            return -1  # triggers invalid input response 
    
    
if __name__ == "__main__":
    file_manager = file_management()
    reader_writer = read_write()

    if file_manager.path_exists() is False:
        file_manager.create_group_dir()
        file_manager.create_group_file()
    else:
        reader_writer.load_group()

    starter_menu = "Monty the Monitor app\n"

    menu = """
    =====================
    Monty the Monitor app
    1) Open Sites
    2) Display Sites
    3) Add Site
    4) Remove Site
    5) Clear Screen
    =====================
    """

    while (True):
        if (len(reader_writer.dicts) == 0):
            print(starter_menu)
            print("Add your first site:")
            site_name = input("Please enter site name: (Ex: Google)\n")
            url = input ("Please enter url: (Ex: www.google.com)\n")
            reader_writer.add_website(site_name, url)
        else:
            print(menu)
            val = input("Enter command here: ")
            val = check_if_isdigit_or_q(val)
            print(val)

            if (val == 1):
                summon = lambda x : webbrowser.open(x)
                for key in reader_writer.dicts:
                    summon(reader_writer.dicts[key])

            elif (val == 2):
                reader_writer.display_all()
        
            elif (val == 3):
                site_name = input("Please enter site name:\n")
                url = input ("Please enter url:\n")
                if (reader_writer.add_website(site_name, url)):
                    print("Site added")
                    sleep(1)
                    clear()
                
            elif (val == 4):
                print("Sites:")
                reader_writer.display_site_names()
                site_name = input("Please enter site name to be removed:\n")
                if (reader_writer.remove_website(site_name)):
                    print("Site removed")
                    sleep(1)
                    clear()
                else:
                    print("Site not found")
                    sleep(1)
                    clear()
                    
            elif (val == 5):
                clear()

            elif (val == 'q'):
                break
            else:
                print("Invalid Input\n")
    


