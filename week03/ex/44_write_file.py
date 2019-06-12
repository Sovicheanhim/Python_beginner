def write_content(filename, content):
    fi = open(filename, "w")
    fi.write(content)
    fi.close()
    return 1

def write_file(filename, content):
    import os
    exists = os.path.isfile(filename)
    if exists:
        while 1:
            answer = input("Are you sure you want to replace "+filename+"? [Y/N]")
            if answer == "N" or answer == "n":
                return 0
            elif answer == "Y" or answer == "y":
                return write_content(filename, content)
            else:
                print("Invalid Option")
                continue
    else:
        return write_content(filename, content)



# print(write_file("hello.txt","boy"))