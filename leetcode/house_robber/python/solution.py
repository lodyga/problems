class Solution:
    def rob(self, nums: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: array
            A: bottom-up
        """
        N = len(nums)

        if N <= 2:
            return max(nums)

        cache = [0] * N
        cache[0] = nums[0]
        cache[1] = max(nums[0], nums[1])

        for idx in range(2, N):
            num = nums[idx]
            cache[idx] = max(cache[idx - 1], cache[idx - 2] + num)

        return cache[-1]


class Solution:
    def rob(self, nums: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            DS: array
            A: bottom-up
        """
        N = len(nums)

        if (N <= 2):
            return max(nums)

        cache = [nums[0], max(nums[0], nums[1])]

        for idx in range(2, N):
            num = nums[idx]
            (cache[0], cache[1]) = (cache[1], max(cache[1], cache[0] + num))

        return cache[-1]


class Solution:
    def rob(self, nums: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: array
            A: bottom-up
        """
        N = len(nums)
        cache = [0] * (N + 2)

        for idx in range(N - 1, -1, -1):
            num = nums[idx]
            cache[idx] = max(cache[idx + 1], cache[idx + 2] + num)

        return cache[0]


class Solution:
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

        def dfs(idx):
            if memo[idx] != -1:
                return memo[idx]

            house = houses[idx]
            sikp = dfs(idx + 1)
            take = house + dfs(idx + 2)
            
            memo[idx] = max(sikp, take)
            return memo[idx]

        return dfs(0)


print(Solution().rob([2]) == 2)
print(Solution().rob([0]) == 0)
print(Solution().rob([2, 1]) == 2)
print(Solution().rob([2, 100, 9, 3, 100]) == 200)
print(Solution().rob([100, 9, 3, 100, 2]) == 200)
print(Solution().rob([1, 2, 3, 1]) == 4)
print(Solution().rob([2, 7, 9, 3, 1]) == 12)
print(Solution().rob([183, 219, 57, 193, 94, 233, 202, 154, 65, 240, 97, 234, 100, 249, 186, 66, 90, 238, 168, 128, 177, 235, 50, 81, 185, 165, 217, 207, 88, 80, 112, 78, 135, 62, 228, 247, 211]) == 3365)
print(Solution().rob([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0)
