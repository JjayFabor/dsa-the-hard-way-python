"""

Calculate Length of an Array

Problem: Write a function to return the length of an array without using the len() function.

    Example:
        Input: [1, 2, 3, 4]
        Output: 4

Solution:
    Initialize a count variable
    Loop through the array and increment the count

"""

def calculate_length(arr):
    count = 0
    for i in arr:
        count += 1
    return count

print(calculate_length([1,2,3,4]))
