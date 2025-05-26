r"""
preorder: [1, None, 3]
inorder: [None, 1, 3]

        1
    /       \
    None    3

preorder: [3, 9, 20, 15, 7]
inorder: [9, 3, 15, 20, 7]

    3:
9,    15, 20, 7

    9:
        3, 15, 20, 7

    20:
9, 3, 15    7

                    3
                /       \
                9       20
                        /\
                    15      7
"""

class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: binary tree, dfs, recursion, in-order traversal, pre-order traversal
        """
        if not preorder or not inorder:
            return
        
        node = TreeNode(preorder[0])
        pivot = inorder.index(preorder[0])
        node.left = self.buildTree(preorder[1: pivot + 1], inorder[:pivot])
        node.right = self.buildTree(preorder[pivot + 1:], inorder[pivot + 1:])
        return node


print(get_tree_values(Solution().buildTree([1, None, 3], [None, 1, 3])), [1, None, 3])
print(get_tree_values(Solution().buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])), [3, 9, 20, None, None, 15, 7])
print(get_tree_values(Solution().buildTree([-1], [-1])), [-1])