"""

Count characters in a string

Problem: Write a function that takes a string as input and returns the number of characters in the string.
    Example:
        Input: "hello"
        Output: 5

Solution:
    Loop throught a string and increment the variable 'count' and return/print it

"""


def count_characters(s):
    count = 0
    for char in s:
        count += 1
    return count

print(count_characters("Hello World!"))
