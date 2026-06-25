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
    Time complexity:
        next: Amortized O(1)
        hasNext: O(1)
    Auxiliary space complexity: O(n)
    Tags:
        DS: binary tree
        A: dfs, recursion, pre-order traversal, in-order traversal
    """

    def __init__(self, root: TreeNode) -> None:
        self.root = root
        self.bstInorderGenerator = self._generateBstInorder()
        self.node = next(self.bstInorderGenerator, None)

    def _generateBstInorder(self) -> TreeNode:
        def dfs(node):
            if node is None:
                return

            yield from dfs(node.left)
            yield node
            yield from dfs(node.right)

        yield from dfs(self.root)

    def next(self) -> int:
        node = self.node
        self.node = next(self.bstInorderGenerator, None)
        return node.val

    def hasNext(self) -> bool:
        return self.node is not None


class BSTIterator:
    """
    Time complexity:
        next: Amortized O(1)
        hasNext: O(1)
    Auxiliary space complexity: O(n)
    Tags:
        DS: binary tree
        A: dfs, iteration, pre-order traversal, in-order traversal
    """

    def __init__(self, root: TreeNode):
        self.stack = []
        self._push_left(root)

    def _push_left(self, node: TreeNode) -> None:
        while node:
            self.stack.append(node)
            node = node.left

    def next(self) -> int:
        node = self.stack.pop()
        self._push_left(node.right)
        return node.val

    def hasNext(self) -> bool:
        return len(self.stack) > 0


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


bstIterator = BSTIterator(build_tree([6, 5, 7]))
print(bstIterator.hasNext() is True)
print(bstIterator.next() == 5)
print(bstIterator.hasNext() is True)
print(bstIterator.next() == 6)
print(bstIterator.hasNext() is True)
print(bstIterator.next() == 7)
print(bstIterator.hasNext() is False)


bstIterator = BSTIterator(build_tree([7, 3, 15, None, None, 9, 20]))
print(bstIterator.next() == 3)
print(bstIterator.next() == 7)
print(bstIterator.hasNext() is True)
print(bstIterator.next() == 9)
print(bstIterator.hasNext() is True)
print(bstIterator.next() == 15)
print(bstIterator.hasNext() is True)
print(bstIterator.next() == 20)
print(bstIterator.hasNext() is False)
