class Solution:
    def diameterOfBinaryTree(self, root: TreeNode | None) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: binary tree, dfs, recursion
        """
        self.diameter = 0

        def dfs(node):
            if not node:
                return 0

            left_path = dfs(node.left)
            right_path = dfs(node.right)
            self.diameter = max(self.diameter, left_path + right_path)

            return 1 + max(left_path, right_path)

        dfs(root)
        return self.diameter


print(Solution().diameterOfBinaryTree(build_tree([])), 0)
print(Solution().diameterOfBinaryTree(build_tree([5])), 0)
print(Solution().diameterOfBinaryTree(build_tree([1, 2])), 1)
print(Solution().diameterOfBinaryTree(build_tree([1, 2, 3])), 2)
print(Solution().diameterOfBinaryTree(build_tree([1, 2, 3, 4, 5])), 3)
