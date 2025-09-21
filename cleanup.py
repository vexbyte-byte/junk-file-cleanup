# android junk file remover

import os
from datetime import datetime
from send2trash import send2trash as delete

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
]


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
    for directory in directory_list:
        if not os.path.exists(directory):
            print(f"{red}[!] Directory does not exist: {directory}")
            continue # skip if file not found

        for file_name in os.listdir(directory):
            file_path = os.path.join(directory, file_name)
            try:
                now = datetime.now()
                formatted_time = now.strftime("%H:%M:%S")

                # Delete files only
                if os.path.isfile(file_path):
                    delete(file_path)
                    print(f"{b_green}[{d_yellow}{formatted_time}{b_green}] Successfully Removed: {file_path}")

                # Delete empty directories
                elif os.path.isdir(file_path):
                    try:
                        delete(file_path)  # only works if empty
                        print(f"{b_green}[{d_yellow}{formatted_time}{b_green}] Successfully Removed Empty Dir: {file_path}")
                    except OSError:
                        print(f"{b_green}[{d_yellow}{formatted_time}{b_green}] Skipped Non-Empty Dir: {file_path}")

            except Exception as e:
                print(f"{red}[!] Error removing {file_path}: {e}")

    print(f"\n{d_green}[+]{b_green} Cleanup Complete!\n")


def find_nomedia(root_path):
    """Recursively walk through root_path and print all .nomedia files."""
    for dirpath, dirnames, filenames in os.walk(root_path):
        for name in filenames:
            if name == ".nomedia":
                nomedia_path = os.path.join(dirpath, name)
                if nomedia_path not in directory_list():
                    print(f"{b_green}[+] {nomedia_path}")



if __name__ == "__main__":
    # main()
    # detect_directories()
    print(f"Searching for .nomedia under: {SEARCH_ROOT}\n")
    find_nomedia(SEARCH_ROOT)
    print("\nSearch complete.")
