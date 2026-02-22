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
    def countPairs(self, root: TreeNode, distance: int) -> int:
        """
        Time complexity: O(n*d2)
            n: node count
            d: distance
        Auxiliary space complexity: O(n)
        Tags:
            DS: binary tree
            A: dfs, recursion, post-order traversal
        """
        counter = 0

        def dfs(node):
            nonlocal counter
            if node is None:
                return []
            elif node.left is None and node.right is None:
                return [1]

            left = dfs(node.left)
            right = dfs(node.right)

            for l in left:
                for r in right:
                    if l + r <= distance:
                        counter += 1

            return [val + 1 for val in left + right if val + 2 <= distance]

        dfs(root)
        return counter


print(Solution().countPairs(build_tree([1]), 1) == 0)
print(Solution().countPairs(build_tree([1, 2, 3]), 2) == 1)
print(Solution().countPairs(build_tree([1, 2]), 1) == 0)
print(Solution().countPairs(build_tree([1, 2, 3, None, 4]), 3) == 1)
print(Solution().countPairs(build_tree([1, 2, 3, 4, 5, 6, 7]), 3) == 2)
print(Solution().countPairs(build_tree([7, 1, 4, 6, None, 5, 3, None, None, None, None, None, 2]), 3) == 1)
