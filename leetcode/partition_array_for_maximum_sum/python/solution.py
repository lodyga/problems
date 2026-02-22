class Solution:
    def maxSumAfterPartitioning(self, nums: list[int], k: int) -> int:
        """
        Time complexity: O(k*n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: array
            A: top-down
        """
        N = len(nums)
        memo = [-1] * N
        memo.append(0)

        def dfs(left):
            if memo[left] != -1:
                return memo[left]

            max_val = 0
            res = 0

            for right in range(left, min(left + k, N)):
                max_val = max(max_val, nums[right])
                sub_sum = max_val * (right - left + 1)
                res = max(res, sub_sum + dfs(right + 1))

            memo[left] = res
            return res

        return dfs(0)


class Solution:
    def maxSumAfterPartitioning(self, nums: list[int], k: int) -> int:
        """
        Time complexity: O(k*n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: array
            A: bottom-up
        """
        N = len(nums)
        cache = [0] * (N + 1)

        for left in range(N - 1, -1, -1):
            max_val = 0

            for right in range(left, min(left + k, N)):
                max_val = max(max_val, nums[right])
                sub_sum = max_val * (right - left + 1)
                cache[left] = max(cache[left], sub_sum + cache[right + 1])

        return cache[0]


class Solution:
    def maxSumAfterPartitioning(self, nums: list[int], k: int) -> int:
        """
        Time complexity: O(k*n)
        Auxiliary space complexity: O(k)
        Tags:
            DS: array
            A: bottom-up
            Shift cache.
        """
        # cache[i] stores max sum starting from index i
        cache = [0] * k

        for left in range(len(nums) - 1, -1, -1):
            max_val = nums[left]
            next_cache = 0
            
            for right in range(left, min(left + k, len(nums))):
                max_val = max(max_val, nums[right])
                next_cache = max(
                    next_cache,
                    max_val * (right - left + 1) + cache[right - left]
                )
            
            for right in range(k - 1, 0, -1):
                cache[right] = cache[right - 1]
            
            cache[0] = next_cache

        return cache[0]


class Solution:
    def maxSumAfterPartitioning(self, nums: list[int], k: int) -> int:
        from collections import deque
        """
        Time complexity: O(k*n)
        Auxiliary space complexity: O(k)
        Tags:
            DS: array
            A: bottom-up
            Deque.
        """
        # cache[i % k] stores max sum starting from index i
        cache = deque([0] * k)

        for left in range(len(nums) - 1, -1, -1):
            max_val = nums[left]
            next_cache = 0
            
            for right in range(left, min(left + k, len(nums))):
                max_val = max(max_val, nums[right])
                next_cache = max(
                    next_cache,
                    max_val * (right - left + 1) + cache[right - left]
                )
            
            cache.pop()
            cache.appendleft(next_cache)

        return cache[0]


class Solution:
    def maxSumAfterPartitioning(self, nums: list[int], k: int) -> int:
        """
        Time complexity: O(k*n)
        Auxiliary space complexity: O(k)
        Tags:
            DS: array
            A: bottom-up
            Index pointer.
        """
        # cache[i] stores max sum starting from index i
        N = len(nums)
        cache = [0] * k
        start = 0

        for left in range(len(nums) - 1, -1, -1):
            max_val = nums[left]
            next_cache = 0
            
            for right in range(left, min(left + k, N)):
                max_val = max(max_val, nums[right])
                next_cache = max(
                    next_cache,
                    max_val * (right - left + 1) +
                    cache[(right - left + start) % k]
                )
            
            start = (start - 1) % k
            cache[start] = next_cache

        return cache[start]


class Solution:
    def maxSumAfterPartitioning(self, nums: list[int], k: int) -> int:
        """
        Time complexity: O(k*n)
        Auxiliary space complexity: O(k)
        Tags:
            DS: array
            A: bottom-up
            Circular array.
        """
        # cache[i % k] stores max sum starting from index i
        cache = [0] * k

        for left in reversed(range(len(nums))):
            max_val = 0
            next_cache = 0
            
            for right in range(left, min(left + k, len(nums))):
                max_val = max(max_val, nums[right])
                sub_sum = max_val * (right - left + 1)
                next_cache = max(
                    next_cache,
                    sub_sum + cache[(right + 1) % k]
                )
            cache[left % k] = next_cache

        return cache[0]


print(Solution().maxSumAfterPartitioning([1, 15, 7, 9, 2, 5, 10], 3) == 84)
print(Solution().maxSumAfterPartitioning([1, 4, 1, 5, 7, 3, 6, 1, 9, 9, 3], 4) == 83)
print(Solution().maxSumAfterPartitioning([1], 1) == 1)
print(Solution().maxSumAfterPartitioning([20779, 436849, 274670, 543359, 569973, 280711, 252931, 424084, 361618, 430777, 136519, 749292, 933277, 477067, 502755, 695743, 413274, 168693, 368216, 677201, 198089, 927218, 633399, 427645, 317246, 403380, 908594, 854847, 157024, 719715, 336407, 933488, 599856, 948361, 765131, 335089, 522119, 403981, 866323, 519161, 109154, 349141, 764950, 558613, 692211], 26) == 42389649)
