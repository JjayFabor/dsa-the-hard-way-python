"""

Check if a String is a Palindrome

Prroblem:
    Write a function that checks if a string is a palindrome (same forwards and backwards),
    without using string slicing or built-in helpers.

    Example:
        Input: 'hello'
        Output: False
        Input: 'level'
        Output: True

Solution:
    create a function to reverse the string
    Compare the reverse string value and the original string

"""
def reverse_str(s):
    rev_str = ""
    for _ in s:
        rev_str = _ + rev_str
    return rev_str

def is_palindrome(s):
    if  s == reverse_str(s):
        return True
    return False

print(is_palindrome('hello')) # False
print(is_palindrome('level')) # True
