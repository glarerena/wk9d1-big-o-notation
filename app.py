# // Tech Pathways SU 24

# // Week 9 Day 1

# // This is the file for Big O Notation

# // Time Complexity

# // Need to go over space complexity

# This is where i will do the code for the actual assignment 

# linear search

def linear_search(arr, target):
    for i, value in enumerate(arr):
        if value == target:
            return i
    return -1



# Sample Test Cases
array = [10, 23, 45, 70, 11, 15]
target = 70
print(f"Index of {target}: {linear_search(array, target)}")  # Output: 3

target = 11
print(f"Index of {target}: {linear_search(array, target)}")  # Output: 4

target = 99
print(f"Index of {target}: {linear_search(array, target)}")  # Output: -1

# bubble sort

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


# Sample Test Cases
array = [64, 34, 25, 12, 22, 11, 90]
print(f"Sorted array: {bubble_sort(array)}")  # Output: [11, 12, 22, 25, 34, 64, 90]

array = [5, 1, 4, 2, 8]
print(f"Sorted array: {bubble_sort(array)}")  # Output: [1, 2, 4, 5, 8]
