"""

Check if Array is Sorted

Problem: Write a function to check if the array is sorted in non-decreasing order.
    Example:
        Input: [1, 2, 3, 4]
        Output: True

        Input: [1, 3, 2, 4]
        Output: False

Solution:
    Initialize counter
    Use while loop to go through each element of the array comparing to the len(arr) - 1
    Compare the value of first index > second index

"""

def check_sorted_array(arr):
    i = 0
    while i < len(arr) - 1:
        if arr[i] > arr[i + 1]:
            return False
        i += 1
    return True

arr1 = [1,2,3,4]
arr2 = [1,3,2,4]

print(check_sorted_array(arr1))
print(check_sorted_array(arr2))
