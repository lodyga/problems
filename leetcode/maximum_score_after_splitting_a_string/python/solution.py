class Solution:
    def maxScore(self, text: str) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            DS: string
            A: iteration
        """
        score = text.count("1")
        res = 0

        for idx in range(len(text) - 1):
            chr = text[idx]
            score += 1 if chr == "0" else -1
            res = max(res, score)

        return res


print(Solution().maxScore("011101") == 5)
print(Solution().maxScore("00111") == 5)
print(Solution().maxScore("1111") == 3)
print(Solution().maxScore("00") == 1)
