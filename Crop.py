# Thomas Lopes
# 05/12/2018
# This code takes a full path and return the filename

def crop(sentence):
    path = ""
    for letter in sentence:
        if(letter == "/"):
            path = ""
        else:
            path += letter
    return path


print(crop("C:/Users/Thomas/205git"))
