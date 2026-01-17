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
    def sortedArrayToBST(self, nums: list[int]) -> TreeNode:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: binary tree
            A: dfs, recursion, pre-order traversal
        """
        def dfs(left: int, right: int) -> TreeNode:
            if left == right:
                return TreeNode(nums[left])
            elif left > right:
                return None

            middle = (left + right) >> 1
            node = TreeNode(nums[middle])
            node.left = dfs(left, middle - 1)
            node.right = dfs(middle + 1, right)
            return node

        return dfs(0, len(nums) - 1)


print(is_same_tree(Solution().sortedArrayToBST([5]), build_tree([5])))
print(is_same_tree(Solution().sortedArrayToBST([1, 3]), build_tree([1, None, 3])))
print(is_same_tree(Solution().sortedArrayToBST([-10, -3, 0, 5, 9]), build_tree([0, -10, 5, None, -3, None, 9])))
