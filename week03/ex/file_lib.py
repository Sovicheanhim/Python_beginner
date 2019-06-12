class FileLib:
    def inspect(self):
        import os
        from os import listdir
        from os.path import isfile, join, isdir
        current_path = os.getcwd()
        onlyfiles = [f for f in listdir(current_path) if isfile(join(current_path, f))]
        onlyfolders = [x for x in listdir(current_path) if isdir(join(current_path, x))]
        if len(onlyfolders) == 0 and len(onlyfiles) == 0:
            return []
        else:
            onlyfiles = [(x, 'File') for x in onlyfiles]
            onlyfolders = [(x, 'Folder') for x in onlyfolders]
            result = onlyfiles + onlyfolders
            result.sort(reverse = True, key=lambda x: x[-1])
            return result

    def current_path(self):
        import os
        return os.path.abspath("41_current_path.py")

    def read(self,filename):
        try:
            self.path = filename
            fi = open(self.path, 'r')
            print(fi.read())
            return fi.read()
        except FileNotFoundError:
            return "Invalid FILENAME"
        except SyntaxError:
            return "Invalid FILENAME"
        except OSError:
            return "Invalid FILENAME"

    def write_content(self, filename, content):
        fi = open(filename, "w")
        fi.write(content)
        fi.close()
        return 1

    def write(self, filename, content):
        import os
        exists = os.path.isfile(filename)
        if exists:
            while 1:
                answer = input("Are you sure you want to replace " + filename + "? [Y/N]")
                if answer == "N" or answer == "n":
                    return 0
                elif answer == "Y" or answer == "y":
                    return self.write_content(filename, content)
                else:
                    print("Invalid Option")
                    continue
        else:
            return self.write_content(filename, content)

    def append(self, filename, content):
        fi = open(filename, "a")
        fi.write(content)
        fi.close()
        return 1

    def remove(self, filename):
        import os, shutil
        while 1:
            answer = input("Are you sure you want to delete " + filename + "? [Y/N]")
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

    def create_folder(self, folder_list):
        import os, shutil
        count = 0
        if len(folder_list) == 0:
            return 0
        for foldername in folder_list:
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


p1 = FileLib()
print(p1.inspect())
print(p1.current_path())
print(p1.read("hello.txt"))
print(p1.write("hello.txt", "boy"))
print(p1.append("hello.txt", "Atreus"))
print(p1.remove("hello.txt"))
print(p1.create_folder(["asfds", "dafsdf", "afds"]))