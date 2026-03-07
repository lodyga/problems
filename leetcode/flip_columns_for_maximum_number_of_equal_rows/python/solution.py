class Solution:
    def maxEqualRowsAfterFlips(self, matrix: list[list[int]]) -> int:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n)
        Tags:
            DS: hash map, tuple
            A: iteration
        """
        bin_count = {}

        for row in matrix:
            if row[0] == 0:
                row_hash = tuple(row)
            else:
                row_hash = tuple(0 if cell else 1 for cell in row)

            bin_count[row_hash] = bin_count.get(row_hash, 0) + 1

        return max(bin_count.values())


print(Solution().maxEqualRowsAfterFlips([[0, 1], [1, 1]]) == 1)
print(Solution().maxEqualRowsAfterFlips([[0, 1], [1, 0]]) == 2)
print(Solution().maxEqualRowsAfterFlips([[0, 0, 0], [0, 0, 1], [1, 1, 0]]) == 2)
print(Solution().maxEqualRowsAfterFlips([[1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1], [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0], [1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1], [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0], [1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1]]) == 2)
