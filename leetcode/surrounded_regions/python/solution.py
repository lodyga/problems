from collections import deque


class Solution:
    def solve(self, board: list[list[str]]) -> None:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(1)
        Tags:
            DS: array (matrix)
            A: multi-source DFS
        """
        ROWS = len(board)
        COLS = len(board[0])
        DIRECTIONS = ((-1, 0), (1, 0), (0, -1), (0, 1))

        def dfs(row: int, col: int) -> None:
            if (
                row == -1 or
                col == -1 or
                row == ROWS or
                col == COLS or
                board[row][col] != "O"
            ):
                return

            board[row][col] = "@"

            for dr, dc in DIRECTIONS:
                (r, c) = (row + dr, col + dc)
                dfs(r, c)

        # Mark border regions. Change "O" to "@".
        for row in range(ROWS):
            dfs(row, 0)
            dfs(row, COLS - 1)
        for col in range(COLS):
            dfs(0, col)
            dfs(ROWS - 1, col)

        # Capture internal regions.
        for row in range(1, ROWS - 1):
            for col in range(1, COLS - 1):
                if board[row][col] == "O":
                    board[row][col] = "X"

        # Revert border regions marking.
        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == "@":
                    board[row][col] = "O"

        return board


class Solution:
    def solve(self, board: list[list[str]]) -> None:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n2)
        Tags:
            DS: queue, array (matrix)
            A: multi-source BFS
        """
        ROWS = len(board)
        COLS = len(board[0])
        DIRECTIONS = ((-1, 0), (1, 0), (0, -1), (0, 1))

        def bfs(row: int, col: int) -> None:
            if board[row][col] != "O":
                return

            queue = deque([(row, col)])
            while queue:
                row, col = queue.popleft()
                board[row][col] = "@"

                for dr, dc in DIRECTIONS:
                    (r, c) = (row + dr, col + dc)

                    if (
                        r == -1 or
                        c == -1 or
                        r == ROWS or
                        c == COLS or
                        board[r][c] != "O"
                    ):
                        continue

                    queue.append((r, c))
                    board[r][c] = "@"

        # Mark border regions. Change "O" to "@".
        for row in range(ROWS):
            bfs(row, 0)
            bfs(row, COLS - 1)
        for col in range(COLS):
            bfs(0, col)
            bfs(ROWS - 1, col)

        # Capture internal regions.
        for row in range(1, ROWS - 1):
            for col in range(1, COLS - 1):
                if board[row][col] == "O":
                    board[row][col] = "X"

        # Revert border regions marking.
        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == "@":
                    board[row][col] = "O"

        return board


print(Solution().solve([["X"]]) == [["X"]])
print(Solution().solve([["O"]]) == [["O"]])
print(Solution().solve([["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]]) == [["X", "X", "X", "X"], ["X", "X", "X", "X"], ["X", "X", "X", "X"], ["X", "O", "X", "X"]])
print(Solution().solve([["X", "X", "X", "X"], ["X", "X", "X", "X"], ["X", "O", "X", "X"], ["X", "O", "X", "X"]]) == [["X", "X", "X", "X"], ["X", "X", "X", "X"], ["X", "O", "X", "X"], ["X", "O", "X", "X"]])
