#!/usr/bin/python3
def uppercase(txt):
    for letter in txt:
        new_letter = letter
        if ord(letter) >= 97 and ord(letter) <= 122:
            new_letter = chr(ord(letter) - 32)
        print("{}".format(new_letter), end="")
    print("")
