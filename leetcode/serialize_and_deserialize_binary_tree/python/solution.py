from binary_tree_utils import *


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
    Tags: binary tree, dfs, recursion, pre-order traversal
    """

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string."""
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
        """Decodes your encoded data to tree."""
        values = data.split(",")
        self.index = 0
        
        def dfs():
            if values[self.index] == "None":
                self.index += 1
                return None

            node: TreeNode = TreeNode(int(values[self.index]))
            self.index += 1
            node.left = dfs()
            node.right = dfs()
            return node

        return dfs()


tree1 = build_tree([1, 2, 3, None, None, 4, 5])
serial_tree1 = Codec().serialize(tree1)  # "1,2,None,None,3,4,None,None,5,None,None"
deserail_tree1 = Codec().deserialize(serial_tree1)
tree1_values = get_tree_values(deserail_tree1)
# print(tree1_values)
print(get_tree_values(Codec().deserialize(Codec().serialize(build_tree([1, 2, 3, None, None, 4, 5])))) == [1, 2, 3, None, None, 4, 5])
print(get_tree_values(Codec().deserialize(Codec().serialize(build_tree([])))) == [])