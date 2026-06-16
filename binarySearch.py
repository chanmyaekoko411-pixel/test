def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid

        elif arr[mid] > target:
            right = mid - 1

        else:
            left = mid + 1

    return -1


# Example usage
arr = [10, 20, 30, 40, 50]

index = binary_search(arr, 30)

if index != -1:
    print(f"Element found at index {index}")
else:
    print("Element not found")