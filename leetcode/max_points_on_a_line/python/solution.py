class Solution:
    def maxPoints(self, points: list[list[int]]) -> int:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n2)
        Tags:
            DS: hash map, hash set
            A: iteration
        """
        if len(points) in (0, 1, 2):
            return len(points)

        point_set = set()
        # {x: couter}
        x_map = {}
        # {(slope: intercept): {(x1, y1), (x2, y2), }, }
        line_to_point = {}

        for nx, ny in points:
            x_map[nx] = x_map.get(nx, 0) + 1

            for x, y in point_set:
                if nx == x:
                    continue

                a = (ny - y) / (nx - x)
                b = y - a*x

                if (a, b) in line_to_point:
                    if (nx, ny) not in line_to_point[(a, b)]:
                        line_to_point[(a, b)].add((nx, ny))

                else:
                    line_to_point[(a, b)] = set([(x, y), (nx, ny)])

            point_set.add((nx, ny))

        return max(
            len(max(line_to_point.values(), key=len)) if line_to_point else 0,
            max(x_map.values()),
        )


print(Solution().maxPoints([[1, 1], [2, 2], [3, 3]]) == 3)
print(Solution().maxPoints([[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]) == 4)
print(Solution().maxPoints([[0, 0]]) == 1)
print(Solution().maxPoints([[1, 0], [0, 0]]) == 2)
print(Solution().maxPoints([[0, 0], [1, -1], [1, 1]]) == 2)
print(Solution().maxPoints([[4, 5], [4, -1], [4, 0]]) == 3)
