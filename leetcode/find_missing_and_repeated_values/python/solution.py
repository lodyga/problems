class Solution:
    def findMissingAndRepeatedValues(self, grid: list[list[int]]) -> list[int]:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n2)
        Tags:
            DS: array (matrix)
            A: iteration
        """
        N = len(grid)
        seen = [False] * N * N
        res = []

        for row in range(N):
            for col in range(N):
                val = grid[row][col]

                if seen[val - 1]:
                    res.append(val)
                else:
                    seen[val - 1] = True

        for idx, b in enumerate(seen):
            if not b:
                res.append(idx + 1)
                break

        return res


print(Solution().findMissingAndRepeatedValues([[1, 3], [2, 2]]) == [2, 4])
print(Solution().findMissingAndRepeatedValues([[9, 1, 7], [8, 9, 2], [3, 4, 6]]) == [9, 5])
