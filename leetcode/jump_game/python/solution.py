class Solution:
    def canJump(self, nums: list[int]) -> bool:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            A: greedy
        """
        N = len(nums)
        step = 0

        for idx in range(N - 1):
            num = nums[idx]
            step = max(step - 1, num)

            if step == 0:
                return False

        return True


class Solution:
    def canJump(self, nums: list[int]) -> bool:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n)
        Tags:
            DS: array
            A: top-down
        """
        N = len(nums)
        memo = [-1] * N
        memo[-1] = 1

        def dfs(idx: int) -> int:
            if memo[idx] != -1:
                return memo[idx]

            memo[idx] = 0
            step = min(idx + nums[idx], N - 1)
            
            for jdx in range(idx + 1, step + 1):
                if dfs(jdx):
                    memo[idx] = 1
                    break

            return memo[idx]

        return bool(dfs(0))


class Solution:
    def canJump(self, nums: list[int]) -> bool:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n)
        Tags:
            DS: array
            A: bottom-up
        """
        N = len(nums)
        cache = [False] * N
        cache[-1] = True

        for idx in range(N - 2, -1, -1):
            step = min(idx + nums[idx], N - 1)
            
            for jdx in range(idx + 1, step + 1):
                if cache[jdx]:
                    cache[idx] = True
                    break
        
        return cache[0]


print(Solution().canJump([2, 3, 1, 1, 4]) == True)
print(Solution().canJump([3, 2, 1, 0, 4]) == False)
print(Solution().canJump([0]) == True)
print(Solution().canJump([2, 0, 0]) == True)
print(Solution().canJump([0, 2, 3]) == False)
print(Solution().canJump([1, 0, 1, 0]) == False)
print(Solution().canJump([2, 0, 6, 9, 8, 4, 5, 0, 8, 9, 1, 2, 9, 6, 8, 8, 0, 6, 3, 1, 2, 2, 1, 2, 6, 5, 3, 1, 2, 2, 6, 4, 2, 4, 3, 0, 0, 0, 3, 8, 2, 4, 0, 1, 2, 0, 1, 4, 6, 5, 8, 0, 7, 9, 3, 4, 6, 6, 5, 8, 9, 3, 4, 3, 7, 0, 4, 9, 0, 9, 8, 4, 3, 0, 7, 7, 1, 9, 1, 9, 4, 9, 0, 1, 9, 5, 7, 7, 1, 5, 8, 2, 8, 2, 6, 8, 2, 2, 7, 5, 1, 7, 9, 6]) == False)
