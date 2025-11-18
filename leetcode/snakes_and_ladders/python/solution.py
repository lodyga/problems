from collections import deque


class Solution:
    def snakesAndLadders(self, board: list[list[int]]) -> int:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n2)
        Tags: bfs, iteration, queue, graph, matrix
        """
        ROWS = len(board)
        COLS = len(board[0])
        LAST = ROWS * COLS - 1
        visited = [[False] * COLS for _ in range(ROWS)]

        def get_row_cell(cell):
            rev_row = cell // COLS
            row = ROWS - 1 - rev_row

            col = cell % COLS
            if rev_row % 2:
                col = COLS - 1 - col

            return (row, col)

        def bfs(moves, cell):
            # deque((moves, distance)); min moves, max distance
            queue = deque([(moves, cell)])

            while queue:
                distance, cell = queue.popleft()

                row, col = get_row_cell(cell)
                if visited[row][col]:
                    continue
                visited[row][col] = True

                for next_cell in range(cell + 1, min(cell + 7, LAST + 1)):
                    row, col = get_row_cell(next_cell)

                    # if snake or ladder
                    if board[row][col] != -1:
                        next_cell = board[row][col] - 1
                    
                    if next_cell == LAST:
                        return distance + 1
                    
                    queue.append((distance + 1, next_cell))

            return -1

        return bfs(0, 0)


import heapq


class Solution:
    def snakesAndLadders(self, board: list[list[int]]) -> int:
        """
        Time complexity: O(n2logn)
        Auxiliary space complexity: O(n2)
        Tags: bfs, iteration, heap, graph, matrix
        Dijkstra's alg
        """
        ROWS = len(board)
        COLS = len(board[0])
        LAST = ROWS * COLS - 1
        visited = [[False] * COLS for _ in range(ROWS)]

        def get_row_cell(cell):
            rev_row = cell // COLS
            row = ROWS - 1 - rev_row

            col = cell % COLS
            if rev_row % 2:
                col = COLS - 1 - col

            return (row, col)

        def bfs(moves, cell):
            # heap((moves, -distance)); min moves, max distance
            heap = [(moves, -cell)]

            while heap:
                distance, cell = heapq.heappop(heap)
                cell = -cell

                row, col = get_row_cell(cell)
                if visited[row][col]:
                    continue
                visited[row][col] = True

                for next_cell in range(cell + 1, min(cell + 7, LAST + 1)):
                    row, col = get_row_cell(next_cell)

                    # if snake or ladder
                    if board[row][col] != -1:
                        next_cell = board[row][col] - 1

                    if next_cell == LAST:
                        return distance + 1
                    
                    heapq.heappush(heap, (distance + 1, -next_cell))

            return -1

        return bfs(0, 0)


print(Solution().snakesAndLadders([[-1, -1], [-1, 3]]) == 1)
print(Solution().snakesAndLadders([[2, -1, -1], [-1, -1, -1], [-1, -1, -1]]) == 2)
print(Solution().snakesAndLadders([[-1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1], [-1, 35, -1, -1, 13, -1], [-1, -1, -1, -1, -1, -1], [-1, 15, -1, -1, -1, -1]]) == 4)
print(Solution().snakesAndLadders([[1, 1, -1], [1, 1, 1], [-1, 1, 1]]) == -1)
print(Solution().snakesAndLadders([[2, -1, -1, -1, -1], [-1, -1, -1, -1, -1], [-1, -1, -1, -1, -1], [-1, -1, -1, -1, -1], [-1, -1, -1, -1, -1]]) == 4)