"""

Check if Two Strings are Anagrams

Problem: Check if two strings are anagrams (same letters and counts).
    Example:
        Input: "listen", "silent"
        Output: True
        Input: "bat", "man"
        Output: False

Solution:
    Loop through first string and store to an empty list
    Loop through second string and checks if a character is already on the list, if not return False

"""

def check_anagram(s1, s2):
    # Step 1: Loop to the first string and insert into a list
    lst = []

    # I have to use the range() and len() method of python here in order to
    # get the lenght of a string to be used by insertion on a list without
    # using the insert(), append(), etc., list method.
    for i in range(len(s1)):
        lst += [s1[i]]

    # Step 2: Check if s2 characters already in list
    for char in s2:
        if char not in lst:
            return False
        else:
            return True


print(check_anagram('silent', 'listen'))
print(check_anagram('bat', 'man'))
