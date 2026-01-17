class Solution:
    def scoreOfString(self, text: str) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            A: iteration
        """
        score = 0
        for index in range(len(text) - 1):
            score += abs(ord(text[index]) - ord(text[index + 1]))
        return score


class Solution:
    def scoreOfString(self, text: str) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            A: iteration
        """
        return sum(
            abs(ord(text[index]) - ord(text[index + 1]))
            for index in range(len(text) - 1)
        )


print(Solution().scoreOfString("hello") == 13)
print(Solution().scoreOfString("zaz") == 50)
