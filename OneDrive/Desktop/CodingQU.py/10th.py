def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

def rotate_array(arr, k):
    n = len(arr)
    k = k % n  # In case the rotation count is greater than the array length

    if k == 0:
        return arr  # No rotation needed

    # Reverse the first part
    reverse(arr, 0,  k - 1)
    # Reverse the second part
    reverse(arr,  k, n - 1)
    # Reverse the whole array
    reverse(arr, 0, n - 1)

    return arr

# Example usage
arr = [1, 2, 3, 4, 5, 6, 7]
k = 3
rotated_arr = rotate_array(arr, k)
print(f'The array after {k} rotations: {rotated_arr}')
