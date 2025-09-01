r"""
[   pacific
p   [1 , 2 , 2 , 3 , 5 ],    a
a   [3 , 2 , 3 , 4 , 4 ],    t
c   [2 , 4 , 5 , 3 , 1 ],    l 
i   [6 , 7 , 1 , 4 , 5 ],    a
f   [5 , 1 , 1 , 2 , 4 ]     n
    atlantic
]
[   pacific
p   [p , p , p , p , pa],    a
a   [p , 2 , 3 , 4 , a ],    t
c   [p , 4 , 5 , 3 , a ],    l 
i   [p , 7 , 1 , 4 , a ],    a
f   [pa, a , a , a , a ]     n
    atlantic
]

1 , 2 , 3,
8 , 9 , 4,
7 , 6 , 5

p , p , p ,
p , p , p ,
p ,   ,   ,
"""


class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n2)
        Tags: backtracking, hash set
        """
        rows = len(heights)
        cols = len(heights[0])
        pacific = set()
        atlantic = set()
        DIRECTIONS = ((-1, 0), (1, 0), (0, -1), (0, 1))

        def dfs(row, col, ocean, prev_height):
            if (
                row < 0 or
                col < 0 or
                row == rows or
                col == cols or
                heights[row][col] < prev_height or
                (row, col) in ocean
            ):
                return

            ocean.add((row, col))
            for r, c in directions:
                dfs(row + r, col + c, ocean, heights[row][col])

        for row in range(rows):
            dfs(row, 0, pacific, heights[row][0])
            dfs(row, cols - 1, atlantic, heights[row][cols - 1])

        for col in range(cols):
            dfs(0, col, pacific, heights[0][col])
            dfs(rows - 1, col, atlantic, heights[rows - 1][col])
        
        return [[row, col] for row, col in pacific & atlantic]


class Solution2:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        """
        Time complexity: O(nm4^nm)
        Auxiliary space complexity: O(nm)
        Tags: brute-force, dfs, recursion, matrix, graph
        """
        rows = len(heights)
        cols = len(heights[0])
        DIRECTIONS = ((-1, 0), (1, 0), (0, -1), (0, 1))
        both_oceans = set()
        # visited_cells = set()

        def dfs(row, col):
            if (row == 0 or col == 0):
                self.pacific = True
            if (row == rows - 1 or col == cols - 1):
                self.atlantic = True
            if self.pacific and self.atlantic:
                return True

            visited_cells.add((row, col))

            for r, c in directions:
                if (
                    0 <= row + r < rows and
                    0 <= col + c < cols and
                    (row + r, col + c) not in visited_cells and
                    heights[row + r][col + c] <= heights[row][col]
                ):
                    if (row + r, col + c) in both_oceans:
                        return True
                    elif dfs(row + r, col + c):
                        return True
            
            visited_cells.discard((row, col))
            return False

        for row in range(rows):
            for col in range(cols):
                visited_cells = set()
                self.pacific = False
                self.atlantic = False
                if dfs(row, col):
                    both_oceans.add((row, col))

        return [[row, col] for row, col in both_oceans]


from collections import deque


class Solution2:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        """
        Time complexity: O(nm4^nm)
        Auxiliary space complexity: O(nm)
        Tags: brute-force, bfs, iteration, queue, matrix, graph
        """
        rows = len(heights)
        cols = len(heights[0])
        DIRECTIONS = ((-1, 0), (1, 0), (0, -1), (0, 1))
        both_oceans = []

        def bfs(row, col):
            queue = deque([(row, col)])
            pacific = False
            atlantic = False

            while queue:
                row, col = queue.popleft()

                if (row == 0 or col == 0):
                    pacific = True
                if (row == rows - 1 or col == cols - 1):
                    atlantic = True
                if pacific and atlantic:
                    return True

                visited_cells.add((row, col))

                for r, c in directions:
                    if (
                        0 <= row + r < rows and
                        0 <= col + c < cols and
                        (row + r, col + c) not in visited_cells and
                        heights[row + r][col + c] <= heights[row][col]
                    ):
                        queue.append((row + r, col + c))

            return False

        for row in range(rows):
            for col in range(cols):
                visited_cells = set()
                self.pacific = False
                self.atlantic = False
                if bfs(row, col):
                    both_oceans.append([row, col])

        return both_oceans


print(sorted(Solution().pacificAtlantic([[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]])) == sorted([[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]]))
print(sorted(Solution().pacificAtlantic([[1, 2, 3], [8, 9, 4], [7, 6, 5]])) == sorted([[0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]))
print(sorted(Solution().pacificAtlantic([[1]])) == sorted([[0, 0]]))