from pathlib import Path
import tkinter as tk
from tkinter import filedialog
import os
import sys
import shutil




# color & format codes
rst = "\033[0m"
red = "\033[0;31m"
grn = "\033[1;32m"
ylw = "\033[1;33m"
prp = "\u001b[35;1m"
cyn = '\033[36m'

bnk = "\033[5m"




# extra shit
root = tk.Tk()
root.withdraw()

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

folder_to_create = ["Archives", "Images", "Videos", "Audios", "Texts", "Documents", "Executables", "Others"]





# main function
def main():

    clear_console()

    print(f"""{grn}
  _____ _ _        _   _                 _ _ _              __        ___                  _ 
 |  ___(_) | ___  | | | | __ _ _ __   __| | (_)_ __   __ _  \ \      / (_)______ _ _ __ __| |
 | |_  | | |/ _ \ | |_| |/ _` | '_ \ / _` | | | '_ \ / _` |  \ \ /\ / /| |_  / _` | '__/ _` |
 |  _| | | |  __/ |  _  | (_| | | | | (_| | | | | | | (_| |   \ V  V / | |/ / (_| | | | (_| |
 |_|   |_|_|\___| |_| |_|\__,_|_| |_|\__,_|_|_|_| |_|\__, |    \_/\_/  |_/___\__,_|_|  \__,_|
                                                     |___/              
                                                                    {bnk}-By BLz{rst}
{grn}---------------------------------------------------------------------------------------------{rst}

{prp}1. S O R T   F I L E S   B Y   T Y P E
0. E X I T{rst}

          """)
    
    try:
        user_input = int(input(f"{grn}[ Select an option ] > {rst}"))
    except:
        input(f"\n\n{red}[ *breaks monitor ]\n\n[ Enter a valid number ... ]{rst}")
        clear_console()
        main()

    match user_input:
        case 1:
            sort_by_type()
        case 0:
            sys.exit()
        case _:
            input(f"\n\n{red}[ Enter a number that represents an option ... ]{rst}")
            clear_console()
            main()





# 1. Sorter
def sort_by_type():

    clear_console()
    print(f"""{prp}-----------------------------------------------------------------------\n
[ This tool sorts files into separate folders depending on their type ]

-----------------------------------------------------------------------{rst}

""")
    input(f"{ylw}{cyn}[ Press {ylw}ENTER{cyn} to select a folder & sort files inside ... ]{rst}")

    folder = filedialog.askdirectory()
    print(f"{grn}[ Selected folder: {folder} ]{rst}")

    if not folder:
        input(f"{red}[ No folder was selected ]{rst}\n\n\n{ylw}{cyn}[ Press {ylw}ENTER{cyn} to return ... ]{rst}")
        clear_console()
        main()

    global target_path
    target_path = Path(folder)

    folder_creation()

    print(f"{ylw}{cyn}[ Sorting... ]{rst}\n")
    for files in target_path.iterdir():
        if files.is_file():
            sorting(files, target_path)
            print(f"[ Sorting: {files} ]")       
        else:
            continue
    
    input(f"{grn}\n--------------------------------\n[ Task completed successfully! ]\n--------------------------------{rst}\n\n{ylw}{cyn}[ Press {ylw}ENTER{cyn} to continue ... ]{rst}")

    main()

def folder_creation():

    print(f"\n\n{ylw}{cyn}[ Required sorting folders will be created in the selected directory ]{rst}")

    for folder_ in folder_to_create:

        (target_path / folder_).mkdir(parents=True, exist_ok=True)
 
    input(f"{grn}[ Missing folders have been created ]\n\n\n{rst}{ylw}{cyn}[ Press {ylw}ENTER{cyn} to start sorting ... ]{rst}")
    clear_console()

def sorting(file_path, target_path):

    match file_path.suffix:
        case ".zip" | ".rar" | ".7z" | ".tar" | ".gz":
            shutil.move(file_path, target_path / "Archives")
        case ".jpg" | ".png" | ".jpeg" | ".gif":
            shutil.move(file_path, target_path / "Images")
        case ".mp4" | ".mov" | ".avi" | ".wmv" | ".mkv":
            shutil.move(file_path, target_path / "Videos")
        case ".mp3" | ".aac" | ".wav" | ".m4a":
            shutil.move(file_path, target_path / "Audios")
        case ".txt" | ".docx" | ".doc" | ".odt":
            shutil.move(file_path, target_path / "Texts")
        case ".pdf" | ".csv" :
            shutil.move(file_path, target_path / "Documents")
        case ".exe":
            shutil.move(file_path, target_path / "Executables")
        case _:
            shutil.move(file_path, target_path / "Others")






main()