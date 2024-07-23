def sum_of_squares(n):
    total_sum = 0
    while n > 0:
        digit = n % 10
        total_sum += digit ** 2
        n = n // 10
    return total_sum
def is_happy_number(n):
    slow = n
    fast = n

    while True:
        slow = sum_of_squares(slow)  # Move slow one step
        fast = sum_of_squares(sum_of_squares(fast))  # Move fast two steps

        if slow == 1 or fast == 1:
            return True

        if slow == fast:
            return False

# Example usage
print(is_happy_number(19))  # Output: True, because 19 is a happy number
print(is_happy_number(20))  # Output: False, because 20 is not a happy number
