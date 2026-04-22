class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            DS: array
            A: iteration
        """
        DIRECTIONS = (
            (0, 1),   # N
            (1, 0),   # E
            (0, -1),  # S
            (-1, 0),  # W
        )
        direction = 0
        pos = [0, 0]

        for ins in instructions:
            if ins == "L":
                direction = (direction - 1) % 4
            elif ins == "R":
                direction = (direction + 1) % 4
            else:
                pos[0] += DIRECTIONS[direction][0]
                pos[1] += DIRECTIONS[direction][1]

        return pos == [0, 0] or direction != 0


print(Solution().isRobotBounded("GGLLGG") == True)
print(Solution().isRobotBounded("GG") == False)
print(Solution().isRobotBounded("GL") == True)
