"""

Remove Duplicates from an Array

Problem: Return a new array with duplicates removed, using only basic loops.
    Example:
        Input: [1, 2, 2, 3, 4, 4]
        Output: [1, 2, 3, 4]

Solution:
    Initialize new_arr
    Loop the arr and check if num is in new_arr, if not insert it, else do not insert it

"""

def remove_duplicates(arr):
    new_arr = []

    for num in arr:
        if num not in new_arr:
            new_arr += [num]
    return new_arr

arr = [1,2,2,3,4,4]
print(remove_duplicates(arr))
