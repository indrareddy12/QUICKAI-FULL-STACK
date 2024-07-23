def find_second_largest_sort(arr):
    # Remove duplicates by converting the list to a set, then back to a list
    unique_arr = list(set(arr))
    # Sort the unique array in descending order
    unique_arr.sort(reverse=True)
    # Return the second element in the sorted list
    if len(unique_arr) < 2:
        return None  # Return None if there is no second largest element
    return unique_arr[1]

# Example usage
arr = [10, 5, 10, 3, 5, 1]
second_largest = find_second_largest_sort(arr)
print(f"The second largest element is: {second_largest}")








def find_second_largest_iter(arr):
    if len(arr) < 2:
        return None  # Return None if there are not enough elements

    first = second = float('-inf')
    for num in arr:
        if num > first:
            second = first
            first = num
        elif first > num > second:
            second = num

    return second if second != float('-inf') else None

# Example usage
arr = [5, 5, 5, 5]
second_largest = find_second_largest_iter(arr)
print(f"The second largest element is: {second_largest}")  # Output: None




def find_second_largest_iter(arr):
    if len(arr) < 2:
        return None  # Return None if there are not enough elements

    first = second = float('-inf')
    for num in arr:
        if num > first:
            second = first  # Preserve the current first as the second largest
            first = num
        elif first > num > second:
            second = num

    return second if second != float('-inf') else None

# Example usage
arr = [10, 5, 10, 3, 5, 1]
second_largest = find_second_largest_iter(arr)
print(f"The second largest element is: {second_largest}")






def find_k_largest_sort(arr, k):
    # Sort the array in descending order
    arr.sort(reverse=True)
    # Return the first k elements
    return arr[:k]

# Example usage
arr = [3, 10, 4, 7, 8, 9]
k = 3
k_largest_elements = find_k_largest_sort(arr, k)
print(f"The {k} largest elements are: {k_largest_elements}")



import heapq

def find_k_largest_heap(arr, k):
    # Initialize a min-heap with the first k elements
    min_heap = arr[:k]
    heapq.heapify(min_heap)  # Convert list to heap in-place

    # Traverse the remaining elements of the array
    for num in arr[k:]:
        if num > min_heap[0]:  # If current element is larger than the smallest element in heap
            heapq.heapreplace(min_heap, num)  # Replace the smallest element
            # Alternatively, you can use heapq.heappushpop(min_heap, num) as well

    # Elements in min_heap are the k largest elements
    return min_heap

# Example usage
arr = [3, 10, 4, 7, 8, 9]
k = 3
k_largest_elements = find_k_largest_heap(arr, k)
print(f"The {k} largest elements are: {k_largest_elements}")
