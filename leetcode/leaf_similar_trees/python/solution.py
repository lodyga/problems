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
            A: dfs, recursion, pre-order traversal
        """
        def dfs(node, leaves):
            if node is None:
                return
            if node.left is None and node.right is None:
                leaves.append(node.val)
                return

            dfs(node.left, leaves)
            dfs(node.right, leaves)

        leaves1 = []
        dfs(root1, leaves1)
        leaves2 = []
        dfs(root2, leaves2)
        return leaves1 == leaves2


class Solution2:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: binary tree, stack
            A: dfs, iteration, pre-order traversal, generator
        """
        def get_leaves(node):
            # values = []
            stack = []

            while node or stack:
                if node:
                    stack.append(node)
                    node = node.left
                else:
                    node = stack.pop()
                    if node.left is None and node.right is None:
                        # values.append(node.val)
                        yield node.val
                    node = node.right
            yield True

        leaves1 = get_leaves(root1)
        leaves2 = get_leaves(root2)

        while True:
            leaf1 = next(leaves1)
            leaf2 = next(leaves2)
            if leaf1 != leaf2:
                return False
            elif leaf1 is True and leaf2 is True:
                return True


class Solution2:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: binary tree
            A: dfs, recursion, pre-order traversal, generator
        """
        def get_leaves(root):
            def dfs(node):
                if node is None:
                    return
                if node.left is None and node.right is None:
                    yield node.val

                yield from dfs(node.left)
                yield from dfs(node.right)

            yield from dfs(root)

        leaves1 = get_leaves(root1)
        leaves2 = get_leaves(root2)

        gen_stopped = object()
        while True:
            leaf1 = next(leaves1, gen_stopped)
            leaf2 = next(leaves2, gen_stopped)
            if leaf1 is gen_stopped or leaf2 is gen_stopped:
                return leaf1 is leaf2
            if leaf1 != leaf2:
                return False


print(Solution().leafSimilar(build_tree([1, 2]), build_tree([2, 2])) == True)
print(Solution().leafSimilar(build_tree([1, 2, 3]), build_tree([1, 3, 2])) == False)
print(Solution().leafSimilar(build_tree([3, 5, 1, 6, 2, 9, 8, None, None, 7, 4]), build_tree([3, 5, 1, 6, 7, 4, 2, None, None, None, None, None, None, 9, 8])) == True)
print(Solution().leafSimilar(build_tree([3, 5, 1, 6, 7, 4, 2, None, None, None, None, None, None, 9, 11, None, None, 8, 10]), build_tree([3, 5, 1, 6, 2, 9, 8, None, None, 7, 4])) == False)
print(Solution().leafSimilar(build_tree([3, 5, 1, 6, 2, 9, 8, None, None, 7, 4]), build_tree([3, 5, 1, 6, 7, 4, 2, None, None, None, None, None, None, 9, 11, None, None, 8, 10])) == False)
print(Solution().leafSimilar(build_tree([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 8, 9]), build_tree([1, 2, 3, 10, 11, 12, 13])) == False)
