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
            num_freq[num] = num_freq.get(num, 0) + 1

        N = len(num_freq)
        sorted_unique_nums = sorted(num_freq)

        def dfs(idx: int) -> int:
            if idx == N:
                return 0

            num = sorted_unique_nums[idx]

            # Next num is greater than this num + 1.
            if (
                idx + 1 == N
                or (idx + 1 < N
                    and num + 1 < sorted_unique_nums[idx + 1])
            ):
                return (num * num_freq[num]) + dfs(idx + 1)

            skip = dfs(idx + 1)
            take = (num * num_freq[num]) + dfs(idx + 2)

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
            num_freq[num] = num_freq.get(num, 0) + 1

        N = len(num_freq)
        sorted_unique_nums = sorted(num_freq)

        memo = [-1] * (N + 2)
        memo[-2] = 0
        memo[-1] = 0

        def dfs(idx: int) -> int:
            if memo[idx] != -1:
                return memo[idx]

            num = sorted_unique_nums[idx]
            val = num * num_freq[num]

            # Next num is greater than this num + 1.
            if (
                idx + 1 < N
                and num + 1 < sorted_unique_nums[idx + 1]
            ):
                memo[idx] = val + dfs(idx + 1)
                return memo[idx]
            
            skip = dfs(idx + 1)
            take = val + dfs(idx + 2)

            memo[idx] = max(skip, take)
            return memo[idx]

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
            num_freq[num] = num_freq.get(num, 0) + 1

        N = len(num_freq)
        sorted_unique_nums = sorted(num_freq)
        cache = [0] * (N + 2)

        for idx in range(len(sorted_unique_nums) - 1, -1, -1):
            num = sorted_unique_nums[idx]
            val = num * num_freq[num]

            if (
                idx + 1 < len(sorted_unique_nums) and
                num + 1 < sorted_unique_nums[idx + 1]
            ):
                cache[idx] = val + cache[idx + 1]
            else:
                cache[idx] = max(
                    cache[idx + 1],
                    val + cache[idx + 2]
                )

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
            num_freq[num] = num_freq.get(num, 0) + 1

        sorted_unique_nums = sorted(num_freq)
        N = len(sorted_unique_nums)
        cache = [0, 0]

        for idx in range(N - 1, -1, -1):
            num = sorted_unique_nums[idx]
            val = num * num_freq[num]

            if (
                idx + 1 < len(sorted_unique_nums) and
                num + 1 < sorted_unique_nums[idx + 1]
            ):
                cache0 = val + cache[0]
            else:
                cache0 = max(cache[0], val + cache[1])

            cache[1] = cache[0]
            cache[0] = cache0

        return cache[0]


print(Solution().deleteAndEarn([3, 4, 2]) == 6)
print(Solution().deleteAndEarn([2, 2, 3, 3, 3, 4]) == 9)
print(Solution().deleteAndEarn([1]) == 1)
print(Solution().deleteAndEarn([2, 3]) == 3)
print(Solution().deleteAndEarn([2, 3]) == 3)
print(Solution().deleteAndEarn([2, 4]) == 6)
print(Solution().deleteAndEarn([8, 10, 4, 9, 1, 3, 5, 9, 4, 10]) == 37)
print(Solution().deleteAndEarn([1, 1, 1, 2, 4, 5, 5, 5, 6]) == 18)
print(Solution().deleteAndEarn([1, 6, 3, 3, 8, 4, 8, 10, 1, 3]) == 43)
print(Solution().deleteAndEarn([1, 1, 1]) == 3)
print(Solution().deleteAndEarn([12, 32, 93, 17, 100, 72, 40, 71, 37, 92, 58, 34, 29, 78, 11, 84, 77, 90, 92, 35, 12, 5, 27, 92, 91, 23, 65, 91, 85, 14, 42, 28, 80, 85, 38, 71, 62, 82, 66, 3, 33, 33, 55, 60, 48, 78, 63, 11, 20, 51, 78, 42, 37, 21, 100, 13, 60, 57, 91, 53, 49, 15, 45, 19, 51, 2, 96, 22, 32, 2, 46, 62, 58, 11, 29, 6, 74, 38, 70, 97, 4, 22, 76, 19, 1, 90, 63, 55, 64, 44, 90, 51, 36, 16, 65, 95, 64, 59, 53, 93]) == 3451)
