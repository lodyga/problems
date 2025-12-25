class Solution:
    def isPathCrossing(self, path: str) -> bool:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: hash set, hash map
            A: iteration
        """
        DIRECTIONS = {"E": (1, 0), "W": (-1, 0), "N": (0, 1), "S": (0, -1)}
        x, y = 0, 0
        visited = set([(x, y)])

        for direction in path:
            dx, dy = DIRECTIONS[direction]
            (x, y) = (x + dx, y + dy)
            
            if (x, y) in visited:
                return True
            else:
                visited.add((x, y))

        return False


print(Solution().isPathCrossing("NES") == False)
print(Solution().isPathCrossing("WNSN") == True)
print(Solution().isPathCrossing("NESWW") == True)
