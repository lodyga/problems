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
        unique_cells = set()
        directions = ((-1, 0), (1, 0), (0, -1), (0, 1))

        def dfs(index, row, col):
            if index == len(word):
                return True
            elif (
                row < 0 or
                col < 0 or
                row == rows or
                col == cols or
                board[row][col] != word[index] or
                (row, col) in unique_cells
            ):
                return

            unique_cells.add((row, col))
            is_path_right = any(dfs(index + 1, row + r, col + c)
                                for r, c in directions)
            
            unique_cells.pop()
            return is_path_right

        for row in range(rows):
            for col in range(cols):
                if dfs(0, row, col):
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

        def dfs(index, row, col):
            if index == len(word):
                return True
            elif (
                row < 0 or
                col < 0 or
                row == rows or
                col == cols or
                board[row][col] != word[index] or
                [row, col] == "#"
            ):
                return

            board[row][col] = "#"
            is_path_right = any(dfs(index + 1, row + r, col + c)
                                for r, c in directions)

            board[row][col] = word[index]
            return is_path_right

        for row in range(rows):
            for col in range(cols):
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