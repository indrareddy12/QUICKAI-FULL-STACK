# Maximum sum of the subarray by using SlidingWindow tech.

def max_sum_subarray(arr, k):
    n = len(arr)
    if n < k:
        return "Invalid input"

    # Calculate the sum of the first window
    window_sum = sum(arr[:k])
    max_sum = window_sum

    # Slide the window from start to end in the array
    for i in range(n - k):
        window_sum = window_sum - arr[i] + arr[i + k]
        max_sum = max(max_sum, window_sum)

    return max_sum

# Example usage
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
k = 3
print(f"The maximum sum of a subarray of size {k} is: {max_sum_subarray(arr, k)}")



#largest substring of k distinct characters by using SlidingWindow tech.

def longest_substring_k_distinct(s, k):
    n = len(s)
    if n == 0 or k == 0:
        return 0

    left = 0
    right = 0
    max_length = 0
    char_count = {}

    while right < n:
        # Add the character at the right pointer to the window
        char_count[s[right]] = char_count.get(s[right], 0) + 1

        # Shrink the window from the left if more than k distinct characters
        while len(char_count) > k:
            char_count[s[left]] -= 1
            if char_count[s[left]] == 0:
                del char_count[s[left]]
            left += 1

        # Update the maximum length of the substring
        max_length = max(max_length, right - left + 1)

        # Move the right pointer to the right
        right += 1

    return max_length

# Example usage
s = "eceba"
k = 2
print(f"The length of the longest substring with {k} distinct characters is: {longest_substring_k_distinct(s, k)}")
