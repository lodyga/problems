class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        """
        Time complexity: O(n2*3^k)
            k: word length
        Auxiliary space complexity: O(n2)
        Tags: 
            DS: array (matrix)
            A: backtracking
        """
        ROWS = len(board)
        COLS = len(board[0])
        DIRECTIONS = ((-1, 0), (1, 0), (0, -1), (0, 1))
        visited = [[False] * COLS for _ in range(ROWS)]

        def dfs(index, row, col):
            if index == len(word):
                return True
            elif (
                row == -1 or
                col == -1 or
                row == ROWS or
                col == COLS or
                board[row][col] != word[index] or
                visited[row][col] is True
            ):
                return False

            visited[row][col] = True
            for dr, dc in DIRECTIONS:
                (r, c) = (row + dr, col + dc)
                if dfs(index + 1, r, c):
                    return True

            visited[row][col] = False
            return False

        for row in range(ROWS):
            for col in range(COLS):
                if dfs(0, row, col):
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
