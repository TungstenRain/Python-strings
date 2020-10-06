"""
    This module contains code from
    Think Python, 2nd Edition
    by Allen Downey
    http://thinkpython2.com

    This is to test out the turtle module from Chapter 8: Strings in Think Python 2
    
    Note: Although this is saved in a .py file, code was run on an interpreter to get results
    Note: Using Python 3.9.0
"""
def rotate_letter(letter, amount):
    """
        Apply a simple Caesar Cypher by rotating each letter in a word by a user-specified amount

        word: string to rotate
        amount: integer, amount to rotate each letter

        return: a single-letter string rotated
    """
    if letter.isupper():
        start = ord('A')
    elif letter.islower():
        start = ord('a')
    else:
        return letter
    
    c = ord(letter) - start
    i = (c + amount) % 26 + start
    return chr(i)

def rotate_word(word, amount):
    """
        Apply a simple Caesar Cypher by rotating each letter in a word by a user-specified amount

        word: string to rotate
        amount: integer, amount to rotate each letter

        return: string rotated
    """
    res = ''
    for letter in word:
        res += rotate_letter(letter, amount)
    return res

def user_input():
    """
        Request user input to apply a Caesar Cypher to a string
    """
    print("Welcome! Let's apply a Caesar Cypher to a string.\n")
    text = input("Please enter some text: ")
    amount = int(input("Please enter by how much you want it rotated: "))
    print(rotate_word(text, amount))

user_input()