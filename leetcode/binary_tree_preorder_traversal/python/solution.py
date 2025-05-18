class Solution:
    def preorderTraversal(self, root: TreeNode | None) -> list[int]:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: binary tree, dfs, recursion
        """
        node_list = []

        def dfs(node):
            if not node:
                return
        
            node_list.append(node.val)
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return node_list


class Solution:
    def preorderTraversal(self, root: TreeNode) -> list[int]:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: binary tree, dfs, iteration, stack
        """
        node_list = []
        stack = []
        node = root

        while node or stack:
            if node:
                node_list.append(node.val)
                stack.append(node.right)
                node = node.left
            else:
                # Backtrack to the last right child
                node = stack.pop()

        return node_list


class Solution:
    def preorderTraversal(self, root: TreeNode) -> list[int]:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: binary tree, dfs, iteration, stack
        """
        if not root:
            return []

        node_list = []
        stack = [root]

        while stack:
            for _ in stack:
                node = stack.pop()
                node_list.append(node.val)

                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)

        return node_list


print(Solution().preorderTraversal(build_tree([])), [])
print(Solution().preorderTraversal(build_tree([1])), [1])
print(Solution().preorderTraversal(build_tree([1, None, 2, 3])), [1, 2, 3])
print(Solution().preorderTraversal(build_tree([1, 2, 3, 4, 5, None, 8, None, None, 6, 7, 9])), [1, 2, 4, 5, 6, 7, 3, 8, 9])