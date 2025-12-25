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
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: 
            DS: binary tree
            A: dfs, recursion, pre-order traversal
        """
        def dfs(node):
            if node is None:
                return 0

            total = 0
            if low <= node.val <= high:
                total += node.val
            if low < node.val:
                total += dfs(node.left)
            if high > node.val:
                total += dfs(node.right)

            return total

        return dfs(root)


print(Solution().rangeSumBST(build_tree([10, 5, 15, 3, 7, None, 18]), 7, 15) == 32)
print(Solution().rangeSumBST(build_tree([10, 5, 15, 3, 7, 13, 18, 1, None, 6]), 6, 10) == 23)
print(Solution().rangeSumBST(build_tree([182, 107, 257, 68, 146, 221, 296, 50, 89, 128, 164, 203, 239, 278, 314, 41, 59, 80, 98, 119, 137, 155, 173, 194, 212, 230, 248, 269, 287, 305, 323, 35, 47, 56, 65, 74, 86, 95, 104, 113, 125, 134, 143, 152, 161, 170, 179, 188, 200, 209, 218, 227, 236, 245, 254, 263, 275, 284, 293, 302, 311, 320, 329, 32, 38, 44, None, 53, None, 62, None, 71, 77, 83, None, 92, None, 101, None, 110, 116, 122, None, 131, None, 140, None, 149, None, 158, None, 167, None, 176, None, 185, 191, 197, None, 206, None, 215, None, 224, None, 233, None, 242, None, 251, None, 260, 266, 272, None, 281, None, 290, None, 299, None, 308, None, 317, None, 326]), 86, 224) == 7285)
