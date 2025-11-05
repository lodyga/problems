class Solution:
    def minimumFuelCost(self, roads: list[list[int]], seats: int) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: dfs, recursion, graph
        """
        if len(roads) == 0:
            return 0

        adjs = {}
        for u, v in roads:
            if u not in adjs:
                adjs[u] = set()
            if v not in adjs:
                adjs[v] = set()
            adjs[u].add(v)
            adjs[v].add(u)

        fuel = 0
        def dfs(city, prev_city):
            nonlocal fuel
            passengers = 1

            for next_city in adjs[city]:
                if next_city == prev_city:
                    continue
                
                next_passengers = dfs(next_city, city)
                # fuel += math.ceil(next_passengers / seats)
                fuel += ((next_passengers - 1) // seats) + 1
                passengers += next_passengers

            return passengers

        dfs(0, -1)
        return fuel


from collections import deque


class Solution2:
    def minimumFuelCost(self, roads: list[list[int]], org_seats: int) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: bfs, iteration, queue, graph
        Failed attempt. Calculates as driving passangers from the capital outwards 
        starting from the closet cities. It overestimate the fuel result.
        It should start from the farthest cities.
        """
        if len(roads) == 0:
            return 0

        adjs = {}
        for u, v in roads:
            if u not in adjs:
                adjs[u] = set()
            if v not in adjs:
                adjs[v] = set()
            adjs[u].add(v)
            adjs[v].add(u)

        visited = set([0])

        fuel = 0

        def bfs(city, distance):
            nonlocal fuel
            queue = deque([(city, org_seats, distance)])
            
            while queue:
                for _ in range(len(queue)):
                    city, seats, distance = queue.popleft()

                    for next_city in adjs[city]:
                        if next_city not in visited:
                            visited.add(next_city)
                            fuel += 1
                            seats -= 1
                            if seats == 0:
                                fuel += distance
                                queue.append(
                                    (next_city, org_seats, distance + 1))
                            else:
                                queue.append(
                                    (next_city, seats - 1, distance + 1))

        bfs(0, 0)
        return fuel


print(Solution().minimumFuelCost([[0, 1]], 1) == 1)
print(Solution().minimumFuelCost([[0, 1], [0, 2]], 1) == 2)
print(Solution().minimumFuelCost([[0, 1], [1, 2]], 1) == 3)
print(Solution().minimumFuelCost([[0, 1], [1, 2]], 2) == 2)
print(Solution().minimumFuelCost([[0, 1], [0, 2], [2, 3]], 2) == 3)
print(Solution().minimumFuelCost([[0, 1], [1, 2], [2, 3]], 1) == 6)
print(Solution().minimumFuelCost([[0, 4], [0, 1], [1, 2]], 1) == 4)
print(Solution().minimumFuelCost([[0, 1], [0, 2], [0, 3]], 5) == 3)
print(Solution().minimumFuelCost([[3, 1], [3, 2], [1, 0], [0, 4], [0, 5], [4, 6]], 2) == 7)
print(Solution().minimumFuelCost([], 1) == 0)