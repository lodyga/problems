import binary_tree_utils as bt


# class TreeNode:
#     """
#     Definition for a binary tree node.
#     """
#     def __init__(self, val=None, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def countPairs(self, root: bt.TreeNode, distance: int) -> int:
        """
        Time complexity: O(n*d2)
            n: node count
            d: distance
        Auxiliary space complexity: O(n)
        Tags: binary tree, dfs, recursion, post-order traversal
        """
        self.pairs = 0

        def dfs(node):
            if node is None:
                return []
            if node.left is None and node.right is None:
                return [1]

            left = dfs(node.left)
            right = dfs(node.right)

            self.pairs += sum(True for l in left for r in right if l + r <= distance)
            
            return [value + 1 for value in left + right if value + 1 < distance]
        
        dfs(root)
        return self.pairs


    def countPairs(self, root: bt.TreeNode, distance: int) -> int:
        """
        Time complexity: O(n*d2)
            n: node count
            d: distance
        Auxiliary space complexity: O(n)
        Tags: binary tree, dfs, recursion, post-order traversal
        """
        def dfs(node):
            if node is None:
                return ([], 0)
            if node.left is None and node.right is None:
                return ([1], 0)

            left_leafs, left_pairs_counter = dfs(node.left)
            right_leafs, right_pairs_counter = dfs(node.right)

            leaf_distances = [value + 1 for value in left_leafs + right_leafs if value + 1 < distance]

            node_pairs_counter = sum(True for l in left_leafs for r in right_leafs if l + r <= distance)
            total_pairs_counter = left_pairs_counter + right_pairs_counter + node_pairs_counter
            
            return (leaf_distances, total_pairs_counter)
        
        return dfs(root)[1]


print(Solution().countPairs(bt.build_tree([1]), 1) == 0)
print(Solution().countPairs(bt.build_tree([1, 2, 3]), 2) == 1)
print(Solution().countPairs(bt.build_tree([1, 2, 3]), 2) == 1)
print(Solution().countPairs(bt.build_tree([1, 2]), 1) == 0)
print(Solution().countPairs(bt.build_tree([1, 2, 3, None, 4]), 3) == 1)
print(Solution().countPairs(bt.build_tree([1, 2, 3, 4, 5, 6, 7]), 3) == 2)
print(Solution().countPairs(bt.build_tree([7, 1, 4, 6, None, 5, 3, None, None, None, None, None, 2]), 3) == 1)