class Solution:
    def dir_reduc(self, direction_list: list[str]) -> list[str]:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: stack
            A: iteration
        """
        direction_stack = []
        OPPOSITE_DIRECTION = {
            "SOUTH": "NORTH",
            "NORTH": "SOUTH",
            "EAST": "WEST",
            "WEST": "EAST"
        }

        for direction in direction_list:
            if direction_stack and direction_stack[-1] == OPPOSITE_DIRECTION[direction]:
                direction_stack.pop()
            else:
                direction_stack.append(direction)
        
        return direction_stack


print(Solution().dir_reduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]) == ["WEST"])
print(Solution().dir_reduc(["NORTH", "EAST", "WEST", "SOUTH", "WEST", "WEST"]) == ["WEST", "WEST"])
print(Solution().dir_reduc(["NORTH", "WEST", "SOUTH", "EAST"]) == ["NORTH", "WEST", "SOUTH", "EAST"])
print(Solution().dir_reduc([]) == [])
