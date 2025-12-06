class Solution:
    def balancedStringSplit(self, text: str) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            A: iteration
        """
        surplus = 0
        counter = 0
        for letter in text:
            if letter == "R":
                surplus += 1
            else:
                surplus -= 1
            if surplus == 0:
                counter += 1
        return counter


print(Solution().balancedStringSplit("RLRRLLRLRL") == 4)
print(Solution().balancedStringSplit("RLRRRLLRLL") == 2)
print(Solution().balancedStringSplit("LLLLRRRR") == 1)
