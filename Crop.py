def crop(sentence):
    path = ""
    for letter in sentence:
        if(letter == "/"):
            path = ""
        else:
            path += letter
    return path


print(crop("C:/Users/Thomas/205git"))
