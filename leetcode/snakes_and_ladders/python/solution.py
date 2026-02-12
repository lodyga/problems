class Solution:
    def snakesAndLadders(self, board: list[list[int]]) -> int:
        from collections import deque
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n2)
        Tags:
            DS: deque, array (matrix)
            A: BFS
        """
        def get_bord_val(index: int) -> int:
            index -= 1
            row = index // COLS
            col = index % COLS
            col = COLS - 1 - col if row % 2 else col
            val = board[row][col]
            return index + 1 if val == -1 else val

        ROWS = len(board)
        COLS = len(board[0])
        N = ROWS * COLS
        visited = [False] * (N + 1)
        board.reverse()

        def dijkstra(moves: int, board_val: int) -> int:
            roll_queue = deque([(moves, board_val)])
            visited[board_val] = True

            while roll_queue:
                moves, cell_index = roll_queue.popleft()

                for die_roll in range(1, 7):
                    next_cell = cell_index + die_roll
                    board_val = get_bord_val(next_cell)

                    if visited[board_val]:
                        continue
                    elif board_val == N:
                        return moves + 1

                    roll_queue.append((moves + 1, board_val))
                    visited[board_val] = True

            return -1

        return dijkstra(0, 1)


class Solution:
    def snakesAndLadders(self, board: list[list[int]]) -> int:
        import heapq
        """
        Time complexity: O(n2logn)
        Auxiliary space complexity: O(n2)
        Tags:
            DS: heap, array (matrix)
            A: greedy, Dijkstra
        """
        def get_bord_val(index: int) -> int:
            index -= 1
            row = index // COLS
            col = index % COLS
            col = COLS - 1 - col if row % 2 else col
            val = board[row][col]
            return index + 1 if val == -1 else val

        ROWS = len(board)
        COLS = len(board[0])
        N = ROWS * COLS
        visited = [False] * (N + 1)
        board.reverse()

        def dijikstra(moves: int, board_val: int) -> int:
            roll_heap = [(moves, board_val)]
            visited[board_val] = True

            while roll_heap:
                moves, cell_index = heapq.heappop(roll_heap)

                for die_roll in range(1, 7):
                    next_cell = cell_index + die_roll
                    board_val = get_bord_val(next_cell)

                    if visited[board_val]:
                        continue
                    elif board_val == N:
                        return moves + 1

                    heapq.heappush(roll_heap, (moves + 1, board_val))
                    visited[board_val] = True

            return -1

        return dijikstra(0, 1)


print(Solution().snakesAndLadders([[-1, -1], [-1, 3]]) == 1)
print(Solution().snakesAndLadders([[2, -1, -1], [-1, -1, -1], [-1, -1, -1]]) == 2)
print(Solution().snakesAndLadders([[-1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1], [-1, 35, -1, -1, 13, -1], [-1, -1, -1, -1, -1, -1], [-1, 15, -1, -1, -1, -1]]) == 4)
print(Solution().snakesAndLadders([[1, 1, -1], [1, 1, 1], [-1, 1, 1]]) == -1)
print(Solution().snakesAndLadders([[2, -1, -1, -1, -1], [-1, -1, -1, -1, -1], [-1, -1, -1, -1, -1], [-1, -1, -1, -1, -1], [-1, -1, -1, -1, -1]]) == 4)
