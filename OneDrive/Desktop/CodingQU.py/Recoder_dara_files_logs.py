import re

def reorder_log_files(logs):
    def is_digit_log(log):
        return log.split()[1].isdigit()
    
    def log_key(log):
        identifier, rest = log.split(" ", 1)
        return (rest, identifier)
    
    digit_logs = [log for log in logs if is_digit_log(log)]
    letter_logs = [log for log in logs if not is_digit_log(log)]
    
    # Sort letter logs based on the log_key
    letter_logs.sort(key=log_key)
    
    # Combine letter logs and digit logs (digit logs retain their order)
    return letter_logs + digit_logs

# Example usage
logs = [
    "log1 123 456",
    "log2 abc def",
    "log3 789 101",
    "log4 ghi jkl"
]

sorted_logs = reorder_log_files(logs)

for log in sorted_logs:
    print(log)
