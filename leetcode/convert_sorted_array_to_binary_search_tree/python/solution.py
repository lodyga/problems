class Solution:
    def sortedArrayToBST(self, numbers: list[int]) -> TreeNode:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: binary tree, dfs, recursion
        """
        def dfs(left: int, right: int) -> TreeNode | None:
            if left > right:
                return None
            
            middle = (left + right) // 2

            node = TreeNode(numbers[middle])
            node.left = dfs(left, middle - 1)
            node.right = dfs(middle + 1, right)

            return node

        return get_tree_values(dfs(0, len(numbers) - 1))


print(Solution().sortedArrayToBST([5]) ==  [5])
print(Solution().sortedArrayToBST([1, 3]) in ([1, None, 3], [1, 3]))
print(Solution().sortedArrayToBST([-10, -3, 0, 5, 9]) in ([0, -10, 5, None, -3, None, 9], [0, -3, 9, -10, None, 5]))