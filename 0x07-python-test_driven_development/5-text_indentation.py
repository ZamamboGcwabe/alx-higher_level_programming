#!/usr/bin/python3
""" A function that prints a text with 2 new lines
after each of these characters: ., ? and :. """

def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    a = 0
    while a < len(text) and text[a] == ' ':
        a  += 1

    while a < len(text):
        print(text[a], end="")
        if text[a] == "\n" or text[a] in ",?:":
            print("\n")
        a += 1
        while a < len(text) and text[a] == ' ':
            a += 1
        continue
    a += 1
