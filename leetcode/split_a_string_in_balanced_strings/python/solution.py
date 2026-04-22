class Solution:
    def balancedStringSplit(self, text: str) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            A: iteration
        """
        counter = 0
        res = 0

        for char in text:
            counter += 1 if char == "R" else -1
            
            if (counter == 0):
                res += 1

        return res


print(Solution().balancedStringSplit("RLRRLLRLRL") == 4)
print(Solution().balancedStringSplit("RLRRRLLRLL") == 2)
print(Solution().balancedStringSplit("LLLLRRRR") == 1)
