class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n)
        """
        last_row = [1]

        for row in range(rowIndex):
            current_row = [1] * (row + 2)
            for col in range(len(last_row) - 1):
                current_row[col + 1] = last_row[col] + last_row[col + 1]
            last_row = current_row

        return last_row


print(Solution().getRow(0) == [1])
print(Solution().getRow(1) == [1, 1])
print(Solution().getRow(2) == [1, 2, 1])
print(Solution().getRow(3) == [1, 3, 3, 1])
