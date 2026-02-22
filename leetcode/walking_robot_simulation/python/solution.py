class Solution:
    def robotSim(self, commands: list[int], obstacles: list[list[int]]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: hash set
            A iteration
        """
        x = 0
        y = 0
        # N, E, S, W
        DIRECTIONS = ((0, 1), (1, 0), (0, -1), (-1, 0))
        direction = 0
        res = 0
        obstacle_set = {tuple(obstacle) for obstacle in obstacles}

        for command in commands:
            if command == -1:
                direction = (direction + 1) % 4
            elif command == -2:
                direction = (direction - 1) % 4
            else:
                dx, dy = DIRECTIONS[direction]

                for _ in range(command):
                    if (x + dx, y + dy) in obstacle_set:
                        break
                    else:
                        x += dx
                        y += dy

                res = max(res, x**2 + y**2)

        return res


print(Solution().robotSim([4, -1, 3], []) == 25)
print(Solution().robotSim([4, -1, 4, -2, 4], [[2, 4]]) == 65)
print(Solution().robotSim([6, -1, -1, 6], [[0, 0]]) == 36)
print(Solution().robotSim([6, -1, -1, 6], []) == 36)
print(Solution().robotSim([-2, -1, 8, 9, 6], [[-1, 3], [0, 1], [-1, 5], [-2, -4], [5, 4], [-2, -3], [5, -1], [1, -1], [5, 5], [5, 2]]) == 0)
print(Solution().robotSim([7, -2, -2, 7, 5], [[-3, 2], [-2, 1], [0, 1], [-2, 4], [-1, 0], [-2, -3], [0, -3], [4, 4], [-3, 3], [2, 2]]) == 4)
print(Solution().robotSim([-2, -1, -2, 3, 7], [[1, -3], [2, -3], [4, 0], [-2, 5], [-5, 2], [0, 0], [4, -4], [-2, -5], [-1, -2], [0, 2]]) == 100)
print(Solution().robotSim([2, -1, -1, -1, -2, 1, 7, -2, 9, 2, 3, -1, 4, 9, 7, 7, 2, 4, 2, -2, 1, 5, 8, -2, -2, 4, 2, 9, 7, 5, 5, -2, 2, 2, 1, -1, -1, 1, 6, 6, -1, 7, -1, 7, 1, 8, 2, -1, 8, 7, -1, 2, -2, 2, 2, 4, 9, -1, 4, -1, -2, 8, -1, 3, 6, -2, 7, -2, 6, 7, 9, 6, -2, -1, 3, 6, 2, 8, 6, 6, -2, -2, 4, 2, 4, 1, 2, 2, 2, 8, 6, 4, 6, 7, -1, 1, -2, -1, -1, 7], [[75, 61], [-27, -13], [-85, 77], [-40, -30], [-71, -34], [41, -39], [73, -54], [-19, 16], [76, 50], [-12, -9], [-25, -100], [45, -86], [-43, -88], [50, -23], [-46, -89], [-66, 91], [-57, -46], [-82, 51], [78, 98], [65, -61], [83, -14], [24, -17], [28, 77], [-63, -3], [77, -39], [18, -63], [10, -91], [-11, -15], [-75, -80], [68, 92], [21, -70], [91, -53], [-68, -64], [9, -68], [1, 40], [-73, 20], [56, 15], [-90, -43], [-100, 99], [-19, 7], [14, 76], [-80, -2], [24, -34], [47, 7], [25, 73], [-99, -39], [-55, -9], [85, 31], [14, 0], [-68, 94], [-25, 25], [44, -77], [-94, 59], [92, -47], [40, 5], [-68, -58], [87, 39], [-43, 93], [-83, -77], [-95, 81], [82, 37], [66, 21], [-5, 73], [-75, 32], [30, 70], [22, -68], [-27, 31], [-91, 80], [82, -58], [-95, -24], [15, 22], [-10, 38], [85, 96], [68, 26], [81, -18], [23, -47], [-80, -78], [30, 18], [-56, 4], [1, 33], [-21, 2], [-69, 85], [41, 92], [-72, 79], [-48, -34], [-34, 63], [48, -78], [17, 73], [16, 28], [-13, -14], [16, 24], [11, -27], [44, 52], [-78, 67], [93, 65], [-32, -33], [6, -2], [67, -100], [95, 77], [-6, 28], [10, 81], [-45, 48], [80, -34], [-49, 46], [-38, 17], [7, -81], [-29, 52], [46, -82], [5, -71], [79, -87], [39, -82], [-78, -82], [-85, 19], [74, -55], [22, 45], [-40, -24], [44, 97], [41, -21], [-17, -92], [17, 49], [-1, -33], [39, -36], [37, -38], [41, -29], [72, -88], [-100, 57], [-95, 74], [-27, -16], [57, -34], [74, -85], [62, 92], [44, 0], [83, 57], [90, 96], [-65, 70], [-58, 99], [-70, -86], [75, -74], [-63, 11], [-64, 20], [-35, -40], [-86, -71], [-77, -62], [4, -95], [97, 76], [36, -62], [-1, 90], [99, 91], [55, 89], [80, 77], [40, 54], [79, -11], [44, -36], [-35, 21], [-13, -86], [-55, 84], [27, 94], [74, 91], [-77, -45], [-90, 44], [-80, -35], [-38, 80], [34, -28], [45, -77], [1, 28], [-88, -50], [-100, 87], [19, 93], [-26, -39], [-83, -100], [-6, 43], [89, 42], [-35, -95], [-67, -96], [14, 22], [-25, 8], [-31, -9], [-94, 48], [82, -3], [39, 95], [44, 47], [-62, -71], [73, -30], [92, -11], [2, 85], [-91, 97], [99, -18], [-57, -17], [57, 73], [-41, 9], [44, 9], [17, -96], [-95, -16], [40, -3], [-48, -41], [95, 18], [-34, -94], [15, -90], [42, 11], [-65, -57]]) == 3557)


class Solution:
    def robotSim(self, commands: list[int], obstacles: list[list[int]]) -> int:
        import heapq
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
