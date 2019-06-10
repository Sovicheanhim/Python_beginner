def read_file(path):
    try:
        fi = open(path, 'r')
        print(fi.read())
        return fi.read()
    except FileNotFoundError:
        return "Invalid FILENAME"
    except SyntaxError:
        return "Invalid FILENAME"
    except OSError:
        return "Invalid FILENAME"

# print(read_file(r"C:\Users\Orng\Downloads\Documents\nhimsovichea18\week03\ex\41_current_path.py"))