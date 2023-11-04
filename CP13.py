def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Split the input array into two halves
    middle = len(arr) // 2
    left_half = arr[:middle]
    right_half = arr[middle:]

    # Recursively sort each half
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # Merge the sorted halves back together
    result = []
    i = j = 0

    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            result.append(left_half[i])
            i += 1
        else:
            result.append(right_half[j])
            j += 1

    result.extend(left_half[i:])
    result.extend(right_half[j:])

    return result

# Sample data
data = [29, 13, 22, 37, 52, 49, 46, 71, 56]
sorted_data = merge_sort(data)

print("Sorted Result using Merge Sort:", sorted_data)
