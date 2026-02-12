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
    def getDirections(self, root: TreeNode, start_val: int, dest_val: int) -> str:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: binary tree
            A: DFS with backtracking, post-order traversal
        """
        def get_lca(node: TreeNode) -> TreeNode | None:
            if node is None:
                return None
            elif node.val in (start_val, dest_val):
                return node

            left = get_lca(node.left)
            right = get_lca(node.right)

            if left and right:
                return node
            else:
                return left or right

        def get_path(node: TreeNode, target: int) -> str:

            def backtrack(node: TreeNode, path: list[str]) -> str:
                if node is None:
                    return ""
                elif node.val == target:
                    return "".join(path)

                path.append("L")
                left = backtrack(node.left, path)
                if left:
                    return left

                path.pop()
                path.append("R")
                right = backtrack(node.right, path)
                if right:
                    return right

                path.pop()

            return backtrack(node, [])

        lca = get_lca(root)
        start_path = get_path(lca, start_val)
        dest_path = get_path(lca, dest_val)
        return ("U" * len(start_path)) + dest_path


class Solution:
    def getDirections(self, root: TreeNode, start_value: int, dest_value: int) -> str:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: binary tree
        """
        def get_path(node: TreeNode, target: int, path: list[str]) -> list[str]:
            if node is None:
                return
            if node.val == target:
                return path

            path.append("L")
            left = get_path(node.left, target, path)
            if left:
                return path

            path.pop()
            path.append("R")
            right = get_path(node.right, target, path)
            if right:
                return right

            path.pop()
            return

        start_path = get_path(root, start_value, [])
        dest_path = get_path(root, dest_value, [])

        i = 0
        while (
            i < min(len(start_path), len(dest_path)) and
            start_path[i] == dest_path[i]
        ):
            i += 1

        return "U" * len(start_path[i:]) + "".join(dest_path[i:])


print(Solution().getDirections(build_tree([2, 1, 3]), 1, 3) == "UR")
print(Solution().getDirections(build_tree([2, 1]), 2, 1) == "L")
print(Solution().getDirections(build_tree([5, 1, 2, 3, None, 6, 4]), 3, 6) == "UURL")
