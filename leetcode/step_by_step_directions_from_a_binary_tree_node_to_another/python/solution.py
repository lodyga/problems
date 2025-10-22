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
    def getDirections(self, root: TreeNode, start_value: int, dest_value: int) -> str:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: binary tree
        """
        def get_path_to_node2(node, target, path):
            if node is None:
                return
            if node.val == target:
                return path
            
            path.append("L")
            left = get_path_to_node2(node.left, target, path)
            if left:
                return path
            
            path.pop()
            path.append("R")
            right = get_path_to_node2(node.right, target, path)
            if right:
                return right

            path.pop()
            return 

        def get_path_to_node(node, target, path):
            if node is None:
                return
            if node.val == target:
                return []
            
            left = get_path_to_node(node.left, target, path)
            right = get_path_to_node(node.right, target, path)  

            
            if left is not None:
                path.append("L")
                return path
            if right is not None:
                path.append("R")
                return path

        
        path_to_start = get_path_to_node2(root, start_value, [])
        # path_to_start.reverse()
    
        path_to_end = get_path_to_node2(root, dest_value, [])
        # path_to_end.reverse()

        i = 0
        while (
            i < len(path_to_start) and 
            i < len(path_to_end) and 
            path_to_start[i] == path_to_end[i]
        ):
            i += 1

        return "U" * len(path_to_start[i:]) + "".join(path_to_end[i:])


print(Solution().getDirections(build_tree([2, 1, 3]), 1, 3) == "UR")
print(Solution().getDirections(build_tree([2, 1]), 2, 1) == "L")
print(Solution().getDirections(build_tree([5, 1, 2, 3, None, 6, 4]), 3, 6) == "UURL")