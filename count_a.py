"""
    This module contains code from
    Think Python, 2nd Edition
    by Allen Downey
    http://thinkpython2.com

    This is to test out the turtle module from Chapter 8: Strings in Think Python 2
    
    Note: Although this is saved in a .py file, code was run on an interpreter to get results
    Note: Using Python 3.9.0
"""
def count_a(input):
    """
        Count the number of letter 'a' in a string

        return: the number of letter 'a'
    """
    return input.count("a")
    
def user_input():
    """
        Request user input to count the number of letter 'a' in a string
    """
    print("Welcome to trying out counting the number of 'a's in a string.\n")
    text = input("Please enter some text: ")
    num_of_a = count_a(text)
    print("There are " + str(num_of_a) + " letter 'a's in the string: " + text)

user_input()