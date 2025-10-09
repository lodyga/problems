class Solution:
    def rotateTheBox(self, box_grid: list[list[str]]) -> list[list[str]]:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(1)
        Tags: two pointers
        """
        ROWS = len(box_grid)
        COLS = len(box_grid[0])

        def drop_stones(row, empty, left, right):
            while left < right:
                if empty:
                    box_grid[row][left] = "."
                    empty -= 1
                else:
                    box_grid[row][left] = "#"
                left += 1

        for row in range(ROWS):
            left = 0
            empty = 0
            for right, cell in enumerate(box_grid[row]):
                if cell == ".":
                    empty += 1
                elif cell == "*":
                    drop_stones(row, empty, left, right)
                    empty = 0
                    left = right + 1
            drop_stones(row, empty, left, COLS)

        return [[box_grid[row][col] 
                 for row in reversed(range(ROWS))] 
                 for col in range(COLS)]


class Solution:
    def rotateTheBox(self, box_grid: list[list[str]]) -> list[list[str]]:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(1)
        Tags: two pointers
        """
        ROWS = len(box_grid)
        COLS = len(box_grid[0])

        for row in range(ROWS):
            right = COLS - 1

            for col in reversed(range(COLS)):
                cell = box_grid[row][col]
                if cell == "#":
                    box_grid[row][col], box_grid[row][right] = box_grid[row][right], box_grid[row][col]
                    right -= 1
                elif cell == "*":
                    right = col - 1

        return [[box_grid[row][col] 
                 for row in reversed(range(ROWS))] 
                 for col in range(COLS)]


print(Solution().rotateTheBox([["#", ".", "#"]]) == [['.'], ['#'], ['#']])
print(Solution().rotateTheBox([["#", ".", "#", "."]]) == [['.'], ['.'], ['#'], ['#']])
print(Solution().rotateTheBox([["#", ".", "*", "."]]) == [['.'], ['#'], ['*'], ['.']])
print(Solution().rotateTheBox([["#", ".", "*", "#", "."]]) == [['.'], ['#'], ['*'], ['.'], ['#']])
print(Solution().rotateTheBox([["#", ".", "*", "."], ["#", "#", "*", "."]]) == [["#", "."], ["#", "#"], ["*", "*"], [".", "."]])
print(Solution().rotateTheBox([["#", "#", "*", ".", "*", "."], ["#", "#", "#", "*", ".", "."], ["#", "#", "#", ".", "#", "."]]) == [[".", "#", "#"], [".", "#", "#"], ["#", "#", "*"], ["#", "*", "."], ["#", ".", "*"], ["#", ".", "."]])