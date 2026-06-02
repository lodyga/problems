class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        """
        Time complexity: O(n2^n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: list
            A: backtracking
        """
        combination = []
        res = []

        def backtrack(idx):
            if len(combination) == k:
                res.append(combination.copy())
                return
            elif idx == n + 1:
                return

            combination.append(idx)
            backtrack(idx + 1)
            combination.pop()
            backtrack(idx + 1)

        backtrack(1)
        return res


class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        """
        Time complexity: O(n2^n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: list
            A: backtracking
        """
        combination = []
        res = []

        def backtrack(index):
            if len(combination) == k:
                res.append(combination.copy())
                return

            for num in range(index, n + 1):
                combination.append(num)
                backtrack(num + 1)
                combination.pop()

        backtrack(1)
        return res


class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        """
        Time complexity: O(n2^n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: queue
            A: bfs
        """
        from collections import deque
        combinations = []
        queue = deque([([], 0)])

        def bfs():
            level = 0
            while queue:
                for _ in range(len(queue)):

                    if level == k:
                        while queue:
                            combination, _ = queue.popleft()
                            combinations.append(combination)
                        return combinations
                
                    combination, prev_num = queue.popleft()

                    for num in range(prev_num + 1, n + 1):
                        combination.append(num)
                        queue.append((combination.copy(), num))
                        combination.pop()
                level += 1
        
        return bfs()


print(Solution().combine(4, 2) == [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]])
print(Solution().combine(1, 1) == [[1]])
print(Solution().combine(2, 2) == [[1, 2]])
