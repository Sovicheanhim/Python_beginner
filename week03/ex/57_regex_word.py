import re

def regex_word(number, string):
    regex = r"\b\w{1,"+re.escape(str(number))+r"}\b"
    result = re.sub(regex, '', string)
    return " ".join(result.split())


# print(regex_word(2, "Is it a cat or is it a dog?"))
# print(regex_word(5, "How are you today?"))
# print(regex_word(3, "My name is Kevin."))