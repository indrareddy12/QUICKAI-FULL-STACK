def numSubarraysWithSum(nums, target):
    def atMost(S):
        if S < 0:
            return 0
        left, right = 0, 0
        current_sum, count = 0, 0

        while right < len(nums):
            current_sum += nums[right]
            
            while current_sum > S:
                current_sum -= nums[left]
                left += 1

            count += right - left + 1
            right += 1

        return count
    
    return atMost(target) - atMost(target - 1)

# Example usage:
nums = [1, 0, 1, 0, 1]
target = 2
print(numSubarraysWithSum(nums, target))  # Output: 4
