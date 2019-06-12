def append_file(filename):
    from datetime import datetime
    fi = open(filename, "a")
    while 1:
        content = input("$: ")
        if content == "EXIT":
            break
        else:
            now = datetime.now()
            fi.write(now.strftime("[%d/%m/%Y %H:%M:%S] ")+content+'\n')
    fi.close()

# print(append_file("hello.txt"))