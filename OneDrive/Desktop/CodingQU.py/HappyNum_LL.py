def sum_of_squares(n):
    total = 0
    while n > 0:
        digit = n % 10
        total += digit * digit
        n = n // 10
    return total

def is_happy_number(n):
    slow = n
    fast = sum_of_squares(n)
    
    while fast != 1 and slow != fast:
        slow = sum_of_squares(slow)
        fast = sum_of_squares(sum_of_squares(fast))
    
    return fast == 1

# Example Usage
number = 19
if is_happy_number(number):
    print(f"{number} is a happy number!")
else:
    print(f"{number} is not a happy number.")

number = 2
if is_happy_number(number):
    print(f"{number} is a happy number!")
else:
    print(f"{number} is not a happy number.")
