def linear_search(data, target):
    """
    Perform a linear search for the target element.

    Returns the index if found, otherwise -1.
    """
    for i in range(len(data)):
        if data[i] == target:
            return i  # Return index if element is found

    return -1  # Element not found


# List of elements
numbers = [10, 25, 36, 47, 58, 69, 80]

# Taking user input for the search element
target = int(input("Enter number to search: "))

# Calling the function
result = linear_search(numbers, target)

# Displaying the result
if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")