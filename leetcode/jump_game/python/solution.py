class Solution:
    def canJump(self, nums: list[int]) -> bool:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n)
        Tags:
            DS: array
            A: top-down
        """
        memo = [None] * len(nums)
        memo[-1] = True

        def dfs(index: int) -> bool:
            if memo[index] is not None:
                return memo[index]

            memo[index] = False
            max_jump = min(index + nums[index], len(nums) - 1)
            for i2 in range(max_jump, index, -1):
                if dfs(i2):
                    memo[index] = True
                    break

            return memo[index]

        return dfs(0)


class Solution:
    def canJump(self, nums: list[int]) -> bool:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n)
        Tags:
            DS: array
            A: bottom-up
        """
        cache = [False] * len(nums)
        cache[-1] = True

        for index in range(len(nums) - 2, -1, -1):
            max_jump = min(index + nums[index], len(nums) - 1)
            for i2 in range(max_jump, index, -1):
                if cache[i2]:
                    cache[index] = True
                    break
        
        return cache[0]


class Solution:
    def canJump(self, nums: list[int]) -> bool:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            A: greedy
        """
        max_jump = 1
        for index in range(len(nums) - 1):
            max_jump = max(max_jump - 1, nums[index])
            if max_jump == 0:
                return False

        return True


print(Solution().canJump([2, 3, 1, 1, 4]) == True)
print(Solution().canJump([3, 2, 1, 0, 4]) == False)
print(Solution().canJump([0]) == True)
print(Solution().canJump([2, 0, 0]) == True)
print(Solution().canJump([0, 2, 3]) == False)
print(Solution().canJump([1, 0, 1, 0]) == False)
print(Solution().canJump([2, 0, 6, 9, 8, 4, 5, 0, 8, 9, 1, 2, 9, 6, 8, 8, 0, 6, 3, 1, 2, 2, 1, 2, 6, 5, 3, 1, 2, 2, 6, 4, 2, 4, 3, 0, 0, 0, 3, 8, 2, 4, 0, 1, 2, 0, 1, 4, 6, 5, 8, 0, 7, 9, 3, 4, 6, 6, 5, 8, 9, 3, 4, 3, 7, 0, 4, 9, 0, 9, 8, 4, 3, 0, 7, 7, 1, 9, 1, 9, 4, 9, 0, 1, 9, 5, 7, 7, 1, 5, 8, 2, 8, 2, 6, 8, 2, 2, 7, 5, 1, 7, 9, 6]) == False)
