def wood_collected(heights, cut_height):
    total = 0
    for height in heights:
        if height > cut_height:
            total += height - cut_height
    return total

def optimal_cut_height(heights, target):
    left, right = 0, max(heights)
    best_height = 0
    closest_to_target = float('inf')
    
    while left <= right:
        mid = (left + right) // 2
        collected = wood_collected(heights, mid)
        
        if collected >= target:
            waste = collected - target
            if waste < closest_to_target:
                closest_to_target = waste
                best_height = mid
            left = mid + 1  # Try to find a higher height
        else:
            right = mid - 1  # Try to find a lower height
    
    return best_height

# Example usage
tree_heights = [20, 15, 10, 17]
target = 7
print(f"The optimal height to set the machine is: {optimal_cut_height(tree_heights, target)}")
