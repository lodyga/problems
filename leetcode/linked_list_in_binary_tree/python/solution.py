from linked_list_utils import *
from binary_tree_utils import *


# class ListNode:
#     """
#     Definition for singly-linked list.
#     """
#     def __init__(self, val=None, next=None):
#         self.val = val
#         self.next = next

# class TreeNode:
#     """
#     Definition for a binary tree node.
#     """
#     def __init__(self, val=None, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        """
        Time complexity: O(n * m)
            n: list size
            m: tree size
        Auxiliary space complexity: O(m)
        Tags: linked list, binary tree, dfs, recursion
        """
        def compare(list_node, tree_node):
            if list_node is None:
                return True
            elif tree_node is None:
                return False
            elif list_node.val != tree_node.val:
                return False
           
            return (
                compare(list_node.next, tree_node.left) or
                compare(list_node.next, tree_node.right)
            )

        if root is None:
            return False
        elif compare(head, root):
            return True

        return (
            self.isSubPath(head, root.left) or
            self.isSubPath(head, root.right)
        )


print(Solution().isSubPath(build_linked_list([1, 2]), build_tree([1, 2, 3])) == True)
print(Solution().isSubPath(build_linked_list([2, 3]), build_tree([1, 2, 4, 3])) == True)
print(Solution().isSubPath(build_linked_list([4, 2, 8]), build_tree([1, 4, 4, None, 2, 2, None, 1, None, 6, 8, None, None, None, None, 1, 3])) == True)
print(Solution().isSubPath(build_linked_list([1, 4, 2, 6]), build_tree([1, 4, 4, None, 2, 2, None, 1, None, 6, 8, None, None, None, None, 1, 3])) == True)
print(Solution().isSubPath(build_linked_list([1, 4, 2, 6, 8]), build_tree([1, 4, 4, None, 2, 2, None, 1, None, 6, 8, None, None, None, None, 1, 3])) == False)
print(Solution().isSubPath(build_linked_list([4, 2]), build_tree([4,4,4,1,None,None,None,2])) == False)