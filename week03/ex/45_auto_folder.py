def auto_folder(a):
    import os,shutil
    count = 0
    if len(a) == 0:
        return 0
    for foldername in a:
        exist = os.path.isdir(foldername)
        if exist:
            while 1:
                answer = input("Are you sure you want to replace " + foldername + "? [Y/N]")
                if answer == "N" or answer == "n":
                    break
                elif answer == "Y" or answer == "y":
                    shutil.rmtree(foldername)
                    os.mkdir(foldername)
                    break
                else:
                    print("Invalid Option")
                    continue
        else:
            os.mkdir(foldername)
            count += 1
    if count > 1:
        return 1
    else:
        return 0


# print(auto_folder(['hello.txt', 'hello01.txt', 'hello02.txt', 'hello03.txt']))