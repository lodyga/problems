class Solution:
    def rotateTheBox(self, box_grid: list[list[str]]) -> list[list[str]]:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(1)
        Tags:
            DS: array (matrix)
            A: two pointers
        """
        ROWS = len(box_grid)
        COLS = len(box_grid[0])
        
        for row in range(ROWS):
            right = COLS - 1
            stone_row = box_grid[row]
            
            for left in range(COLS - 1, -1, -1):
                cell = stone_row[left]
                
                if cell == "#":
                    stone_row[left], stone_row[right] = stone_row[right], stone_row[left]
                    right -= 1
                elif cell == "*":
                    right = left - 1
        
        return [[box_grid[row][col] 
                 for row in range(ROWS - 1, -1, -1)] 
                for col in range(COLS)]


print(Solution().rotateTheBox([["#", ".", "#"]]) == [['.'], ['#'], ['#']])
print(Solution().rotateTheBox([["#", ".", "#", "."]]) == [['.'], ['.'], ['#'], ['#']])
print(Solution().rotateTheBox([["#", ".", "*", "."]]) == [['.'], ['#'], ['*'], ['.']])
print(Solution().rotateTheBox([["#", ".", "*", "#", "."]]) == [['.'], ['#'], ['*'], ['.'], ['#']])
print(Solution().rotateTheBox([["#", ".", "*", "."], ["#", "#", "*", "."]]) == [["#", "."], ["#", "#"], ["*", "*"], [".", "."]])
print(Solution().rotateTheBox([["#", "#", "*", ".", "*", "."], ["#", "#", "#", "*", ".", "."], ["#", "#", "#", ".", "#", "."]]) == [[".", "#", "#"], [".", "#", "#"], ["#", "#", "*"], ["#", "*", "."], ["#", ".", "*"], ["#", ".", "."]])
