import re
def regex_alpha(string):
    if string == "":
        return False
    search = re.search(r"^([\w]+)$", string)
    for character in string:
        if search:
            continue
        else:
            return False
    return True

# print(regex_alpha("abafsd21321f$%$%"))