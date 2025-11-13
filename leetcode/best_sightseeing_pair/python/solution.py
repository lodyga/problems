class Solution:
    def maxScoreSightseeingPair(self, values: list[int]) -> int:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(1)
        Tags: brute-force
        """
        max_score = 0
        for index, value in enumerate(values):
            for index2 in range(index + 1, len(values)):
                value2 = values[index2]
                score = value + value2 + index - index2
                max_score = max(max_score, score)
        return max_score


class Solution:
    def maxScoreSightseeingPair(self, values: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: greedy
        """
        max_score = 0
        prev_value = values[0] - 1
        for index in range(1, len(values)):
            value = values[index]
            score = value + prev_value
            max_score = max(max_score, score)
            prev_value = max(prev_value - 1, values[index] - 1)
        return max_score


print(Solution().maxScoreSightseeingPair([8, 1, 5, 2, 6]), 11)
print(Solution().maxScoreSightseeingPair([1, 2]), 2)
