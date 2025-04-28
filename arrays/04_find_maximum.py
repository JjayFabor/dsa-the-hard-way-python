"""

Find Maximum  Element

Problem: Return the largest number in an array using iteration and a tracking variable (no max()).

    Example:
        Input: [1, 3, 2, 4]
        Output: 4

Solution:
    Set the maximum to the first index
    Loop through the array and compare each val to the maximum

"""

def find_maximum(arr):
    max_n = arr[0]

    for i in arr:
        if i > max_n:
            max_n = i
    return max_n

print(find_maximum([12,9,3,13]))
