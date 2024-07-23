def left_rotate_manual(arr, d):
    n = len(arr)
    d = d % n
    rotated_arr = arr[d:] + arr[:d]
    return rotated_arr

# Example usage
arr = [1, 2, 3, 4, 5, 6, 7]
rotated_arr = left_rotate_manual(arr, 2)
print(rotated_arr)  # Output: [3, 4, 5, 6, 7, 1, 2]
