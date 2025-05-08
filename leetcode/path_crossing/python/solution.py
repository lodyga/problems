class Solution:
    def isPathCrossing(self, path: str) -> bool:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        """
        horizontal = 0
        vertical = 0
        visited = set({(0, 0)})

        for direction in path:
            if direction == "E":
                horizontal += 1
            elif direction == "W":
                horizontal -= 1
            elif direction == "N":
                vertical += 1
            elif direction == "S":
                vertical -= 1
            
            if (vertical, horizontal) in visited:
                return True
            else:
                visited.add((vertical, horizontal))
        
        return False


class Solution:
    def isPathCrossing(self, path: str) -> bool:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        """
        prev_visit = (0, 0)
        visited = {prev_visit}

        directions = {
            "E": (0, 1),
            "W": (0, -1),
            "N": (1, 0),
            "S": (-1, 0)
        }

        for direction in path:
            next_visit = (prev_visit[0] + directions[direction][0], 
                          prev_visit[1] + directions[direction][1])

            if next_visit in visited:
                return True
            else:
                visited.add(next_visit)
                prev_visit = next_visit

        return False


print(Solution().isPathCrossing("NES"), False)
print(Solution().isPathCrossing("WNSN"), True)
print(Solution().isPathCrossing("NESWW"), True)