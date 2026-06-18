def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                # Swap elements
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


# Example usage
arr = [64, 34, 25, 12, 22, 11, 90]
print("Unsorted array:", arr)

bubble_sort(arr)
print("Sorted array:", arr)