class Solution:
    def solve(self, board: list[list[str]]) -> None:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n2)
        Tags: backtracking, dfs, recursion, matrix, graph, hash set
        """
        ROWS = len(board)
        COLS = len(board[0])
        o_cells = set()
        DIRECTIONS = ((-1, 0), (1, 0), (0, -1), (0, 1))

        def dfs(row, col):
            if (
                row < 0 or
                col < 0 or
                row == ROWS or
                col == COLS or
                board[row][col] == "X" or
                (row, col) in o_cells
            ):
                return 
            
            o_cells.add((row, col))
            for r, c in DIRECTIONS:
                dfs(row + r, col + c)
                
        # check only the edges for border regions and mark them in o_colls
        # left and right edge
        for row in range(ROWS):
            dfs(row, 0)
            dfs(row, COLS - 1)
        
        # top and bottom edge
        for col in range(COLS):
            dfs(0, col)
            dfs(ROWS - 1, col)

        # change only non-border regions
        for row in range(ROWS):
            for col in range(COLS):
                if (
                    board[row][col] == "O" and 
                    (row, col) not in o_cells
                ):
                    board[row][col] = "X"

        return board


from collections import deque


class Solution:
    def solve(self, board: list[list[str]]) -> None:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n2)
        Tags: backtracking, bfs, iteration, matrix, graph
        """
        ROWS = len(board)
        COLS = len(board[0])
        DIRECTIONS = ((-1, 0), (1, 0), (0, -1), (0, 1))

        def bfs(row, col):
            if board[row][col] != 'O':
                return
            
            queue = deque([(row, col)])
            board[row][col] = "@"
            
            while queue:
                row, col = queue.popleft()

                for r, c in DIRECTIONS:
                    if (
                        0 <= row + r < ROWS and
                        0 <= col + c < COLS and
                        board[row + r][col + c] == "O"
                    ):
                        board[row + r][col + c] = "@"
                        queue.append((row + r, col + c))

        # check only the edges for border regions and mark them in o_colls
        # left and right edge
        for row in range(ROWS):
            bfs(row, 0)
            bfs(row, COLS - 1)
        
        # top and bottom edge
        for col in range(COLS):
            bfs(0, col)
            bfs(ROWS - 1, col)

        # change only non-border regions
        for row in range(ROWS):
            for col in range(COLS):
                if (board[row][col] == "O"):
                    board[row][col] = "X"
        
        for row in range(ROWS):
            for col in range(COLS):
                if (board[row][col] == "@"):
                    board[row][col] = "O"

        return board


print(Solution().solve([["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]]) == [["X", "X", "X", "X"], ["X", "X", "X", "X"], ["X", "X", "X", "X"], ["X", "O", "X", "X"]])
print(Solution().solve([["X"]]) == [["X"]])
print(Solution().solve([["O"]]) == [["O"]])