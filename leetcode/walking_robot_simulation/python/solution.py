import heapq


class Solution:
    def robotSim(self, commands: list[int], obstacles: list[list[int]]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: hash set
        """
        # orientation (x, y)
        DIRECTIONS = ((0, 1), (1, 0), (0, -1), (-1, 0))  # N, E, S, W
        direction = 0
        max_distance = 0
        x = y = 0
        obstacle_set = {tuple(obstacle) for obstacle in obstacles}

        for command in commands:
            if command == -1:
                direction = (direction + 1) % 4
            elif command == -2:
                direction = (direction - 1) % 4
            elif command > 0:
                d_x, d_y = DIRECTIONS[direction]
                for _ in range(command):
                    if (x + d_x, y + d_y) in obstacle_set:
                        break
                    x += d_x
                    y += d_y

                max_distance = max(max_distance, x**2 + y**2)

        return max_distance



class Solution:
    def robotSim(self, commands: list[int], obstacles: list[list[int]]) -> int:
        """
        Time complexity: O(nlogn)
        Auxiliary space complexity: O(n)
        Tags: heap
        Fails 46/51 test case.
        """
        # orientation (x, y)
        DIRECTIONS = ((0, 1), (1, 0), (0, -1), (-1, 0))  # N, E, S, W
        direction = 0
        max_distance = 0
        x_map = {}
        y_map = {}

        for x, y in obstacles:
            if x not in x_map:
                x_map[x] = ([], [])
            if y > 0:
                heapq.heappush(x_map[x][1], y)
            else:
                heapq.heappush(x_map[x][0], -y)

            if y not in y_map:
                y_map[y] = ([], [])
            if x > 0:
                heapq.heappush(y_map[y][1], x)
            else:
                heapq.heappush(y_map[y][0], -x)

        x = y = 0
        for command in commands:
            if command == -1:
                direction = (direction + 1) % 4
            elif command == -2:
                direction = (direction - 1) % 4
            elif command > 0:
                d_x, d_y = DIRECTIONS[direction]

                if d_x and y in y_map:
                    left_heap = y_map[y][0]
                    right_heap = y_map[y][1]

                    while d_x == 1 and right_heap and x >= right_heap[0]:
                        heapq.heappush(left_heap, -heapq.heappop(right_heap))
                    while d_x == -1 and left_heap and x <= -left_heap[0]:
                        heapq.heappush(right_heap, -heapq.heappop(left_heap))

                    x += command * d_x
                    if d_x == 1 and right_heap and x >= right_heap[0]:
                        x = right_heap[0] - d_x
                    elif d_x == -1 and left_heap and x <= -left_heap[0]:
                        x = -left_heap[0] - d_x

                elif d_y and x in x_map:
                    left_heap = x_map[x][0]
                    right_heap = x_map[x][1]
                    
                    while d_y == 1 and right_heap and y >= right_heap[0]:
                        heapq.heappush(left_heap, -heapq.heappop(right_heap))
                    while d_y == -1 and left_heap and y <= -left_heap[0]:
                        heapq.heappush(right_heap, -heapq.heappop(left_heap))

                    y += command * d_y
                    if d_y == 1 and right_heap and y >= right_heap[0]:
                        y = right_heap[0] - d_y
                    elif d_y == -1 and left_heap and y <= -left_heap[0]:
                        y = -left_heap[0] - d_y

                else:
                    x += command * d_x
                    y += command * d_y

                max_distance = max(max_distance, x**2 + y**2)

        return max_distance


print(Solution().robotSim([4, -1, 3], []), 25)
print(Solution().robotSim([4, -1, 4, -2, 4], [[2, 4]]), 65)
print(Solution().robotSim([6, -1, -1, 6], [[0, 0]]), 36)
print(Solution().robotSim([6, -1, -1, 6], []), 36)
print(Solution().robotSim([-2, -1, 8, 9, 6], [[-1, 3], [0, 1], [-1, 5], [-2, -4], [5, 4], [-2, -3], [5, -1], [1, -1], [5, 5], [5, 2]]), 0)
print(Solution().robotSim([7, -2, -2, 7, 5], [[-3, 2], [-2, 1], [0, 1], [-2, 4], [-1, 0], [-2, -3], [0, -3], [4, 4], [-3, 3], [2, 2]]), 4)
print(Solution().robotSim([-2,-1,-2,3,7], [[1,-3],[2,-3],[4,0],[-2,5],[-5,2],[0,0],[4,-4],[-2,-5],[-1,-2],[0,2]]), 100)
