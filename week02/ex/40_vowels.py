def vowels(a):
    count = 0
    str_vowels = str()
    str_characters = str()
    for character in a:
        if character == 'a' or character == 'e' or character == 'i' or character == 'o' or character == 'u':
            count += 1
            str_vowels += character
        elif character == 'A' or character == 'E' or character == 'I' or character == 'O' or character == 'U':
            count += 1
            str_vowels += character
        else:
            str_characters += character
            str_characters = str_characters.strip()
    if count > 0:
        print(count)
        print(str_vowels.lower())
        print(str_characters.upper())
        return count
    else:
        print("NO VOWELS")
        return 0
