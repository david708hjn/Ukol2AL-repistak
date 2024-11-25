import numpy as np

# 1.
random_array = np.random.randint(0, 101, 10)
print("Původní pole:", random_array)

# 2.
sorted_array = np.sort(random_array)
print("Seřazené pole (numpy sort):", sorted_array)

# 3.
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
       
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
              
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


bubble_sorted_array = bubble_sort(random_array.copy())
print("Seřazené pole (bubble sort):", bubble_sorted_array)
