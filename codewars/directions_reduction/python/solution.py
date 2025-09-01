class Solution:
    def dir_reduc(self, direction_list: list[str]) -> list[str]:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: stack
        """
        visited_directions = []
        OPPOSITE_DIRECTIONS = {
            "NORTH": "SOUTH",
            "SOUTH": "NORTH",
            "EAST": "WEST",
            "WEST": "EAST",
        }

        for direction in direction_list:
            if (
                visited_directions and
                visited_directions[-1] == OPPOSITE_DIRECTIONS[direction]
            ):
                visited_directions.pop()
            else:
                visited_directions.append(direction)
        
        return visited_directions


print(Solution().dir_reduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]) == ["WEST"])
print(Solution().dir_reduc(["NORTH", "EAST", "WEST", "SOUTH", "WEST", "WEST"]) == ["WEST", "WEST"])
print(Solution().dir_reduc(["NORTH", "WEST", "SOUTH", "EAST"]) == ["NORTH", "WEST", "SOUTH", "EAST"])
print(Solution().dir_reduc([]) == [])
