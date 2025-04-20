class Solution:
    def isBalanced(self, root: TreeNode | None) -> bool:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: binary tree, dfs, recursion
        """
        self.is_balanced = True

        def dfs(node):
            if not node or not self.is_balanced:
                return 0

            left_path = dfs(node.left)
            right_path = dfs(node.right)
            if abs(left_path - right_path) > 1:
                self.is_balanced = False
                return 0

            return 1 + max(left_path, right_path)

        dfs(root)
        return self.is_balanced


print(Solution().isBalanced(build_tree([1, 2, 3])), True)
print(Solution().isBalanced(build_tree([3, 9, 20, None, None, 15, 7])), True)
print(Solution().isBalanced(build_tree([1, 2, 2, 3, 3, None, None, 4, 4])), False)
print(Solution().isBalanced(build_tree([1, 2, 2, 3, None, None, 3, 4, None, None, 4])), False)