def frequency_using_dict(arr):
    freq_dict = {}
    for elem in arr:
        if elem in freq_dict:
            freq_dict[elem] += 1
        else:
            freq_dict[elem] = 1
    return freq_dict

# Example usage
arr = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
print(frequency_using_dict(arr))
