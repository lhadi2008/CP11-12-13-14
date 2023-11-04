def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[0]
    left = []
    right = []
    
    for element in arr[1:]:
        if element < pivot:
            left.append(element)
        else:
            right.append(element)
    
    return quick_sort(left) + [pivot] + quick_sort(right)

# Sample data
sample_data = [29, 13, 22, 37, 52, 49, 46, 71, 56]

# Sort the sample data using quick sort
sorted_data = quick_sort(sample_data)

print("Sorted result:", sorted_data)
