class Solution:
    def survivedRobotsHealths(self, positions: list[int], healths: list[int], directions: str) -> list[int]:
        """
        Time complexity: O(nlogn)
        Auxiliary space complexity: O(n)
        Tags: stack
        """
        zip_data = sorted(zip(positions, healths, directions, range(len(positions))))
        robots = [(health, direction, position) for _, health, direction, position in zip_data]
        robot_stack = []

        for robot in robots:
            health, direction, position = robot

            if (
                robot_stack and 
                robot_stack[-1][1] == "R" and 
                direction == "L"
            ):
                prev_health, _, _ = robot_stack[-1]

                if prev_health == health:
                    robot_stack.pop()
                elif prev_health > health:
                    prev_health, prev_direction, prev_position = robot_stack.pop()
                    robot_stack.append((prev_health - 1, prev_direction, prev_position))
                else:
                    add = False
                    while robot_stack and robot_stack[-1][1] == "R":
                        prev_health, prev_direction, prev_position = robot_stack.pop()
                        
                        if prev_health < health:
                            health -= 1
                            add = True
                        elif prev_health == health:
                            add = False
                            break
                        else: # robot_stack[-1][0] > health
                            robot_stack.append((prev_health - 1, prev_direction, prev_position))
                            add = False
                            break

                    if add:
                        robot_stack.append((health, direction, position))
                    
            else:
                robot_stack.append(robot)

        robot_stack.sort(key=lambda x: x[2])
        return [health for health, _, _, in robot_stack]


print(Solution().survivedRobotsHealths([5, 4, 3, 2, 1], [2, 17, 9, 15, 10], "RRRRR") == [2, 17, 9, 15, 10])
print(Solution().survivedRobotsHealths([3, 5, 2, 6], [10, 10, 15, 12], "RLRL") == [14])
print(Solution().survivedRobotsHealths([1, 2, 5, 6], [10, 10, 11, 11], "RLRL") == [])
print(Solution().survivedRobotsHealths([11, 44, 16], [1, 20, 17], "RLR") == [18])
print(Solution().survivedRobotsHealths([17, 24, 18], [1, 39, 30], "LLR") == [1, 38])
print(Solution().survivedRobotsHealths([34, 50, 42, 2], [6, 27, 17, 38], "LLRR") == [36])