"""

Check Substring

Problem: Check if one string is a substring of another.
    Example:
        Input: "hello world", "world"
        Output: True

Solution:
    I would be try using the sliding window pattern here
    Get the length of the substring ('world') [I am gonna use the len() for this]
    Loop through the string and extract the first word (the word which also have the same size of the substring)
    Check if it is equal to the substring, return True if not increment the loop until all the string has checked,
    If not, return False

"""

def check_substring(s1, s2):
    window_size = len(s2)
    for i in range(len(s1) - window_size + 1):
        window = s1[i:i + window_size]
        if window == s2:
            return True

    return False


print(check_substring("hello world", "world"))
