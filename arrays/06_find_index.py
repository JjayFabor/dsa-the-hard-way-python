"""

Find the Index of a Given Element

Problem: Return the first index of a given element in the array. Return -1 if not found.
    Example:
        Input: [1,2,3,4], Target: 3
        Output: 2

Solution:
    Use a counter since we cannot use the enumerate() as this is a python built-in method.
    Loop the arr and keep track the counter
    Then  check if the target is in the array and return the counter,
    If not return -1.

"""

def find_index(arr, target):
    counter = 0
    for num in arr:
        if num == target:
            return counter
        counter += 1


arr = [1,2,3,4]
print(find_index(arr, 3))
