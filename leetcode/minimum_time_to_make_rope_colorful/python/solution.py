class Solution:
    def minCost(self, colors: str, neededTime: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: stack
        """
        stack = []  # [(color, needed_time)]
        time_total = 0

        for color, time in zip(colors, neededTime):
            if stack and stack[-1][0] == color:
                if stack[-1][1] < time:
                    time_total += stack[-1][1]
                    stack.pop()
                else:
                    time_total += time
                    continue

            stack.append((color, time))

        return time_total


class Solution:
    def minCost(self, colors: str, neededTime: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: stack
        """
        stack = None  # (color, needed_time)
        time_total = 0

        for color, time in zip(colors, neededTime):
            if stack and stack[0] == color:
                if stack[1] < time:
                    time_total += stack[1]
                else:
                    time_total += time
                    continue

            stack = (color, time)

        return time_total


print(Solution().minCost("abaac", [1, 2, 3, 4, 5]) == 3)
print(Solution().minCost("abc", [1, 2, 3]) == 0)
print(Solution().minCost("aabaa", [1, 2, 3, 4, 1]) == 2)