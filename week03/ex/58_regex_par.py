import re

def regex_par(string):
    return re.sub(r"\([^)]*\)", '', string)

# print(regex_par("((not ok)) )ok( )))(not_ok)(((ok"))


