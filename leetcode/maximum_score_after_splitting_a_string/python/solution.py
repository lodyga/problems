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
        max_score = 0

        for index in range(len(text) - 1):
            if text[index] == "0":
                score += 1
            else:
                score -= 1
            max_score = max(max_score, score)

        return max_score


print(Solution().maxScore("011101") == 5)
print(Solution().maxScore("00111") == 5)
print(Solution().maxScore("1111") == 3)
print(Solution().maxScore("00") == 1)
