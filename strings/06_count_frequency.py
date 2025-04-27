"""

Find Frequency of Each Character in a String

Problem:
    Write a function that counts the number of times
    each character appears in a string. Use arrays or nested loops, no collections.Counter.

    Example:
        Input: Hello
        Output: H: 1, e: 1, l: 2, o: 1

Solution:
    Loop through the string
    Store the character on a dictionary with correspending count value that increments

"""

def count_frequency(s):
    res = {}
    for char in s:
        if char in res:
            res[char] += 1
        else:
            res[char] = 1
    return res

print(count_frequency('hello'))

