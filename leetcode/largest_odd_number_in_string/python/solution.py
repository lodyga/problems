class Solution:
    def largestOddNumber(self, num: str) -> str:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            A: greedy
        """
        for index in range(len(num) - 1, -1, -1):
            if num[index] in "13579":
                return num[: index + 1]
        return ""


print(Solution().largestOddNumber("52") == "5")
print(Solution().largestOddNumber("35427") == "35427")
