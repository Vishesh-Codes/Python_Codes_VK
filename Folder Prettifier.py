#----------------------------------------------
# Exercise-8 : Folder Prettifier
#----------------------------------------------
import os

def Folder_Prettifier(path, exceptions, format):
    file_name_counter = 1
    dir_items = os.listdir(path)

    for item in dir_items:
        item_path = os.path.join(path, item)

        if os.path.isfile(item_path) == True:
            item_name = item.split(".")[0]
            item_format = item.split(".")[1]

            os.chdir(current_working_dir)
            with open(exceptions, "r") as file:
                status = file.read().find(item_name)
            
            if status == -1 and item_format != format:
                capitalized_name = f"{item_name.capitalize()}.{item_format}"
                os.chdir("D:/New Folder/")
                os.rename(item, capitalized_name)

            if item_format == format:
                changed_name = f"{file_name_counter}.{item_format}"
                os.chdir("D:/New Folder/")
                os.rename(item, changed_name)
                file_name_counter += 1

# path = input("enter the path: ")
# exceptions = input("provide exceptions: ")
# format = input("file format: ")
path = "D:/New Folder/"
exceptions = "check.txt"
format = "txt"

current_working_dir = os.getcwd()

Folder_Prettifier(path, exceptions, format)

os.chdir(current_working_dir)