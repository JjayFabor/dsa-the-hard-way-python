"""

Find Minimum Elemen

Problem: Return the smallest number in an array using iteration (no min()).

    Example:
        Input: [5, 3, 8, 1]
        Output: 1

Solution:
    Set minimum val to the first index
    Loop and compare each val

"""

def find_minimum(arr):
    min_n = arr[0]

    for i in arr:
        if i < min_n:
            min_n = i
    return min_n

print(find_minimum([5,3,8,10]))
