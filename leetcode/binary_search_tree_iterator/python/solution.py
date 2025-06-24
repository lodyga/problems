class BSTIterator:
    """
    Time complexity: O(1)
    Auxiliary space complexity: O(n)
    Tags: binary tree, dfs, iteration, stack
    """
    def __init__(self, root: TreeNode):
        self.node = root
        self.stack = []

    def next(self) -> int:
        node = self.node
        stack = self.stack
        
        while node:
            stack.append(node)
            node = node.left
            
        node = stack.pop()
        self.node = node.right
        
        return node.val

    def hasNext(self) -> bool:
        return bool(self.node or self.stack)


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


bstIterator = BSTIterator(build_tree([5, 6, 7]))
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