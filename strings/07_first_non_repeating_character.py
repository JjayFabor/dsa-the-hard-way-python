"""

Find First Non-Repeating Character

Problem:
    Write a function that returns the first character in a string that does not repeat.
    If all characters repeat, return None.

    Example:
        Input: "aabbccdeff"
        Output: 'd'
        Input: "aabbcc"
        Output: None

Solution:
    Create an empty dict to store the counts of each character, then
    Get the first character that the count is equal to 1.

"""

def first_non_repeating_character(s):
    counts = {}

    for char in s:
        found = False
        for key in counts:
            if key == char:
                counts[key] += 1
                found = True
                break
        if not found:
            counts[char] = 1

    for char in s:
        for key in counts:
            if char == key and counts[key] == 1:
                return char

    return None

print(first_non_repeating_character('aabbccdeff'))
print(first_non_repeating_character('ababcc'))
print(first_non_repeating_character('aabbccdde'))
