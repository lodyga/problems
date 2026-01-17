class Solution:
    def deleteAndEarn(self, nums: list[int]) -> int:
        """
        Time complexity: O(2^n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: hash map
            A: brute-force
        """
        num_freq = {}
        for num in nums:
            num_freq[num] = num_freq.get(num, 0) + num
        sorted_nums = sorted(num_freq)

        def dfs(index: int) -> int:
            if index in (len(sorted_nums), len(sorted_nums) + 1):
                return 0

            val = num_freq[sorted_nums[index]]
            skip = dfs(index + 1)
            take = val + dfs(index + 2)
            if (
                index + 1 < len(sorted_nums) and
                sorted_nums[index] + 1 != sorted_nums[index + 1]
            ):
                take = max(take, val + dfs(index + 1))

            return max(skip, take)

        return dfs(0)


class Solution:
    def deleteAndEarn(self, nums: list[int]) -> int:
        """
        Time complexity: O(n + mlogm)
            n: num count
            m: unique num count
        Auxiliary space complexity: O(n)
        Tags:
            DS: array, hash map
            A: top-down
        """
        num_freq = {}
        for num in nums:
            num_freq[num] = num_freq.get(num, 0) + num
        sorted_nums = sorted(num_freq)
        memo = [-1] * (len(sorted_nums) + 2)
        memo[-2] = memo[-1] = 0

        def dfs(index: int) -> int:
            if memo[index] != -1:
                return memo[index]

            val = num_freq[sorted_nums[index]]
            skip = dfs(index + 1)
            take = val + dfs(index + 2)
            if (
                index + 1 < len(sorted_nums) and
                sorted_nums[index] + 1 != sorted_nums[index + 1]
            ):
                take = max(take, val + dfs(index + 1))

            memo[index] = max(skip, take)
            return memo[index]

        return dfs(0)


class Solution:
    def deleteAndEarn(self, nums: list[int]) -> int:
        """
        Time complexity: O(n + mlogm)
            n: num count
            m: unique num count
        Auxiliary space complexity: O(n)
        Tags:
            DS: array, hash map
            A: bottom-up
        """
        num_freq = {}
        for num in nums:
            num_freq[num] = num_freq.get(num, 0) + num
        sorted_nums = sorted(num_freq)
        cache = [0] * (len(sorted_nums) + 2)

        for index in range(len(sorted_nums) - 1, -1, -1):
            val = num_freq[sorted_nums[index]]
            cache[index] = max(cache[index + 1], val + cache[index + 2])
            if (
                index + 1 < len(sorted_nums) and
                sorted_nums[index] + 1 != sorted_nums[index + 1]
            ):
                cache[index] = max(cache[index], val + cache[index + 1])

        return cache[0]


class Solution:
    def deleteAndEarn(self, nums: list[int]) -> int:
        """
        Time complexity: O(n + mlogm)
            n: num count
            m: unique num count
        Auxiliary space complexity: O(m)
        Tags:
            DS: array, hash map
            A: bottom-up
        """
        num_freq = {}
        for num in nums:
            num_freq[num] = num_freq.get(num, 0) + num
        sorted_nums = sorted(num_freq)
        cache = [0] * 2

        for index in range(len(sorted_nums) - 1, -1, -1):
            val = num_freq[sorted_nums[index]]
            cache0 = max(cache[0], val + cache[1])
            if (
                index + 1 < len(sorted_nums) and
                sorted_nums[index] + 1 != sorted_nums[index + 1]
            ):
                cache0 = max(cache0, val + cache[0])
            cache[1] = cache[0]
            cache[0] = cache0

        return cache[0]


print(Solution().deleteAndEarn([1]) == 1)
print(Solution().deleteAndEarn([2, 3]) == 3)
print(Solution().deleteAndEarn([2, 4]) == 6)
print(Solution().deleteAndEarn([3, 4, 2]) == 6)
print(Solution().deleteAndEarn([2, 2, 3, 3, 3, 4]) == 9)
print(Solution().deleteAndEarn([8, 10, 4, 9, 1, 3, 5, 9, 4, 10]) == 37)
print(Solution().deleteAndEarn([1, 1, 1, 2, 4, 5, 5, 5, 6]) == 18)
print(Solution().deleteAndEarn([1, 6, 3, 3, 8, 4, 8, 10, 1, 3]) == 43)
print(Solution().deleteAndEarn([1, 1, 1]) == 3)
print(Solution().deleteAndEarn([12, 32, 93, 17, 100, 72, 40, 71, 37, 92, 58, 34, 29, 78, 11, 84, 77, 90, 92, 35, 12, 5, 27, 92, 91, 23, 65, 91, 85, 14, 42, 28, 80, 85, 38, 71, 62, 82, 66, 3, 33, 33, 55, 60, 48, 78, 63, 11, 20, 51, 78, 42, 37, 21, 100, 13, 60, 57, 91, 53, 49, 15, 45, 19, 51, 2, 96, 22, 32, 2, 46, 62, 58, 11, 29, 6, 74, 38, 70, 97, 4, 22, 76, 19, 1, 90, 63, 55, 64, 44, 90, 51, 36, 16, 65, 95, 64, 59, 53, 93]) == 3451)
