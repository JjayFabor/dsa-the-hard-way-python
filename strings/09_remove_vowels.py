"""

Remove All Vowels from a String

Problem: Remove all vowels (a, e, i, o, u) from the string.
    Example:
        Input: "beautiful"
        Output: "btfl"

Solution:
    Loop through the string
    Check if character is a vowel, do not insert to a new string

"""

def remove_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    new_s = ""

    for char in s:
        if char not in vowels:
            new_s += char

    return new_s


print(remove_vowels("beautiful"))
