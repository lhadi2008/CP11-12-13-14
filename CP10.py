def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return False

# Test cases
arr1 = [[1,2,3,5,8], 6]
target1 = 6
result1 = binary_search(arr1, target1)
print(result1)  # Output: False

arr2 = [[1,2,3,5,8], 5]
target2 = 5
result2 = binary_search(arr2, target2)
print(result2)  # Output: True
