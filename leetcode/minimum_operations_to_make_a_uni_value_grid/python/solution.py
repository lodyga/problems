class Solution:
    def minOperations(self, grid: list[list[int]], x: int) -> int:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n)
        Tags:
        """
        ROWS = len(grid)
        COLS = len(grid[0])
        if ROWS == COLS == 1:
            return 0

        left = min(min(row) for row in grid)
        right = max(max(row) for row in grid)
        middle = int(sum(sum(row) for row in grid) // (ROWS * COLS))
        mod = sum((value - left) % x for row in grid for value in row)

        if mod != 0:
            return -1

        def min_operations(direction):
            min_counter = 10**9
            index = 0
            current_middle = middle
            while left <= current_middle <= right:
                is_break = False
                counter = 0
                current_middle = middle + index
                for row in range(ROWS):
                    if is_break:
                        break
                    for col in range(COLS):
                        cell = grid[row][col]
                        if abs(cell - current_middle) % x:
                            is_break = True
                            break
                        counter += abs(cell - current_middle) // x

                if is_break is False:
                    if counter < min_counter:
                        min_counter = counter
                    else:
                        break

                index += 1 * direction

            return min_counter

        res = min(min_operations(1), min_operations(-1))
        return res if res != 10**9 else -1


print(Solution().minOperations([[2, 4], [6, 8]], 2) == 4)
print(Solution().minOperations([[1, 5], [2, 3]], 1) == 5)
print(Solution().minOperations([[1, 2], [3, 4]], 2) == -1)
print(Solution().minOperations([[146]], 86) == 0)
print(Solution().minOperations([[931, 128], [639, 712]], 73) == 12)
