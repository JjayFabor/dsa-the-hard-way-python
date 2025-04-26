 # Reverse a String

# Problem: Implement a function to reverse a string manually (no slicing or reversed()).
    # Example:
        # Input: "Hello"
        # Output:  "olleH"

# Solution:
# Create a empty variable and loop through the string and store at the beginning of the empty variable
# so every time it loops it will store the  character at the beginning of the char variable

def reverse_string(s):
    char = ""
    for c in s:
        char = c + char
    return char

print(reverse_string("Hello"))
