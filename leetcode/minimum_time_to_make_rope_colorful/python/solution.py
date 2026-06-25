class Solution:
    def minCost(self, colors: str, needed_time: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            A: greedy
        """
        prev_color = ""
        prev_time = 0
        res = 0

        for color, time in zip(colors, needed_time):
            if color == prev_color:
                res += min(prev_time, time)
                prev_time = max(prev_time, time)
            else:
                prev_color = color
                prev_time = time

        return res


print(Solution().minCost("abaac", [1, 2, 3, 4, 5]) == 3)
print(Solution().minCost("abc", [1, 2, 3]) == 0)
print(Solution().minCost("aabaa", [1, 2, 3, 4, 1]) == 2)
print(Solution().minCost("bbbaaa", [4, 9, 3, 8, 8, 9]) == 23)
