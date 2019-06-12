import os

def recursive_folder(string):
    for root, dirs, files, in os.walk(string):
        for name in files:
            if name == "60_recursive_folder.py": continue
            print(os.path.join(root, name))
        for name in dirs:
            if len(os.listdir(name)) == 0 : continue


# recursive_folder(".")