class Solution:
    def maxScore(self, numbers: str) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        """
        prefix_sum = 0
        postfix_sum = sum(int(number) for number in numbers)
        max_sum = 0

        for number in numbers[:-1]:
            if number == "0":
                prefix_sum += 1
            elif number == "1":
                postfix_sum -= 1
            max_sum = max(max_sum, prefix_sum + postfix_sum)

        return max_sum


print(Solution().maxScore("011101"), 5)
print(Solution().maxScore("00111"), 5)
print(Solution().maxScore("1111"), 3)
print(Solution().maxScore("00"), 1)