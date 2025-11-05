from binary_tree_utils import *


# class TreeNode:
#     """
#     Definition for a binary tree node.
#     """
#     def __init__(self, val=None, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class BSTIterator:
    """
    Time complexity: O(1)
    Auxiliary space complexity: O(n)
    Tags: binary tree, dfs, iteration, stack
    """

    def __init__(self, root: TreeNode):
        self.node_right = root
        self.stack = []

    def next(self) -> int:
        if not self.hasNext():
            return False
        return self._get_next()

    def hasNext(self) -> bool:
        return bool(self.node_right or self.stack)

    def _get_next(self) -> int:
        stack = self.stack
        node_left = self.node_right
        
        while node_left:
            stack.append(node_left)
            node_left = node_left.left
        
        node = stack.pop()
        self.node_right = node.right

        return node.val


class BSTIterator:
    """
    Time complexity: O(1)
    Auxiliary space complexity: O(n)
    Tags: binary tree, dfs, iteration, stack
    """
    def __init__(self, root: TreeNode):
        node = root
        self.stack = []
        
        while node:
            self.stack.append(node)
            node = node.left


    def next(self) -> int:
        node = self.stack.pop()
        val = node.val
        node = node.right
        
        while node:
            self.stack.append(node)
            node = node.left
            
        return val

    def hasNext(self) -> bool:
        return bool(self.stack)


bstIterator = BSTIterator(build_tree([6, 5, 7]))
print(bstIterator.hasNext())  # return True
print(bstIterator.next())  # return 5
print(bstIterator.hasNext())  # return True
print(bstIterator.next())  # return 6
print(bstIterator.hasNext())  # return True
print(bstIterator.next())  # return 7
print(bstIterator.hasNext())  # return False


bstIterator = BSTIterator(build_tree([7, 3, 15, None, None, 9, 20]))
print(bstIterator.next())  # return 3
print(bstIterator.next())  # return 7
print(bstIterator.hasNext())  # return True
print(bstIterator.next())  # return 9
print(bstIterator.hasNext())  # return True
print(bstIterator.next())  # return 15
print(bstIterator.hasNext())  # return True
print(bstIterator.next())  # return 20
print(bstIterator.hasNext())  # return False
