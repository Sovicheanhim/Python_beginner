import re

def regex_html(string):
    return re.sub("\<[/\w]*\>", "", string)


# print(regex_html("<<><>>><>"))