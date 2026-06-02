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
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: binary tree
            A: dfs, recursion, pre-order traversal, generator
        """
        def generate_leaf(node: TreeNode) -> TreeNode:
            if node is None:
                return
            elif node.left is None and node.right is None:
                yield node

            yield from generate_leaf(node.left)
            yield from generate_leaf(node.right)

        leaf1_generator = generate_leaf(root1)
        leaf2_generator = generate_leaf(root2)

        while True:
            leaf1 = next(leaf1_generator, None)
            leaf2 = next(leaf2_generator, None)

            if leaf1 is None or leaf2 is None:
                return leaf1 is leaf2
            elif leaf1.val != leaf2.val:
                return False


class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: binary tree
            A: dfs, recursion, pre-order traversal
        """
        def dfs(node: TreeNode, values :list) -> None:
            if node is None:
                return
            elif node.left is None and node.right is None:
                values.append(node.val)

            dfs(node.left, values)
            dfs(node.right, values)

        values1 = []
        values2 = []
        
        dfs(root1, values1)
        dfs(root2, values2)

        return values1 == values2


print(Solution().leafSimilar(build_tree([1, 2]), build_tree([2, 2])) == True)
print(Solution().leafSimilar(build_tree([1, 2, 3]), build_tree([1, 3, 2])) == False)
print(Solution().leafSimilar(build_tree([3, 5, 1, 6, 2, 9, 8, None, None, 7, 4]), build_tree([3, 5, 1, 6, 7, 4, 2, None, None, None, None, None, None, 9, 8])) == True)
print(Solution().leafSimilar(build_tree([3, 5, 1, 6, 7, 4, 2, None, None, None, None, None, None, 9, 11, None, None, 8, 10]), build_tree([3, 5, 1, 6, 2, 9, 8, None, None, 7, 4])) == False)
print(Solution().leafSimilar(build_tree([3, 5, 1, 6, 2, 9, 8, None, None, 7, 4]), build_tree([3, 5, 1, 6, 7, 4, 2, None, None, None, None, None, None, 9, 11, None, None, 8, 10])) == False)
print(Solution().leafSimilar(build_tree([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 8, 9]), build_tree([1, 2, 3, 10, 11, 12, 13])) == False)
