from binary_tree_utils import *
from collections import deque


# class TreeNode:
#     """
#     Definition for a binary tree node.
#     """
#     def __init__(self, val=None, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Codec:
    """
    Time complexity: O(n)
    Auxiliary space complexity: O(n)
    Tags:
        DS: binary tree, queue
        A: bfs, iteration, level-order traversal
    """

    def serialize(self, root: TreeNode) -> str:
        """
        Encodes a tree to a single string.
        """
        if root is None:
            return ""

        res = []
        queue = deque([root])

        while queue:
            node = queue.popleft()

            if node:
                res.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                res.append("None")

        while res and res[-1] == "None":
            res.pop()

        return ",".join(res)

    def deserialize(self, data: str) -> TreeNode:
        """
        Decodes your encoded data to tree.
        """
        if data == "":
            return None

        nodes = data.split(",")
        val = nodes[0]
        root = TreeNode(int(val))
        queue = deque([root])
        index = 1

        while index < len(nodes):
            node = queue.popleft()

            val = nodes[index]
            node.left = None if val == "None" else TreeNode(int(val))
            if node.left:
                queue.append(node.left)
            index += 1

            if index == len(nodes):
                break
            val = nodes[index]
            node.right = None if val == "None" else TreeNode(int(val))
            if node.right:
                queue.append(node.right)
            index += 1

        return root


class Codec:
    """
    Time complexity: O(n)
    Auxiliary space complexity: O(n)
    Tags:
        DS: binary tree
        A: dfs, recursion, pre-order traversal
    """

    def serialize(self, root: TreeNode) -> str:
        """
        Encodes a tree to a single string.
        """
        values = []
        
        def dfs(node):
            if node is None:
                values.append("None")
                return
            
            values.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ",".join(values)

    def deserialize(self, data: str) -> TreeNode:
        """
        Decodes your encoded data to tree.
        """
        values = data.split(",")
        index = 0
        
        def dfs():
            nonlocal index
            if values[index] == "None":
                index += 1
                return None

            node: TreeNode = TreeNode(int(values[index]))
            index += 1
            node.left = dfs()
            node.right = dfs()
            return node

        return dfs()


print(get_tree_values(Codec().deserialize(Codec().serialize(build_tree([4])))) == [4])
print(get_tree_values(Codec().deserialize(Codec().serialize(build_tree([4, 5, 6])))) == [4, 5, 6])
print(get_tree_values(Codec().deserialize(Codec().serialize(build_tree([4, 5])))) == [4, 5])
print(get_tree_values(Codec().deserialize(Codec().serialize(build_tree([4, None, 6])))) == [4, None, 6])
print(get_tree_values(Codec().deserialize(Codec().serialize(build_tree([])))) == [])
print(get_tree_values(Codec().deserialize(Codec().serialize(build_tree([1, 2, 3, None, None, 4, 5])))) == [1, 2, 3, None, None, 4, 5])
print(get_tree_values(Codec().deserialize(Codec().serialize(build_tree([1, 2, 3, None, None, 4, 5, 6, 7])))) == [1, 2, 3, None, None, 4, 5, 6, 7])
