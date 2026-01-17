class Solution:
    def rob(self, houses: list[int]) -> int:
        """
        Time complexity: O(2^n)
        Auxiliary space complexity: O(n)
        Tags:
            A: brute-force
        """
        def dfs(index):
            if index in (len(houses), len(houses) + 1):
                return 0

            house = houses[index]
            # skip current house
            sikp = dfs(index + 1)
            # rob current house
            take = house + dfs(index + 2)
            return max(sikp, take)

        return dfs(0)

    def rob(self, houses: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: hash map
            A: top-down
        """
        memo = {
            len(houses): 0,
            len(houses) + 1: 0
        }

        def dfs(index):
            if index in memo:
                return memo[index]

            house = houses[index]
            # skip current house
            sikp = dfs(index + 1)
            # rob current house
            take = house + dfs(index + 2)
            memo[index] = max(sikp, take)
            return memo[index]

        return dfs(0)

    def rob(self, houses: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: array
            A: top-down
        """
        memo = [-1] * (len(houses) + 2)
        memo[-1] = 0
        memo[-2] = 0

        def dfs(index):
            if memo[index] != -1:
                return memo[index]

            house = houses[index]
            # skip current house
            sikp = dfs(index + 1)
            # rob current house
            take = house + dfs(index + 2)
            memo[index] = max(sikp, take)
            return memo[index]

        return dfs(0)


    def rob(self, houses: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: array
            A: bottom-up
        """
        cache = [0] * (len(houses) + 2)

        for index in range(len(houses) - 1, -1, -1):
            house = houses[index]
            skip = cache[index + 1]
            take = house + cache[index + 2]
            cache[index] = max(skip, take)
        return cache[0]

    def rob(self, houses: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            A: bottom-up, rolling cache
        """
        cache = [0, 0]
        N = len(houses)

        for index in range(N - 1, -1, -1):
            house = houses[index]
            index1 = (N - index) % 2
            index2 = (N - 1 - index) % 2
            skip = cache[index2]
            take = house + cache[index1]
            cache[index1] = max(skip, take)
        
        return cache[N % 2]


print(Solution().rob([2]) == 2)
print(Solution().rob([0]) == 0)
print(Solution().rob([2, 1]) == 2)
print(Solution().rob([2, 100, 9, 3, 100]) == 200)
print(Solution().rob([100, 9, 3, 100, 2]) == 200)
print(Solution().rob([1, 2, 3, 1]) == 4)
print(Solution().rob([2, 7, 9, 3, 1]) == 12)
print(Solution().rob([183, 219, 57, 193, 94, 233, 202, 154, 65, 240, 97, 234, 100, 249, 186, 66, 90, 238, 168, 128, 177, 235, 50, 81, 185, 165, 217, 207, 88, 80, 112, 78, 135, 62, 228, 247, 211]) == 3365)
print(Solution().rob([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0)
