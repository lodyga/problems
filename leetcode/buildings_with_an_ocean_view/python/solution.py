class Solution:
    def findBuildings(self, heights: list[int]) -> list[int]:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: list
            A: greedy
        """
        res = [len(heights) - 1]

        for idx in range(len(heights) - 2, - 1, -1):
            height = heights[idx]

            if height > heights[res[-1]]:
                res.append(idx)

        return res[::-1]


class Solution:
    def findBuildings(self, heights: list[int]) -> list[int]:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: monotonic increasing stack
            A: iteration
        """
        stack = []

        for idx, height in enumerate(heights):
            while stack and stack[-1][0] <= height:
                stack.pop()

            stack.append((height, idx))

        return [idx for _, idx in stack]


print(Solution().findBuildings([4]) == [0])
print(Solution().findBuildings([4, 2, 3, 1]) == [0, 2, 3])
print(Solution().findBuildings([4, 3, 2, 1]) == [0, 1, 2, 3])
print(Solution().findBuildings([1, 3, 2, 4]) == [3])
