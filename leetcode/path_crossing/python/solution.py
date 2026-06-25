class Solution:
    def isPathCrossing(self, path: str) -> bool:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: hash map, hash set
            A: iteration
        """
        DIRECTIONS = {
            "N": (0, 1),
            "S": (0, -1),
            "E": (1, 0),
            "W": (-1, 0),
        }
        x, y = 0, 0
        visited = set([(0, 0)])

        for direction in path:
            dx, dy = DIRECTIONS[direction]
            x += dx
            y += dy

            if (x, y) in visited:
                return True
            else:
                visited.add((x, y))

        return False


class Solution:
    def isPathCrossing(self, path: str) -> bool:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: hash map, hash set
            A: iteration
        """
        DIRECTIONS = {
            "N": (0, 1),
            "S": (0, -1),
            "E": (1, 0),
            "W": (-1, 0),
        }
        x, y = 0, 0
        visited = set()

        for direction in path:
            visited.add((x, y))
            dx, dy = DIRECTIONS[direction]
            x += dx
            y += dy

            if (x, y) in visited:
                return True

        return False


print(Solution().isPathCrossing("NES") == False)
print(Solution().isPathCrossing("NESWW") == True)
print(Solution().isPathCrossing("WNSN") == True)
print(Solution().isPathCrossing("SN") == True)
print(Solution().isPathCrossing("NNSWWEWSSESSWENNW") == True)
