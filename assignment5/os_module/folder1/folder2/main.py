import os

def open_folder(path, folder_name):
    new_path = os.path.join(path, folder_name)
    return os.path.abspath(new_path)

def move_to_parent_folder(path):
    new_path = os.path.join(path, "..")
    return os.path.abspath(new_path)

def display_files_and_folders(path):
    contents = os.listdir(path)
    print(f"Below are the Files and Folders of Path {path}")
    print(contents)

cwd = os.getcwd()
print(cwd)
child = open_folder(cwd, "folder3")
display_files_and_folders(child)

parent = move_to_parent_folder(cwd)
display_files_and_folders(parent)