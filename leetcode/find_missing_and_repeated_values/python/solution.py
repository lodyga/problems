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
        DIMS = len(grid)**2
        seen = [False] * DIMS
        res = []

        for row in range(N):
            for col in range(N):
                num = grid[row][col]
                if seen[num - 1]:
                    res.append(num)
                seen[num - 1] = True

        for index in range(DIMS):
            if not seen[index]:
                res.append(index + 1)

        return res


print(Solution().findMissingAndRepeatedValues([[1, 3], [2, 2]]) == [2, 4])
print(Solution().findMissingAndRepeatedValues([[9, 1, 7], [8, 9, 2], [3, 4, 6]]) == [9, 5])
