class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        """
        Time complexity: O(nm*3^k)
            k: word length
        Auxiliary space complexity: O(nm)
        Tags: backtracking
        """
        rows = len(board)
        cols = len(board[0])
        directions = ((-1, 0), (1, 0), (0, -1), (0, 1))
        visited_cells = set()

        def dfs(row, col, index):
            if index == len(word):
                return True
            elif (
                row < 0 or
                col < 0 or
                row == rows or
                col == cols or
                board[row][col] != word[index] or
                (row, col) in visited_cells
            ):
                return False

            visited_cells.add((row, col))
            for r, c in directions:
                if dfs(row + r, col + c, index + 1):
                    return True
            visited_cells.discard((row, col))

            return False

        for row in range(rows):
            for col in range(cols):
                if dfs(row, col, 0):
                    return True

        return False


class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        """
        Time complexity: O(nm*3^k)
            k: word length
        Auxiliary space complexity: O(nm)
        Tags: backtracking
        """
        rows = len(board)
        cols = len(board[0])
        directions = ((-1, 0), (1, 0), (0, -1), (0, 1))

        def dfs(row, col, index):
            if index == len(word):
                return True
            elif (
                row < 0 or
                col < 0 or
                row == rows or
                col == cols or
                board[row][col] != word[index] or
                board[row][col] == "#"
            ):
                return False

            board[row][col] = "#"
            for r, c in directions:
                if dfs(row + r, col + c, index + 1):
                    return True
            board[row][col] = word[index]

            return False

        for row in range(rows):
            for col in range(cols):
                if dfs(row, col, 0):
                    return True

        return False


print(Solution().exist([["C", "A", "A"]], "AA") == True)
print(Solution().exist([["C", "A", "A"], ["C", "C", "B"]], "AAB") == True)
print(Solution().exist([["C", "A", "A"], ["A", "A", "A"], ["B", "C", "D"]], "AAB") == True)
print(Solution().exist([["C", "A", "A"], ["A", "A", "A"], ["B", "C", "D"]], "AACA") == True)
print(Solution().exist([["A", "A"]], "AAA") == False)
print(Solution().exist([["A", "B", "C", "E"], ["S", "F", "E", "S"], ["A", "D", "E", "E"]], "ABCEFSADEESE") == True)
print(Solution().exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "AB") == True)
print(Solution().exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "AZ") == False)
print(Solution().exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABFS") == True)
print(Solution().exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCCED") == True)
print(Solution().exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "SEE") == True)
print(Solution().exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCB") == False)