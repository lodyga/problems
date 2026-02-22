class Solution:
    def minimumFuelCost(self, roads: list[list[int]], seats: int) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: hash map, array
            A: DFS
            Model: graph
        """
        if len(roads) == 0:
            return 0

        adjs = {}
        fuel = 0

        for u, v in roads:
            if u not in adjs:
                adjs[u] = []
            if v not in adjs:
                adjs[v] = []
            adjs[u].append(v)
            adjs[v].append(u)

        def dfs(city, prev_city):
            nonlocal fuel
            total_passengers = 1

            for next_city in adjs[city]:
                if next_city == prev_city:
                    continue
                
                passengers = dfs(next_city, city)
                # fuel += math.ceil(passengers / seats)
                fuel += ((passengers - 1) // seats) + 1
                total_passengers += passengers

            return total_passengers

        dfs(0, -1)
        return fuel


print(Solution().minimumFuelCost([[0, 1]], 1) == 1)
print(Solution().minimumFuelCost([[0, 1], [0, 2]], 1) == 2)
print(Solution().minimumFuelCost([[0, 1], [1, 2]], 1) == 3)
print(Solution().minimumFuelCost([[0, 1], [1, 2]], 2) == 2)
print(Solution().minimumFuelCost([[0, 1], [0, 2], [2, 3]], 2) == 3)
print(Solution().minimumFuelCost([[0, 1], [1, 2], [2, 3]], 1) == 6)
print(Solution().minimumFuelCost([[0, 3], [0, 1], [1, 2]], 1) == 4)
print(Solution().minimumFuelCost([[0, 1], [0, 2], [1, 3], [1, 4]], 5) == 4)
print(Solution().minimumFuelCost([[0, 1], [0, 2], [0, 3]], 5) == 3)
print(Solution().minimumFuelCost([[3, 1], [3, 2], [1, 0], [0, 4], [0, 5], [4, 6]], 2) == 7)
print(Solution().minimumFuelCost([], 1) == 0)
