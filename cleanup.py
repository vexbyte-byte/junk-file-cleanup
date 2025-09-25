# android junk file remover

import os
import time
import shutil
from datetime import datetime
# from send2trash import send2trash as delete

# base:
SEARCH_ROOT = r"/storage/emulated/0"

# define variables
red = "\033[91m"
b_green = "\033[92m"
d_green = "\033[32m"
b_yellow = "\033[93m"
d_yellow = "\033[33m"

# list of directories to clean
directory_list = [ # you can add more
    # whatsapp junk files
    r"/storage/emulated/0/Android/media/com.whatsapp/WhatsApp/.Shared",
    r"/storage/emulated/0/Android/media/com.whatsapp/WhatsApp/.StickerThumbs",
    r"/storage/emulated/0/Android/media/com.whatsapp/WhatsApp/.Thumbs",
    r"/storage/emulated/0/Android/media/com.whatsapp/WhatsApp/.trash",
    r"/storage/emulated/0/Android/media/com.whatsapp/WhatsApp/Backups/Stickers",
    r"/storage/emulated/0/Android/media/com.whatsapp/WhatsApp/Backups",
    r"/storage/emulated/0/Android/media/com.whatsapp/WhatsApp/Databases",
    r"/storage/emulated/0/Android/media/com.whatsapp/WhatsApp/Media/.Links",
    r"/storage/emulated/0/Android/media/com.whatsapp/WhatsApp/Media/.Statuses",
    r"/storage/emulated/0/Android/media/com.whatsapp/WhatsApp/Media/.udDHFY8K4Eqg",
    r"/storage/emulated/0/Android/media/com.whatsapp/WhatsApp/Media/Wallpaper",
    r"/storage/emulated/0/Android/media/com.whatsapp/WhatsApp/Media/WhatsApp AI Media",
    r"/storage/emulated/0/Android/media/com.whatsapp/WhatsApp/Media/WhatsApp Animated Gifs",
    r"/storage/emulated/0/Android/media/com.whatsapp/WhatsApp/Media/WhatsApp Audio",
    r"/storage/emulated/0/Android/media/com.whatsapp/WhatsApp/Media/WhatsApp Backup Excluded Stickers",
    r"/storage/emulated/0/Android/media/com.whatsapp/WhatsApp/Media/WhatsApp Bug Report Attachments",
    r"/storage/emulated/0/Android/media/com.whatsapp/WhatsApp/Media/WhatsApp Documents/Sent/.nomedia",
    r"/storage/emulated/0/Android/media/com.whatsapp/WhatsApp/Media/WhatsApp Documents/Private/.nomedia",
    r"/storage/emulated/0/Android/media/com.whatsapp/WhatsApp/Media/WhatsApp Documents/Private",
    r"/storage/emulated/0/Android/media/com.whatsapp/WhatsApp/Media/WhatsApp Images/Private/.nomedia",
    r"/storage/emulated/0/Android/media/com.whatsapp/WhatsApp/Media/WhatsApp Images/Sent/.nomedia",
    r"/storage/emulated/0/Android/media/com.whatsapp/WhatsApp/Media/WhatsApp Profile Photos",
    r"/storage/emulated/0/Android/media/com.whatsapp/WhatsApp/Media/WhatsApp Sticker Packs/.nomedia",
    r"/storage/emulated/0/Android/media/com.whatsapp/WhatsApp/Media/WhatsApp Sticker Packs",
    r"/storage/emulated/0/Android/media/com.whatsapp/WhatsApp/Media/WhatsApp Stickers/.nomedia",
    r"/storage/emulated/0/Android/media/com.whatsapp/WhatsApp/Media/WhatsApp Video/Private/.nomedia",
    r"/storage/emulated/0/Android/media/com.whatsapp/WhatsApp/Media/WhatsApp Video/Sent/.nomedia",
    r"/storage/emulated/0/Android/media/com.whatsapp/WhatsApp/Media/WhatsApp Video Notes/.nomedia",
    r"/storage/emulated/0/Android/media/com.whatsapp/WhatsApp/Media/WhatsApp Video Notes",
    r"/storage/emulated/0/Android/media/com.whatsapp/WhatsApp/Media/WhatsApp Voice Notes",
    # instagram junk files
    r"/storage/emulated/0/Android/media/com.instagram.android",
    # X-Recorder junk files
    r"/storage/emulated/0/Android/media/videoeditor.videorecorder.screenrecorder",
    # android junk files
    r"/storage/emulated/0/Android/obb/com.avast.android.mobilesecurity",
    r"/storage/emulated/0/Android/obb/com.sec.android.app.samsungapps",
    r"/storage/emulated/0/Android/obb/.nomedia",
    r"/storage/emulated/0/Ams_vault/.data/.key_store",
    r"/storage/emulated/0/Ams_vault/.data/.metadata_store",
    r"/storage/emulated/0/Ams_vault/.data",
    r"/storage/emulated/0/Ams_vault/.mid_pictures",
    r"/storage/emulated/0/Ams_vault/.thumbnail",
    r"/storage/emulated/0/Ams_vault/pictures",
    r"/storage/emulated/0/DCIM/Deco Pic",
    r"/storage/emulated/0/Movies/.thumbnails/.database_uuid",
    r"/storage/emulated/0/Movies/.thumbnails/.nomedia",
    r"/storage/emulated/0/Movies/.thumbnails",
    r"/storage/emulated/0/Movies/VideoGlitch/.screenCapture",
    r"/storage/emulated/0/Movies/VideoGlitch",
    r"/storage/emulated/0/Music/.thumbnails/.database_uuid",
    r"/storage/emulated/0/Music/.thumbnails/.nomedia",
    r"/storage/emulated/0/Music/.thumbnails",
    r"/storage/emulated/0/Music",
    r"/storage/emulated/0/Pictures/.thumbnails/.database_uuid",
    r"/storage/emulated/0/Pictures/.thumbnails/.nomedia",
    r"/storage/emulated/0/Pictures/.thumbnails",
    r"/storage/emulated/0/Pictures/stickers",
    r"/storage/emulated/0/Pictures/stickers_renamed",

    # nomedia files
    r'/storage/emulated/0/Android/media/com.whatsapp/WhatsApp/Media/WhatsApp Audio/Sent/.nomedia', 
    r'/storage/emulated/0/Android/media/com.whatsapp/WhatsApp/Media/WhatsApp Audio/Private/.nomedia', 
    r'/storage/emulated/0/Android/media/com.whatsapp/WhatsApp/Media/WhatsApp AI Media/.nomedia', 
    r'/storage/emulated/0/Android/media/com.whatsapp/WhatsApp/Media/WhatsApp Animated Gifs/Sent/.nomedia', 
    r'/storage/emulated/0/Android/media/com.whatsapp/WhatsApp/Media/WhatsApp Animated Gifs/Private/.nomedia', 
    r'/storage/emulated/0/Android/media/com.whatsapp/WhatsApp/Media/WhatsApp Voice Notes/.nomedia', 
    r'/storage/emulated/0/Android/media/com.whatsapp/WhatsApp/Media/.Links/.nomedia', 
    r'/storage/emulated/0/Android/media/com.whatsapp/WhatsApp/Media/.Statuses/.nomedia', 
    r'/storage/emulated/0/Android/media/com.whatsapp/WhatsApp/Media/.udDHFY8K4Eqg/.nomedia', 
    r'/storage/emulated/0/Android/media/com.whatsapp/WhatsApp/Media/WhatsApp Backup Excluded Stickers/.nomedia', 
    r'/storage/emulated/0/Android/media/com.whatsapp/WhatsApp/Media/WhatsApp Bug Report Attachments/.nomedia', 
    r'/storage/emulated/0/Android/media/com.whatsapp/WhatsApp/.Shared/.nomedia', 
    r'/storage/emulated/0/Android/.Trash/com.sec.android.app.myfiles/.nomedia', 
    r'/storage/emulated/0/Android/.Trash/com.sec.android.app.myfiles/11b3e3d6-43e3-4a6b-b4dd-441f6036b93bT3/1758423551688/storage/emulated/0/Android/media/com.whatsapp/WhatsApp/Media/WhatsApp Backup Excluded Stickers/.!%#@$/.nomedia',

]

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
        while True:
            # list menu
            # input
            utils.logo()
            print(f"{b_green}[{d_yellow}01{b_green}]{d_green} Search for .nomedia files that aren't included in database")
            print(f"{b_green}[{d_yellow}02{b_green}]{d_green} Search for broken directories in database")
            print(f"{b_green}[{d_yellow}03{b_green}]{d_green} Remove junk files")
            print(red)
            print()
            choice = str(input(f"[Main Menu] > {d_yellow}"))
            utils.clear_screen()
            utils.logo()
            # filter
            if choice.startswith("0") and len(choice) > 1:
                choice = choice[-1]
            
            options = {
                "1": "engine.find_nomedia(SEARCH_ROOT)",
                "2": "engine.detect_directories()",
                "3": "engine.main()"
            }

            try:
                value = options.get(choice)
                exec(value)
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


    def main():
        initial_time = time.time()
        var_1 = 20
        var_2 = 10
        # variables
        deleted_items = []
        total_items = int(len(directory_list))
        file_deleted_count = 0
        folder_deleted_count = 0

        for directory in directory_list:
            now = datetime.now()
            formatted_time = now.strftime("%H:%M:%S")
            if not os.path.exists(directory):
                print(f"{red}[{formatted_time}] Directory does not exist: {directory[-20:]}")
                continue # skip if file not found

            # for file_name in os.listdir(directory):
            # file_path = os.path.join(directory, file_name)
            try:
                # Delete files only
                if os.path.isfile(directory):
                    try:
                        # os.remove(directory)
                        print(f"{b_green}[{d_yellow}{formatted_time}{b_green}] Successfully Removed: {directory}")
                        file_deleted_count += 1
                    except Exception as e:
                        print(f"{red}[{formatted_time}] ", e)

                # Delete empty directories
                elif os.path.isdir(directory):
                    try:
                        # shutil.rmtree(directory)
                        print(f"{b_green}[{d_yellow}{formatted_time}{b_green}] Successfully Removed Empty Dir: {directory}")
                        folder_deleted_count += 1
                    except Exception as e:
                        print(f"{red}[{formatted_time}] ", e)
                try:
                    percentage = (int(len(deleted_items))/total_items) * 100
                    elapsed_time = time.time() - initial_time
                except:
                    pass

                print(f"{b_green}\n")
                print(f"{b_green}Cleaning Up".ljust(var_1) + f"{d_green}:".ljust(var_2) + percentage)
                print(f"{b_green}Files deleted".ljust(var_1) + f"{d_green}:".ljust(var_2) + file_deleted_count)
                print(f"{b_green}Folders Deleted".ljust(var_1) + f"{d_green}:".ljust(var_2) + folder_deleted_count)
                print(f"{b_green}Time Taken (Seconds)".ljust(var_1) + f"{d_green}:".ljust(var_2) + int(round(elapsed_time)))
                
            except Exception as e:
                print(f"{red}[{formatted_time}] ", e)

        print(f"\n{d_green}[+]{b_green} Cleanup Complete!\n")


    def find_nomedia(root_path):
        print(f"{b_green}[*]{d_green} Searching for .nomedia under: {SEARCH_ROOT}\n")
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



if __name__ == "__main__":
    utils.clear_screen()
    utils.selection()

