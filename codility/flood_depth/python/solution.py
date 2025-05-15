def flood_depth(heights: int) -> int:
    """
    Time complexity: O(n)
    Auxiliary space complexity: O(1)
    Tags: two pointers
    """
    max_depth = 0
    left = 0
    right = len(heights) - 1
    left_wall = heights[0]
    right_wall = heights[right]

    while left < right:
        left_height = heights[left]
        right_height = heights[right]
        
        if left_height < right_height:
            left_wall = max(left_wall, left_height)
            depth = left_wall - left_height
            max_depth = max(max_depth, depth)
            left += 1
        else:
            right_wall = max(right_wall, right_height)
            depth = right_wall - right_height
            max_depth = max(max_depth, depth)
            right -= 1
    
    return max_depth


print(flood_depth([1, 3, 2, 1, 2, 1, 5, 3, 3, 4, 2]) == 2)
print(flood_depth([5, 8]) == 0)
print(flood_depth([3, 1, 2]) == 1)
print(flood_depth([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 2)