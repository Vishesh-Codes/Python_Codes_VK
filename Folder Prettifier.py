#----------------------------------------------
# Exercise-8 : Folder Prettifier
#----------------------------------------------
import os
current_working_dir = os.getcwd()

def Folder_Prettifier(path, exceptions, format):
    os.chdir(path)
    file_name_counter = 1
    dir_items = os.listdir(path)

    for item in dir_items:
        item_path = os.path.join(path, item)

        if os.path.isfile(item_path) == True:
            item_name = item.split(".")[0]
            item_format = item.split(".")[1]
            
            with open(exceptions) as file:
                status = file.read().find(item_name)
            
            if status == -1 and item_format != format:
                os.rename(item, item.capitalize())

            if item_format == format:
                os.rename(item, f"{file_name_counter}.{item_format}")
                file_name_counter += 1

# ========================= take input from user =========================
# path = input("enter the path: ")
# exceptions = input("provide exceptions: ")
# format = input("file format: ")

# ========================= example values =========================
path = "D:/New Folder/"
exceptions = r"D:\VK Google Drive\VK__DATA (abcd)\1.     CODING\Programming Language\Python\1. Py Codes\Python course 1\check.txt"
format = "txt"

Folder_Prettifier(path, exceptions, format)
os.chdir(current_working_dir)