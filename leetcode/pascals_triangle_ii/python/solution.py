class Solution:
    def getRow(self, row_index: int) -> list[int]:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n2)
        Tags:
            DS: list
            A: bottom-up
        """
        prev_row_vals = [1]
        
        for row in range(row_index):
            row_vals = [1]
            for col in range(row):
                row_vals.append(prev_row_vals[col] + prev_row_vals[col + 1])
            row_vals.append(1)
            prev_row_vals = row_vals

        return prev_row_vals


print(Solution().getRow(0) == [1])
print(Solution().getRow(1) == [1, 1])
print(Solution().getRow(2) == [1, 2, 1])
print(Solution().getRow(3) == [1, 3, 3, 1])
