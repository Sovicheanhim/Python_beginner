def delete_file(filename):
    import os, shutil
    while 1:
        answer = input("Are you sure you want to delete "+filename+"? [Y/N]")
        if answer == "Y" or answer == "y":
            if os.path.isfile(filename):
                os.remove(filename)
            elif os.path.isdir(filename):
                shutil.rmtree(filename)
            return 1
        elif answer == "N" or answer == "n":
            return 0
        else:
            print("Invalid Option")
            continue


# print(delete_file("folder01"))