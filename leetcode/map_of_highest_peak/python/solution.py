class Solution:
    def highestPeak(self, is_water: list[list[int]]) -> list[list[int]]:
        from collections import deque
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n2)
        Tags:
            DS: queue, array (matrix)
            A: multi-source BFS
        """
        ROWS = len(is_water)
        COLS = len(is_water[0])
        DIRECTIONS = ((-1, 0), (1, 0), (0, -1), (0, 1))
        res = [[0] * COLS for _ in range(ROWS)]
        queue = deque()

        def bfs():
            height = 0

            while queue:
                for _ in range(len(queue)):
                    row, col = queue.popleft()

                    if res[row][col]:
                        continue

                    res[row][col] = height

                    for (dr, dc) in DIRECTIONS:
                        (r, c) = (row + dr, col + dc)

                        if (
                            r == -1 or r == ROWS or
                            c == -1 or c == COLS or
                            is_water[r][c] or
                            res[r][c] != 0
                        ):
                            continue

                        queue.append((r, c))

                height += 1

        for row in range(ROWS):
            for col in range(COLS):
                if is_water[row][col]:
                    queue.append((row, col))

        bfs()
        return res


print(Solution().highestPeak([[0, 1], [0, 0]]) == [[1, 0], [2, 1]])
print(Solution().highestPeak([[0, 0, 1], [1, 0, 0], [0, 0, 0]]) == [[1, 1, 0], [0, 1, 1], [1, 2, 2]])
print(Solution().highestPeak([[0, 0], [1, 1], [1, 0]]) == [[1, 1], [0, 0], [0, 1]])
