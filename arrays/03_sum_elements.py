"""

Sum of Array Elements

Problem: Manually calculate and return the sum of all elements in an array of integers.

    Example:
        Input: [1, 2, 3, 4]
        Output: 10

Solution:
    Initialize res variable
    Loop the array and add to the sum
    
"""

def sum_array(arr):
    res = 0
    for i in arr:
        res += i
    return res

print(sum_array([1,2,3,4]))
