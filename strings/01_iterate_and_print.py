"""

Iterate and print each character in a string

Problem: Write a function that takes a string as input and prints each character on a new line.
    Example:
        Input: "hello"
        Output:
            h
            e
            l
            l
            o

Solution:
    Loop through character and print it

"""


def print_characters(s):
    for char in s:
        print(char)


print_characters("Hello World!")

