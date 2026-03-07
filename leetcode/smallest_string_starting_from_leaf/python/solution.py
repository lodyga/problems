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
    def smallestFromLeaf(self, root: TreeNode) -> str:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n2)
        Tags:
            DS: binary tree, list
            A: dfs, recursion, pre-order traversal
        """
        paths = []

        def dfs(node: TreeNode, path: str) -> None:
            if node is None:
                return

            letter = chr(node.val + ord("a"))
            path = letter + path

            if node.left is None and node.right is None:
                paths.append(path)
                return

            dfs(node.left, path)
            dfs(node.right, path)

        dfs(root, "")
        return min(paths)


class Solution:
    def smallestFromLeaf(self, root: TreeNode) -> str:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n2)
        Tags:
            DS: binary tree
            A: dfs, recursion, pre-order traversal
        """
        def dfs(node: TreeNode, path: str) -> None:
            if node is None:
                return

            letter = chr(node.val + ord("a"))
            path = letter + path

            if node.left and node.right:
                return min(
                    dfs(node.left, path),
                    dfs(node.right, path)
                )
            elif node.left or node.right:
                return (
                    dfs(node.left, path) or
                    dfs(node.right, path)
                )

            return path

        return dfs(root, "")


class Solution:
    def smallestFromLeaf(self, root: TreeNode) -> str:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n2)
        Tags:
            DS: binary tree
            A: dfs, recursion, pre-order traversal
        """
        def dfs(node: TreeNode, path: str) -> None:
            if node is None:
                return

            letter = chr(node.val + ord("a"))
            path = letter + path

            if node.left and node.right:
                return min(
                    dfs(node.left, path),
                    dfs(node.right, path)
                )
            elif node.left:
                return dfs(node.left, path)
            elif node.right:
                return dfs(node.right, path)

            return path

        return dfs(root, "")


print(Solution().smallestFromLeaf(build_tree([0, 1, 2, 3, 4, 3, 4])) == "dba")
print(Solution().smallestFromLeaf(build_tree([25, 1, 3, 1, 3, 0, 2])) == "adz")
print(Solution().smallestFromLeaf(build_tree([2, 2, 1, None, 1, 0, None, 0])) == "abc")
print(Solution().smallestFromLeaf(build_tree([0, None, 1])) == "ba")
