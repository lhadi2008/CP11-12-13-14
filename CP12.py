def bubble_sort(arr):
    n = len(arr)
    
    for i in range(n):
        # Flag to check if any swapping occurs in this pass
        swapped = False
        
        # Last i elements are already in place, so no need to check them
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap the elements
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        # If no swapping occurred in this pass, the list is already sorted
        if not swapped:
            break

# Sample data
data = [29, 13, 22, 37, 52, 49, 46, 71, 56]

# Sort the list using bubble sort
bubble_sort(data)

# Print the sorted list
print(data)
