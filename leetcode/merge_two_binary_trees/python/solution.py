class Solution:
    def mergeTrees(self, root_1: TreeNode, root_2: TreeNode) -> TreeNode:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: binary tree, dfs, recursion
        """
        if not root_1:
            return root_2
        elif not root_2:
            return root_1
        
        root = TreeNode(root_1.val + root_2.val)
        root.left = self.mergeTrees(root_1.left, root_2.left)
        root.right = self.mergeTrees(root_1.right, root_2.right)
        
        return root


class Solution:
    def mergeTrees(self, root_1: TreeNode, root_2: TreeNode) -> TreeNode:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: binary tree, dfs, recursion
        """
        if not root_1 and not root_2:
            return None
        elif not root_1:
            root_1 = TreeNode(0)
        elif not root_2:
            root_2 = TreeNode(0)
        
        root = TreeNode(root_1.val + root_2.val)
        root.left = self.mergeTrees(root_1.left, root_2.left)
        root.right = self.mergeTrees(root_1.right, root_2.right)
        
        return root


print(get_tree_values(Solution().mergeTrees(build_tree([1]), build_tree([1, 2]))) == [2, 2])
print(get_tree_values(Solution().mergeTrees(build_tree([1, 2]), build_tree([1]))) == [2, 2])
print(get_tree_values(Solution().mergeTrees(build_tree([1, 3, 2, 5]), build_tree([2, 1, 3, None, 4, None, 7]))) == [3, 4, 5, 5, 4, None, 7])