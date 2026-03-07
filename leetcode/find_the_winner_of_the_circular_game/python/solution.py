class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        from collections import deque
        """
        Time complexity: O(n*k)
        Auxiliary space complexity: O(n)
        Tags:
            DS: queue
            A: iteration
        """
        queue = deque(list(range(1, n + 1)))
        
        while len(queue) > 1:
            for _ in range(k - 1):
                queue.append(queue.popleft())

            queue.popleft()

        return queue[0]


class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            A: recursion
        """
        def dfs(n, k):
            if n == 1:
                return 0
            
            return (dfs(n - 1, k) + k) % n
        
        return dfs(n, k) + 1


class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            A: iteration
        """
        res = 0
        
        for index in range(1, n + 1):
            res = (res + k) % index
        
        return res + 1


print(Solution().findTheWinner(5, 2) == 3)
print(Solution().findTheWinner(6, 5) == 1)
