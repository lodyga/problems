class Solution:
    def leastBricks(self, wall: list[list[int]]) -> int:
        """
        Time complexity: O(n)
            n: brick count
        Auxiliary space complexity: O(m)
            m: distinct crack count
        Tags: hash map
        """
        # {crack position: vertical crack count}
        cracks = {0: 0}
        for row in wall:
            crack = 0
            for brick in row[:-1]:
                crack += brick
                cracks[crack] = cracks.get(crack, 0) + 1

        return len(wall) - max(cracks.values())


import heapq


class Solution:
    def leastBricks(self, wall: list[list[int]]) -> int:
        """
        Time complexity: O(nlogn)
            n: brick count
        Auxiliary space complexity: O(n)
        Tags: heap, prefix sum
        """
        ROWS = len(wall)
        COLS = sum(wall[0])

        if ROWS == 1:
            return 1 if len(wall[0]) == 1 else 0

        for row in range(ROWS):
            for col in range(1, len(wall[row])):
                wall[row][col] += wall[row][col - 1]

        brick_heap = []
        for row in range(ROWS):
            for col in range(len(wall[row])):
                heapq.heappush(brick_heap, (wall[row][col], row))

        cracks = {}
        while brick_heap:
            brick, _ = heapq.heappop(brick_heap)
            if brick == COLS:
                break
            cracks[brick - 1] = cracks.get(brick - 1, 0) + 1

        max_cracks = max(crack for crack in cracks.values()) if cracks else 0
        return ROWS - max_cracks


print(Solution().leastBricks([[1, 2, 2, 1], [3, 1, 2], [1, 3, 2], [2, 4], [3, 1, 2], [1, 3, 1, 1]]) == 2)
print(Solution().leastBricks([[1], [1], [1]]) == 3)
print(Solution().leastBricks([[2147483647, 2147483647, 2147483647, 2147483647]]) == 0)
print(Solution().leastBricks([[1]]) == 1)
print(Solution().leastBricks([[1000]]) == 1)
print(Solution().leastBricks([[100000000, 100000000], [100000000, 100000000]]) == 0)
print(Solution().leastBricks([[2], [2], [2]]) == 3)
