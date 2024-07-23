def check_valid_string(s):
    # Initialize counters for the minimum and maximum possible balance of parentheses
    min_open = 0
    max_open = 0
    
    # Iterate through each character in the string
    for char in s:
        if char == '(':
            # Increment both min_open and max_open for an opening parenthesis
            min_open += 1
            max_open += 1
        elif char == ')':
            # Decrement both min_open and max_open for a closing parenthesis
            min_open -= 1
            max_open -= 1
        else:  # char == '*'
            # Decrement min_open (treat '*' as ')'), increment max_open (treat '*' as '(')
            min_open -= 1
            max_open += 1
        
        # Ensure min_open doesn't drop below 0
        if min_open < 0:
            min_open = 0
        
        # If max_open drops below 0, the string is invalid
        if max_open < 0:
            return False
    
    # If min_open is 0 at the end, the string is valid
    return min_open == 0

# Examples
print(check_valid_string("()"))        # Output: True
print(check_valid_string("(*)"))       # Output: True
print(check_valid_string("(*))"))      # Output: True
print(check_valid_string("((*)"))      # Output: True
print(check_valid_string("(*)("))      # Output: False
print(check_valid_string("(*)))"))     # Output: False
