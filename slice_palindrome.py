"""
    This module contains code from
    Think Python, 2nd Edition
    by Allen Downey
    http://thinkpython2.com

    This is to test out the turtle module from Chapter 8: Strings in Think Python 2
    
    Note: Although this is saved in a .py file, code was run on an interpreter to get results
    Note: Using Python 3.9.0
"""
def is_palindrome(text):
    """
        Check to see if a string is a palindrome

        return: boolean True or False
    """
    return text == text[::-1]

def user_input():
    """
        Request user input to determine if a string is a palindrome
    """
    print("Welcome! See if a string is a palindrome.\n")
    text = input("Please enter some text: ")
    if is_palindrome(text):
        print("The text you entered: " + text + " is a palindrome!")
    else:
        print("The text you entered: " + text + " is not a palindrome!")

user_input()