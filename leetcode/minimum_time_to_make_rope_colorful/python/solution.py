class Solution:
    def minCost(self, colors: str, needed_time: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            A: greedy
        """
        prev_color = -1
        max_time = 0
        cost = 0

        for color, time in zip(colors, needed_time):
            if color == prev_color:
                cost += min(max_time, time)
                max_time = max(max_time, time)
            else:
                prev_color = color
                max_time = time

        return cost


print(Solution().minCost("abaac", [1, 2, 3, 4, 5]) == 3)
print(Solution().minCost("abc", [1, 2, 3]) == 0)
print(Solution().minCost("aabaa", [1, 2, 3, 4, 1]) == 2)
print(Solution().minCost("bbbaaa", [4, 9, 3, 8, 8, 9]) == 23)
