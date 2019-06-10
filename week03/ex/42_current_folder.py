def current_folder():
    import os
    from os import listdir
    from os.path import isfile, join, isdir
    current_path = os.getcwd()
    onlyfiles = [f for f in listdir(current_path) if isfile(join(current_path, f))]
    onlyfolders = [x for x in listdir(current_path) if isdir(join(current_path, x))]
    if len(onlyfolders) == 0 and len(onlyfiles) == 0:
        return []
    else:
        onlyfiles = [ (x,'File') for x in onlyfiles]
        onlyfolders = [(x,'Folder') for x in onlyfolders]
        result = onlyfiles + onlyfolders
        result.sort( reverse = True, key = lambda x: x[-1])
        return result


# print(current_folder())