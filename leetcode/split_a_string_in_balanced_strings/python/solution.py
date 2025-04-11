class Solution:
    def balancedStringSplit(self, sides: str) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        """
        side_counter = 0
        balanced_string_counter = 0
        
        for side in sides:
            if side == "R":
                side_counter += 1
            else:
                side_counter -= 1
            if not side_counter:
                balanced_string_counter += 1
        
        return balanced_string_counter

print(Solution().balancedStringSplit("RLRRLLRLRL") == 4)
print(Solution().balancedStringSplit("RLRRRLLRLL") == 2)
print(Solution().balancedStringSplit("LLLLRRRR") == 1)
