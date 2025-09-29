class Solution:
    def rob(self, houses: list[int]) -> int:
        """
        Time complexity: O(2^n)
        Auxiliary space complexity: O(n)
        Tags: brute-force, tle
        """
        def dfs(index):
            if index >= len(houses):
                return 0

            rob_house = houses[index] + dfs(index + 2)
            skip_house = dfs(index + 1)
            return max(rob_house, skip_house)

        return dfs(0)


class Solution:
    def rob(self, houses: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: dp, top-down with memoization as hash map
        """
        memo = {}

        def dfs(index):
            if index >= len(houses):
                return 0
            elif index in memo:
                return memo[index]

            rob_house = houses[index] + dfs(index + 2)
            skip_house = dfs(index + 1)

            memo[index] = max(rob_house, skip_house)
            return memo[index]

        return dfs(0)


class Solution:
    def rob(self, houses: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: dp, top-down with memoization as array
        """
        memo = [-1] * len(houses)

        def dfs(index):
            if index >= len(houses):
                return 0
            elif memo[index] != -1:
                return memo[index]

            rob_house = houses[index] + dfs(index + 2)
            skip_house = dfs(index + 1)

            memo[index] = max(rob_house, skip_house)
            return memo[index]

        return dfs(0)


class Solution:
    def rob(self, houses: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: dp, bottom-up
        """
        cache = [0] * (len(houses) + 2)

        for index in reversed(range(len(houses))):
            rob_house = houses[index] + cache[index + 2]
            skip_house = cache[index + 1]
            cache[index] = max(rob_house, skip_house)

        return cache[0]


class Solution:
    def rob(self, houses: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: dp, bottom-up
        """
        cache = [0, 0]

        for index in reversed(range(len(houses))):
            rob_house = houses[index] + cache[1]
            skip_house = cache[0]
            cache[0], cache[1] = max(rob_house, skip_house), cache[0]

        return cache[0]


print(Solution().rob([2]) == 2)
print(Solution().rob([0]) == 0)
print(Solution().rob([2, 1]) == 2)
print(Solution().rob([2, 100, 9, 3, 100]) == 200)
print(Solution().rob([100, 9, 3, 100, 2]) == 200)
print(Solution().rob([1, 2, 3, 1]) == 4)
print(Solution().rob([2, 7, 9, 3, 1]) == 12)
print(Solution().rob([183, 219, 57, 193, 94, 233, 202, 154, 65, 240, 97, 234, 100, 249, 186, 66, 90, 238, 168, 128, 177, 235, 50, 81, 185, 165, 217, 207, 88, 80, 112, 78, 135, 62, 228, 247, 211]) == 3365)
print(Solution().rob([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0)