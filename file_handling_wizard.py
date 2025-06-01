from pathlib import Path
import tkinter as tk
from tkinter import filedialog
import os
import sys
import shutil
import zipfile
try:
    from tqdm import tqdm
except ImportError:
    print("[ tqdm not found. Installing it now ... ]")
    import subprocess
    subprocess.check_call(["python", "-m", "pip", "install", "tqdm"])
    from tqdm import tqdm




# color & format codes
#----------------------------------------------------------------------------------------------------------------
rst = "\033[0m"
red = "\033[0;31m"
grn = "\033[1;32m"
ylw = "\033[1;33m"
prp = "\u001b[35;1m"
cyn = '\033[36m'

bnk = "\033[5m"
#----------------------------------------------------------------------------------------------------------------




# extra shit
#----------------------------------------------------------------------------------------------------------------
root = tk.Tk()
root.withdraw()

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

folder_to_create = ["Archives", "Images", "Videos", "Audios", "Texts", "Documents", "Executables", "Others"]
#----------------------------------------------------------------------------------------------------------------





# main function
#----------------------------------------------------------------------------------------------------------------
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
2. B U L K   R E N A M I N G
3. B U L K   E X T R A C T I N G

0. E X I T{rst}

          """)
    
    try:
        user_input = int(input(f"{grn}[ Select an option ] >>> {rst}"))
    except:
        input(f"\n\n{red}[ *breaks monitor ]\n\n[ Enter a valid number ... ]{rst}")
        clear_console()
        main()

    match user_input:
        case 1:
            sorting_tool()
        case 2:
            bulk_renaming_tool()
        case 3:
            extract_tool()
        case 0:
            sys.exit()
        case _:
            input(f"\n\n{red}[ Enter a number that represents an option ... ]{rst}")
            clear_console()
            main()
#----------------------------------------------------------------------------------------------------------------





# 1. Sorter
#----------------------------------------------------------------------------------------------------------------
def sorting_tool():
    global counter
    counter = 0
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

    for file in target_path.iterdir():
        if file.is_file():
            sorting_core(file, target_path)
            print(f"[ Sorted: {prp}{file}{rst} ]")
            counter += 1       
        else:
            continue

    print(f"\n\n{grn}[ Sorted {counter} file(s) ]{rst}")
    input(f"{grn}\n--------------------------------\n[ Task completed successfully! ]\n--------------------------------{rst}\n\n{ylw}{cyn}[ Press {ylw}ENTER{cyn} to return ... ]{rst}")

    main()

def folder_creation():

    print(f"\n\n{ylw}{cyn}[ Required sorting folders will be created in the selected directory ]{rst}")

    for folder_ in folder_to_create:
        path = target_path / folder_
        if not (path.exists() and path.is_dir()):
            (path).mkdir(parents=True, exist_ok=True)
            print(f"[ Created folder for {prp}{folder_}{rst} ]")
        else:
            continue
 
    input(f"{grn}[ Missing folders have been created ]\n\n\n{rst}{ylw}{cyn}[ Press {ylw}ENTER{cyn} to start the sorting process ... ]{rst}")
    
    clear_console()

def sorting_core(file_path, target_path):

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
        case ".pdf" | ".csv":
            shutil.move(file_path, target_path / "Documents")
        case ".exe":
            shutil.move(file_path, target_path / "Executables")
        case _:
            shutil.move(file_path, target_path / "Others")
#----------------------------------------------------------------------------------------------------------------





# 2. Bulk name changer
#----------------------------------------------------------------------------------------------------------------
def bulk_renaming_tool():
    index = 1
    counter = 0
    clear_console()

    print(f"""{prp}-------------------------------------------\n
[ This tool renames all files in a folder ]

-------------------------------------------{rst}

""")
    input(f"{ylw}{cyn}[ Press {ylw}ENTER{cyn} to select a folder & rename files inside ... ]{rst}")
    folder = filedialog.askdirectory()
    print(f"{grn}[ Selected folder: {folder} ]{rst}")
    target_path = Path(folder)

    if not folder:
        input(f"{red}[ No folder was selected ]{rst}\n\n\n{ylw}{cyn}[ Press {ylw}ENTER{cyn} to return ... ]{rst}")
        clear_console()
        main()

    new_name = input(f"{ylw}{cyn}\n\n[ What should be the files renamed to? ] >>> {rst}")
    print(f"{grn}[ Files will be renamed to: {new_name}_(index) ]{rst}")
    input(f"\n\n{rst}{ylw}{cyn}[ Press {ylw}ENTER{cyn} to start the renaming process ... ]{rst}")
    
    clear_console()

    print(f"{ylw}{cyn}[ Renaming ... ]{rst}\n")

    for file in target_path.iterdir():
        try:
            if file.is_file():
                old_path = Path(file)
                new_path = old_path.with_name(new_name + "_" + str(index) + old_path.suffix)
                print(f"[ Renamed: {prp}{file}{rst} ]")
                index += 1
                old_path.rename(new_path)
                counter += 1
            else:
                continue
        except:
            input(f"{red}[ Invalid characters found in provided name. Please try again ]{rst}\n\n{ylw}{cyn}[ Press {ylw}ENTER{ylw}{cyn} to return ... ]{rst}")
            main()

    print(f"\n\n{grn}[ Renamed {counter} file(s) ]{rst}")
    input(f"{grn}\n--------------------------------\n[ Task completed successfully! ]\n--------------------------------{rst}\n\n{ylw}{cyn}[ Press {ylw}ENTER{cyn} to return ... ]{rst}")

    main()
#----------------------------------------------------------------------------------------------------------------





# 3. Add to archive & Extract
#----------------------------------------------------------------------------------------------------------------
def extract_tool():
    clear_console()

    print(f"""{prp}-----------------------------------------------\n
[ This tool extracts mutiple archives at once ]

-----------------------------------------------{rst}

""")
    input(f"{ylw}{cyn}[ Press {ylw}ENTER{cyn} to select archive(s) to extract ... ]{rst}")
    files = filedialog.askopenfilenames(filetypes=[("Archives", "*.zip *.tar *.tgz *.tar.gz *.bz2 *.tar.bz2 *.gz *.xz")])
    print(f"{grn}[ Selected file(s) to extract: ]{rst}")
    for file in files:
        print(f"{grn}[ {file} ]{rst}")

    if not files:
        input(f"{red}[ No file(s) was selected ]{rst}\n\n\n{ylw}{cyn}[ Press {ylw}ENTER{cyn} to return ... ]{rst}")
        clear_console()
        main()
    else:
        input(f"\n\n{rst}{ylw}{cyn}[ Press {ylw}ENTER{cyn} to start the extraction process ... ]{rst}")
        extraction_core(files)

def extraction_core(file_paths):
    clear_console()
    print(f"{ylw}{cyn}[ Extracting ... ]{rst}")

    for file in file_paths:
        file_path = Path(file)

        folder_path = file_path.with_suffix("")
        (folder_path).mkdir(parents=True, exist_ok=True)

        with zipfile.ZipFile(file, 'r') as zipFile:
            items_inside = zipFile.infolist()
            print(f"\n[ Extracting: {prp}{file_path.stem}{rst} to {prp}{folder_path}{rst} ]")

            for item_inside in tqdm(items_inside, desc=f"[ Progress  "):
                zipFile.extract(item_inside, path=folder_path)
    
    print(f"\n\n{grn}[ Extracted {len(file_paths)} file(s) ]{rst}")
    input(f"{grn}\n--------------------------------\n[ Task completed successfully! ]\n--------------------------------{rst}\n\n{ylw}{cyn}[ Press {ylw}ENTER{cyn} to return ... ]{rst}")
    
    main()



main()