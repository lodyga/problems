from binary_tree_utils import *


# class TreeNode:
#     """
#     Definition for a binary tree node.
#     """
#     def __init__(self, val=None, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def numTrees(self, n: int) -> int:
        """
        Time complexity: O(n2^n)
        Auxiliary space complexity: O(n)
        Tags: brute-force, tle
        """
        def dfs(index):
            if index in (0, 1):
                return 1
            
            level_counter = 0
            for i in range(1, index + 1):
                left = dfs(i - 1)
                right = dfs(index - i)
                level_counter += left * right
            
            return level_counter

        return dfs(n)


class Solution:
    def numTrees(self, n: int) -> int:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n)
        Tags: dp, top-down with memoization as hash map
        """
        memo = {}  # {index: number of unique BSTs with index nodex}
        
        def dfs(index):
            if index in (0, 1):
                return 1
            elif index in memo:
                return memo[index]
            
            level_counter = 0
            for i in range(1, index + 1):
                left = dfs(i - 1)
                right = dfs(index - i)
                level_counter += left * right
            
            memo[index] = level_counter
            return level_counter

        return dfs(n)


class Solution:
    def numTrees(self, n: int) -> int:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n)
        Tags: dp, bottom-up
        """
        # {[index]: number of unique BSTs with index nodex}
        cache = [1] * (n + 1)
        
        for index in range(2, n + 1):
            level_counter = 0
            for i in range(1, index + 1):
                left = cache[i - 1]
                right = cache[index - i]
                level_counter += left * right
            cache[index] = level_counter
        
        return cache[n]


print(Solution().numTrees(1) == 1)  # (0)
print(Solution().numTrees(2) == 2)  # (0, 1)
print(Solution().numTrees(3) == 5)  # (0, 1, 2)
print(Solution().numTrees(19) == 1767263190)