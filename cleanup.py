# android junk file remover

import os
import time
import shutil
import requests
import subprocess
from datetime import datetime
# from send2trash import send2trash as delete

# define variables
red = "\033[91m"
b_green = "\033[92m"
d_green = "\033[32m"
b_yellow = "\033[93m"
d_yellow = "\033[33m"

file_deleted_count = 0
folder_deleted_count = 0
failed_items = 0
progress = 0

# list of directories to clean
temp_directory_list = []
files_list = []
folders_list = []
# will be loaded later using github
directory_list = []

# will be  loaded later using github
data = []

class utils():
    def logo():
        text = r"""
     ________  ___       _______   ________  ________   ___  ___  ________   
    |\   ____\|\  \     |\  ___ \ |\   __  \|\   ___  \|\  \|\  \|\   __  \  
    \ \  \___|\ \  \    \ \   __/|\ \  \|\  \ \  \\ \  \ \  \\\  \ \  \|\  \ 
     \ \  \    \ \  \    \ \  \_|/_\ \   __  \ \  \\ \  \ \  \\\  \ \   ____\
      \ \  \____\ \  \____\ \  \_|\ \ \  \ \  \ \  \\ \  \ \  \\\  \ \  \___|
       \ \_______\ \_______\ \_______\ \__\ \__\ \__\\ \__\ \_______\ \__\   
        \|_______|\|_______|\|_______|\|__|\|__|\|__| \|__|\|_______|\|__|                                                          
    """
        print(text)
        print()

    def selection():
        global directory_list
        engine.explore_subfolders()
        engine.filter_directories()
        while True:
            # list menu
            # input
            utils.logo()
            print(f"{b_green}[{d_yellow}01{b_green}]{d_green} Search for .nomedia files that aren't included in database")
            print(f"{b_green}[{d_yellow}02{b_green}]{d_green} Search for broken directories in database")
            print(f"{b_green}[{d_yellow}03{b_green}]{d_green} Remove junk files")
            print(f"{b_green}[{d_yellow}04{b_green}]{d_green} Clear App Data Recursively (ADB)")
            print(red)
            print()
            choice = str(input(f"[Main Menu] > {d_yellow}"))
            utils.clear_screen()
            utils.logo()
            # filter
            if choice.startswith("0") and len(choice) > 1:
                choice = choice[-1]
            
            options = {
                "1": engine.find_nomedia,
                "2": engine.detect_directories,
                "3": engine.main,
                "4": engine.clear_app_data,
            }

            try:
                value = options.get(choice)
                value()
            except:
                utils.clear_screen()
                continue
            input()
            utils.clear_screen()


    def clear_screen():
        try:
            os.system("cls" if os.name == "nt" else "clear")
            print("\033c\033[0m", end="")
        except Exception as e:
            pass

class engine():
    def detect_directories():
        broken_dir = []
        good_dir = []
        for directory in directory_list:
            if not os.path.exists(directory):
                broken_dir.append(directory)
                continue
            if os.path.exists(directory):
                good_dir.append(directory)
                continue
        
        a = f"{red}[!] Paths/Directories not Found Error:"
        print(a, "\n", "-" * len(a))
        for broken_path in broken_dir:
            print(f"{red}[-] ", broken_path)
        
        print()
        a = f"{d_green}[*]{b_green} Paths/Directories Found:"
        print(a, "\n", "-" * len(a))
        for good_path in good_dir:
            print(f"{d_green}[+]{b_green} ", good_path)
    
    def filter_directories():
        # globals
        global failed_items
        global folder_deleted_count
        global file_deleted_count

        for directory in directory_list:
            try:
                if not os.path.exists(directory):
                    failed_items += 1
                    continue
                # Delete files only
                if os.path.isfile(directory):
                    try: files_list.append(directory)
                    except: pass

                # Delete empty directories
                elif os.path.isdir(directory):
                    try: folders_list.append(directory)
                    except: pass
            except:
                pass
        
        # sorting directories by depth
        try: folders_list.sort(key=lambda x: x.count(os.sep), reverse=True)
        except: pass

    def explore_subfolders():
        for directory in directory_list:
            for root, dirs, files in os.walk(directory, topdown=False):
                for file_name in files:
                    file_path = os.path.join(root, file_name)
                    try: temp_directory_list.append(file_path)
                    except: pass
                
                for dir_name in dirs:
                    dir_path = os.path.join(root, dir_name)
                    try: temp_directory_list.append(dir_path)
                    except: pass
        # combine
        directory_list.extend(temp_directory_list)
        temp_directory_list.clear()

    def main():
        # globals
        global failed_items
        global folder_deleted_count
        global file_deleted_count
        global progress

        # variables
        initial_time = time.time()
        var_1, var_2, var_3, var_4 = 30,10,20,20
        total_items = int(len(directory_list))

        # delete files
        for directory in files_list:
            progress += 1
            now = datetime.now()
            formatted_time = now.strftime("%H:%M:%S")
            # i know i already had this check earlier
            # but it doesnt mean a path would continue to be present during runtime
            if not os.path.exists(directory):
                print(f"{red}[{formatted_time}] Directory does not exist: {directory[-var_4:]}")
                continue # skip if file not found
            
            try:
                os.remove(directory)
                print(f"{b_green}[{d_yellow}{formatted_time}{b_green}] Successfully Removed: {directory[-var_4:]}")
                file_deleted_count += 1
            except Exception as e:
                print(f"{red}[{formatted_time}] ", e)
            
            # calculate percentage
            try:
                percentage = progress / total_items * 100
                elapsed_time = time.time() - initial_time
                
                # print
                print(f"{b_green}\n")
                print(f"{b_green}Cleaning Up".ljust(var_1), f"{d_green}:".ljust(var_2), f"{int(round(percentage))}%", flush=True)
                print(f"{b_green}Files deleted".ljust(var_1), f"{d_green}:".ljust(var_2), int(file_deleted_count), flush=True)
                print(f"{b_green}Folders Deleted".ljust(var_1), f"{d_green}:".ljust(var_2), int(folder_deleted_count), flush=True)
                print(f"{b_green}Time Taken (Seconds)".ljust(var_1), f"{d_green}:".ljust(var_2), int(round(elapsed_time)), flush=True)
                
            except Exception as e:
                print(f"{red}[{formatted_time}] ", e)
                        
            # format screen
            utils.clear_screen()
            utils.logo()

        # Delete folders
        for directory in folders_list:
            progress += 1
            now = datetime.now()
            formatted_time = now.strftime("%H:%M:%S")

            if not os.path.exists(directory):
                print(f"{red}[{formatted_time}] Directory does not exist: {directory[-var_4:]}")
                continue # skip if file not found

            try:
                shutil.rmtree(directory)
                print(f"{b_green}[{d_yellow}{formatted_time}{b_green}] Successfully Removed Empty Dir: {directory[-var_4:]}")
                folder_deleted_count += 1
            except Exception as e:
                print(f"{red}[{formatted_time}] ", e)
            
            # calculate percentage
            try:
                percentage = progress / total_items * 100
                elapsed_time = time.time() - initial_time

                # print
                print(f"{b_green}\n")
                print(f"{b_green}Cleaning Up".ljust(var_1), f"{d_green}:".ljust(var_2), f"{int(round(percentage))}%", flush=True)
                print(f"{b_green}Files deleted".ljust(var_1), f"{d_green}:".ljust(var_2), int(file_deleted_count), flush=True)
                print(f"{b_green}Folders Deleted".ljust(var_1), f"{d_green}:".ljust(var_2), int(folder_deleted_count), flush=True)
                print(f"{b_green}Time Taken (Seconds)".ljust(var_1), f"{d_green}:".ljust(var_2), int(round(elapsed_time)), flush=True)
                
            except Exception as e:
                print(f"{red}[{formatted_time}] ", e)
            
            # format screen
            utils.clear_screen()
            utils.logo()

        print(f"\n{d_green}[+]{b_green} Cleanup Complete!\n")


    def find_nomedia():
        root_path = r"/storage/emulated/0"
        print(f"{b_green}[*]{d_green} Searching for .nomedia under: {root_path}\n")
        """Recursively walk through root_path and print all .nomedia files."""
        for dirpath, dirnames, filenames in os.walk(root_path):
            for name in filenames:
                if name == ".nomedia":
                    nomedia_path = os.path.join(dirpath, name)
                    if nomedia_path not in directory_list:
                        print(f"{b_green}[+]{d_green} {nomedia_path}")
        print(f"\n{b_green}[+]{d_green} Search complete.")
        

    def sanitize():
        text = "[+] /storage/emulated/0/Android/media/com.whatsapp/WhatsApp/Media/WhatsApp Audio/Sent/.nomedia [+] /storage/emulated/0/Android/media/com.whatsapp/WhatsApp/Media/WhatsApp Audio/Private/.nomedia [+] /storage/emulated/0/Android/media/com.whatsapp/WhatsApp/Media/WhatsApp AI Media/.nomedia [+] /storage/emulated/0/Android/media/com.whatsapp/WhatsApp/Media/WhatsApp Animated Gifs/Sent/.nomedia [+] /storage/emulated/0/Android/media/com.whatsapp/WhatsApp/Media/WhatsApp Animated Gifs/Private/.nomedia [+] /storage/emulated/0/Android/media/com.whatsapp/WhatsApp/Media/WhatsApp Voice Notes/.nomedia [+] /storage/emulated/0/Android/media/com.whatsapp/WhatsApp/Media/.Links/.nomedia [+] /storage/emulated/0/Android/media/com.whatsapp/WhatsApp/Media/.Statuses/.nomedia [+] /storage/emulated/0/Android/media/com.whatsapp/WhatsApp/Media/.udDHFY8K4Eqg/.nomedia [+] /storage/emulated/0/Android/media/com.whatsapp/WhatsApp/Media/WhatsApp Backup Excluded Stickers/.nomedia [+] /storage/emulated/0/Android/media/com.whatsapp/WhatsApp/Media/WhatsApp Bug Report Attachments/.nomedia [+] /storage/emulated/0/Android/media/com.whatsapp/WhatsApp/.Shared/.nomedia [+] /storage/emulated/0/Android/.Trash/com.sec.android.app.myfiles/.nomedia [+] /storage/emulated/0/Android/.Trash/com.sec.android.app.myfiles/11b3e3d6-43e3-4a6b-b4dd-441f6036b93bT3/1758423551688/storage/emulated/0/Android/media/com.whatsapp/WhatsApp/Media/WhatsApp Backup Excluded Stickers/.!%#@$/.nomedia"
        paths = [p.strip() for p in text.split("[+]") if p.strip()]
        lists = []
        for i in paths:
            lists.append(i)
        print(lists)
    
    def clear_app_data():
        total_app = len(data)
        progress = 0
        for package_name in data:
            progress += 1
            utils.clear_screen()
            print(f"{d_green}[*]{b_green} clearing data for: ", package_name)
            percentage = progress / total_app * 100
            print(f"\n\n{b_green}Percentage: {int(round(percentage))}%")
            subprocess.run(["adb", "shell", "pm", "clear", package_name])
        print(f"\n\n{d_green}[+]{b_green} Cleanup Complete!")

class github_Api():
    global directory_list
    global data
    def get_and_run_database(url):
        try:
            r = requests.get(url)
            status = r.status_code
            if status == 200: contents = r.text
            else: print(f"{red}[!] Unable to obtain database. Status code: {status}")
        except Exception as e: print(f"{red}[!] ", e)
        exec(contents, globals())


if __name__ == "__main__":
    utils.clear_screen()
    print(f"{d_yellow}[{red}!{d_yellow}] Initializing")
    github_Api.get_and_run_database('https://raw.githubusercontent.com/vexbyte-byte/junk-file-cleanup/refs/heads/main/database_1')
    github_Api.get_and_run_database('https://raw.githubusercontent.com/vexbyte-byte/junk-file-cleanup/refs/heads/main/database_3')
    utils.clear_screen()
    utils.selection()

