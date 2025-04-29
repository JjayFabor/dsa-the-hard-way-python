"""

Reverse an Array

Problem: Return a new array that is the reverse of the input. Don’t use slicing or reversed().
    Example:
        Input: [1, 2, 3, 4]
        Output: [4, 3, 2, 1]

Solution:
    Initialize and empty array
    Loop the array and store the num on the empty array one by one
    -- I am gonna use the [] += [num] ( I think this will insert the num at the beginning) x Wrong conclusion, it did not insert at the beginning

    So I just used the same insert at the beginning of a string.
    Quick learning:
        I need to close the num to a [] in order to prepending to the front of the new_arr,
        because num is a single number like 1. Python won't allow this to insert to a new_arr


"""

def reverse_array(arr):
    new_arr = []

    for num in arr:
        new_arr = [num] + new_arr
    return new_arr

arr = [1,2,3,4]
print(reverse_array(arr))
