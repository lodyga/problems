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
        root = TreeNode(int(nodes[0]))
        queue = deque([root])
        idx = 1

        while idx < len(nodes):
            node = queue.popleft()

            val = nodes[idx]
            
            if val != "None":
                node.left = TreeNode(int(val))
                queue.append(node.left)
            
            idx += 1

            if idx == len(nodes):
                break
            
            val = nodes[idx]
            
            if val != "None": 
                node.right = TreeNode(int(val))
                queue.append(node.right)
            
            idx += 1

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
        def dfs(node: TreeNode):
            if node is None:
                vals.append("None")
                return
            
            vals.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        vals = []
        dfs(root)
        
        return ",".join(vals)

    def deserialize(self, data: str) -> TreeNode:
        """
        Decodes your encoded data to tree.
        """
        vals = data.split(",")
        idx = 0
        
        def dfs():
            nonlocal idx
        
            if vals[idx] == "None":
                idx += 1
                return None

            node = TreeNode(int(vals[idx]))
            idx += 1
            node.left = dfs()
            node.right = dfs()
            return node

        return dfs()


print(get_tree_values(Codec().deserialize(Codec().serialize(build_tree([1, 2, 3, None, None, 4, 5])))) == [1, 2, 3, None, None, 4, 5])
print(get_tree_values(Codec().deserialize(Codec().serialize(build_tree([])))) == [])
print(get_tree_values(Codec().deserialize(Codec().serialize(build_tree([4])))) == [4])
print(get_tree_values(Codec().deserialize(Codec().serialize(build_tree([4, 5, 6])))) == [4, 5, 6])
print(get_tree_values(Codec().deserialize(Codec().serialize(build_tree([4, 5])))) == [4, 5])
print(get_tree_values(Codec().deserialize(Codec().serialize(build_tree([4, None, 6])))) == [4, None, 6])
print(get_tree_values(Codec().deserialize(Codec().serialize(build_tree([1, 2, 3, None, None, 4, 5, 6, 7])))) == [1, 2, 3, None, None, 4, 5, 6, 7])
