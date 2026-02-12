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
    def allPossibleFBT(self, n: int) -> list[TreeNode]:
        """
        Time complexity: O(2^n)
        Auxiliary space complexity: O(2^n)
        Tags:
            DS: binray tree, list
            A: backtracking with memo
        """
        memo = {0: [], 1: [TreeNode(0)]}

        def backtrack(n: int) -> list[list[int]]:
            if n in memo:
                return memo[n]

            res = []

            for left in range(n):
                right = n - 1 - left
                left_trees = backtrack(left)
                right_trees = backtrack(right)

                for left_tree in left_trees:
                    for right_tree in right_trees:
                        res.append(TreeNode(0, left_tree, right_tree))

            memo[n] = res
            return res

        return backtrack(n)


print([get_tree_values(root) for root in Solution().allPossibleFBT(1)] == [[0]])
print([get_tree_values(root) for root in Solution().allPossibleFBT(3)] == [[0, 0, 0]])
print([get_tree_values(root) for root in Solution().allPossibleFBT(7)] == [[0, 0, 0, None, None, 0, 0, None, None, 0, 0], [0, 0, 0, None, None, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, None, None, None, None, 0, 0], [0, 0, 0, 0, 0, None, None, 0, 0]])
