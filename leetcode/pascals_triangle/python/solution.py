class Solution:
    def generate(self, row_count: int) -> list[list[int]]:
        """
        Time complexity: O(2)
        Auxiliary space complexity: O(n)
        """
        triangle = [[1]]

        for row in range(row_count - 1):
            last_row = triangle[-1]
            new_row = [1] * (row + 2)

            for col in range(row):
                new_row[col + 1] = last_row[col] + last_row[col + 1]

            triangle.append(new_row)

        return triangle


print(Solution().generate(1) == [[1]])
print(Solution().generate(2) == [[1], [1, 1]])
print(Solution().generate(5) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]])