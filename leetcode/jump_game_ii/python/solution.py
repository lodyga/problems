class Solution:
    def jump(self, nums: list[int]) -> int:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n)
        Tags:
            DS: array
            A: top-down
        """
        UPPER_BOUND = 10**9 + 7
        N = len(nums)
        memo = [-1] * (N - 1)

        def dfs(idx: int) -> int:
            if idx >= N - 1:
                return 0
            elif memo[idx] != -1:
                return memo[idx]

            res = UPPER_BOUND
            num = nums[idx]

            for jump_idx in range(idx + 1, idx + num + 1):
                res = min(res, 1 + dfs(jump_idx))

            memo[idx] = res
            return res

        return dfs(0)


class Solution:
    def jump(self, nums: list[int]) -> int:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n)
        Tags:
            DS: array
            A: bottom-up
        """
        UPPER_BOUND = 10**9 + 7
        N = len(nums)
        cache = [UPPER_BOUND] * N
        cache[-1] = 0

        for idx in range(N - 2, -1, -1):
            num = nums[idx]
            
            for jump_idx in range(idx + 1, idx + num + 1):
                jump_cache = cache[jump_idx] if jump_idx < N - 1 else 0
                cache[idx] = min(cache[idx], 1 + jump_cache)

        return cache[0]


class Solution:
    def jump(self, nums: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            A: greedy, bfs, iteration, level-order traversal
        """
        N = len(nums)
        res = 0
        left = 0
        next_right = 0
        
        while next_right < N - 1:
            right = next_right

            for idx in range(left, right + 1):
                num = nums[idx]
                next_right = max(next_right, idx + num)

            left = right + 1
            res += 1

        return res


print(Solution().jump([2, 3, 1, 1, 4]) == 2)
print(Solution().jump([2, 3, 0, 1, 4]) == 2)
print(Solution().jump([0]) == 0)
print(Solution().jump([5, 6, 4, 4, 6, 9, 4, 4, 7, 4, 4, 8, 2, 6, 8, 1, 5, 9, 6, 5, 2, 7, 9, 7, 9, 6, 9, 4, 1, 6, 8, 8, 4, 4, 2, 0, 3, 8, 5]) == 5)
