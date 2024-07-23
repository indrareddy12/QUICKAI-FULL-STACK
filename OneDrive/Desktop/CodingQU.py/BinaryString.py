def add_binary_strings(a: str, b: str) -> str:
    # Initialize pointers for both strings and the carry
    i, j, carry = len(a) - 1, len(b) - 1, 0
    result = []
    
    # Loop through both strings from end to beginning
    while i >= 0 or j >= 0 or carry:
        # Sum the bits from both strings and the carry
        sum = carry
        if i >= 0:
            sum += int(a[i])
            i -= 1
        if j >= 0:
            sum += int(b[j])
            j -= 1
        
        # Compute the new carry and the current bit of the result
        carry = sum // 2
        result.append(str(sum % 2))
    
    # Since we've added bits from least significant to most significant, reverse the result
    return ''.join(result[::-1])

# Example usage
a = "1010"
b = "1101"
print(add_binary_strings(a, b))  # Output: "10111"
