class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: binary tree, dfs, recursion
        pure function
        """
        def dfs(node, max_val):
            if not node:
                return 0
            
            max_val = max(max_val, node.val)
            good_nodes = 1 if node.val >= max_val else 0
            good_nodes += dfs(node.left, node.val)
            good_nodes += dfs(node.right, node.val)
            return good_nodes

        return dfs(root, root.val)


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: binary tree, dfs, recursion
        side effect
        """
        self.good_nodes = 0
        
        def dfs(node, max_val):
            if not node:
                return
            
            max_val = max(max_val, node.val)
            if node.val >= max_val:
                self.good_nodes += 1
            
            dfs(node.left, node.val)
            dfs(node.right, node.val)

        dfs(root, root.val)
        return self.good_nodes


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: binary tree, bfs, iteration, queue
        """
        node = root
        queue = deque([(root, root.val)])
        good_nodes = 0

        while queue:
            for _ in range(len(queue)):
                node, max_val = queue.popleft()
                max_val = max(max_val, node.val)
                good_nodes += 1 if node.val >= max_val else 0

                if node.left:
                    queue.append((node.left, max_val))
                if node.right:
                    queue.append((node.right, max_val))
        
        return good_nodes


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: binary tree, dfs, iteration, stack
        """
        node = root
        stack = [(root, root.val)]
        good_nodes = 0

        while stack:
            for _ in range(len(stack)):
                node, max_val = stack.pop()
                max_val = max(max_val, node.val)
                good_nodes += 1 if node.val >= max_val else 0

                if node.left:
                    stack.append((node.left, max_val))
                if node.right:
                    stack.append((node.right, max_val))
        
        return good_nodes


print(Solution().goodNodes(build_tree([1])) == 1)
print(Solution().goodNodes(build_tree([1, 2, 3])) == 3)
print(Solution().goodNodes(build_tree([3, 1, 4, 3, None, 1, 5])) == 4)
print(Solution().goodNodes(build_tree([3, 3, None, 4, 2])) == 3)