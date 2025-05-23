class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> bool:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: binary tree, dfs, recursion, in-order traversal
        """
        numbers = []

        def dfs(node):
            if not node:
                return
        
            dfs(node.left)

            numbers.append(node.val)
            if len(numbers) == k:
                return

            dfs(node.right)

        dfs(root)
        return numbers[k - 1]


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> bool:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: binary tree, dfs, iteration, stack, in-order traversal
        """
        values = []
        stack = []
        node = root

        while node or stack:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                values.append(node.val)
                if len(values) == k:
                    return values[-1]
                node = node.right
                

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> bool:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: binary tree, dfs, recursion, brute-force
        """
        numbers = []
        heapq.heapify(numbers)

        def dfs(node):
            if not node:
                return
            
            if len(numbers) < k:
                heapq.heappush(numbers, -node.val)
            else:
                heapq.heappushpop(numbers, -node.val)

            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return -heapq.heappop(numbers)


print(Solution().kthSmallest(build_tree([1]), 1) == 1)
print(Solution().kthSmallest(build_tree([2, 1, 3]), 1) == 1)
print(Solution().kthSmallest(build_tree([5, 3, 6, 2, 4, None, None, 1]), 3) == 3)
print(Solution().kthSmallest(build_tree([5, 3, 7, 2, 4, None, 8]), 3) == 4)
print(Solution().kthSmallest(build_tree([3, 1, 4, None, 2]), 1) == 1)
print(Solution().kthSmallest(build_tree([41, 37, 44, 24, 39, 42, 48, 1, 35, 38, 40, None, 43, 46, 49, 0, 2, 30, 36, None, None, None, None, None, None, 45, 47, None, None, None, None, None, 4, 29, 32, None, None, None, None, None, None, 3, 9, 26, None, 31, 34, None, None, 7, 11, 25, 27, None, None, 33, None, 6, 8, 10, 16, None, None, None, 28, None, None, 5, None, None, None, None, None, 15, 19, None, None, None, None, 12, None, 18, 20, None, 13, 17, None, None, 22, None, 14, None, None, 21, 23]), 25) == 24)