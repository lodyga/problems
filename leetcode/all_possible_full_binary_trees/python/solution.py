from binary_tree_utils import *


class Solution:
    def allPossibleFBT(self, n: int) -> list[TreeNode]:
        """
        Time complexity: O(2^n)
        Auxiliary space complexity: O(2^n)
        Tags: binary tree
        """
        def dfs(index):
            if index % 2 == 0:
                return []
            elif index == 1:
                return [TreeNode(0)]
            
            tree_list = []

            for left in range(index):
                right = index - 1 - left

                for left_tree in dfs(left):
                    for right_tree in dfs(right):
                        tree_list.append(TreeNode(0, left_tree, right_tree))

            return tree_list
            
        return dfs(n)
        

print(Solution().allPossibleFBT(0))
print(Solution().allPossibleFBT(1))
print(Solution().allPossibleFBT(3))
print(Solution().allPossibleFBT(5))
print(Solution().allPossibleFBT(7))