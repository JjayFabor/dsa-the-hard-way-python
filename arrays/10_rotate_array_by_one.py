"""

Rotate Array Elements by One

Problem: Move every element one position to the right, and the last element becomes the first.
    Example:
        Input: [1, 2, 3, 4]
        Output: [4, 1, 2, 3]

Solution:
    Store the last element of the array in a temp var.
    Set a counter which is the len of the array minus 1.
    Use while loop to check if counter is greater than 0,
    then copy the value at index i into index i + 1,
    and set the index 0 to last_element

"""

def rotate_array_by_one(arr):
    last_element = arr[len(arr) - 1]

    i = len(arr) - 1
    while i > 0:
        arr[i] = arr[i - 1]
        i -= 1
    arr[i] = last_element
    return arr


arr = [1,2,3,4]
print(rotate_array_by_one(arr))
