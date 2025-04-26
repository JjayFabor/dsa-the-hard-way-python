# Compare Two Strings

# Problem : Write a function that checks if two strings are equal without using ==.

# Solution:
    # Count the len of each string
    # compare and check the index of each to see if they are equal

def compare_strings(s1, s2):
    s1_len = 0
    s2_len = 0

    for _ in s1:
        s1_len += 1

    for _ in s2:
        s2_len += 1

    if  s1_len != s2_len:
        return False

    i = 0
    while i < s1_len:
        if s1[i] != s2[i]:
            return False
        i += 1
    return True


print(compare_strings('hello', 'hello')) # True
print(compare_strings('Hello', 'hello')) # False
