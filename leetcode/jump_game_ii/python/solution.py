class Solution:
    def jump(self, nums: list[int]) -> int:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n)
        Tags:
            DS: array
            A: top-down
        """
        upper_bound = len(nums)
        memo = [-1] * len(nums)
        memo[-1] = 0
        
        def dfs(index):
            if index >= len(nums):
                return upper_bound
            elif memo[index] != -1:
                return memo[index]
            
            res = upper_bound
            for start in range(index + 1, index + nums[index] + 1):
                res = min(res, 1 + dfs(start))
            
            memo[index] = res
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
        cache = [len(nums)] * len(nums)
        cache[-1] = 0
        
        for left in range(len(nums) - 2, -1, -1):
            max_jump = min(left + nums[left] + 1, len(nums))
            for right in range(left + 1, max_jump):
                cache[left] = min(cache[left], 1 + cache[right])

        return cache[0]


class Solution:
    def jump(self, nums: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            A: greedy, bfs, iteration, level-order traversal
        """
        jump_counter = 0
        left = 0
        next_right = 0
        
        while next_right < len(nums) - 1:
            right = next_right
            for index in range(left, right + 1):
                next_right = max(next_right, index + nums[index])
            left = right + 1
            jump_counter += 1

        return jump_counter


print(Solution().jump([2, 3, 1, 1, 4]) == 2)
print(Solution().jump([2, 3, 0, 1, 4]) == 2)
print(Solution().jump([0]) == 0)
print(Solution().jump([5, 6, 4, 4, 6, 9, 4, 4, 7, 4, 4, 8, 2, 6, 8, 1, 5, 9, 6, 5, 2, 7, 9, 7, 9, 6, 9, 4, 1, 6, 8, 8, 4, 4, 2, 0, 3, 8, 5]) == 5)
