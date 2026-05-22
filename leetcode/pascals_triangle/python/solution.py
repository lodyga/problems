class Solution:
    def generate(self, num_rows: int) -> list[list[int]]:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n2)
        Tags:
            DS: list
            A: bottom-up
        """
        triangle = [[1]]

        if num_rows == 1:
            return triangle

        for row in range(1, num_rows):
            line = [0] * (row + 1)

            for col in range(row):
                line[col] += triangle[row - 1][col]
                line[col + 1] += triangle[row - 1][col]

            triangle.append(line)

        return triangle


class Solution:
    def generate(self, num_rows: int) -> list[list[int]]:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n2)
        Tags:
            DS: list
            A: bottom-up
        """
        triangle = []

        for index in range(1, num_rows + 1):
            row = [1] * index

            for col in range(index - 2):
                row[col + 1] = triangle[-1][col] + triangle[-1][col + 1]

            triangle.append(row)

        return triangle


print(Solution().generate(1) == [[1]])
print(Solution().generate(2) == [[1], [1, 1]])
print(Solution().generate(5) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]])
