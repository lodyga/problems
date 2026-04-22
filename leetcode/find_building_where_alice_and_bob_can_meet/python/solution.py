class Solution:
    def leftmostBuildingQueries(self, heights: list[int], queries: list[list[int]]) -> list[int]:
        """
        Time complexity: O(q*n)
        Auxiliary space complexity: O(n2)
        Tags:
            DS: list
            A: iteration
        """
        res = []
        N = len(heights)
        cache = {}

        for building_a, building_b in queries:
            if (building_a, building_b) in cache:
                res.append(cache[(building_a, building_b)])

            if building_a > building_b:
                building_a, building_b = building_b, building_a

            if (
                building_a == building_b or 
                heights[building_a] < heights[building_b]
            ):
                res.append(building_b)
                cache[(building_a, building_b)] = res[-1]
                continue

            index = max(building_a, building_b) + 1
            res.append(-1)

            while index < N:
                if (
                    heights[building_a] < heights[index] and
                    heights[building_b] < heights[index]
                ):
                    res.pop()
                    res.append(index)
                    break
                    
                index += 1

            cache[(building_a, building_b)] = res[-1]

        return res


class Solution:
    def leftmostBuildingQueries(self, heights: list[int], queries: list[list[int]]) -> list[int]:
        import heapq
        """
        Time complexity: O(q*n)
        Auxiliary space complexity: O(n2)
        Tags:
            DS: list
            A: iteration
        """
        res = [-1] * len(queries)
        N = len(heights)
        # heap([(right building index, max of two building height, query index)])
        building_heap = []

        for index, (building_a, building_b) in enumerate(queries):
            right_building = max(building_a, building_b)
            higher_building_height = max(heights[building_a], heights[building_b])
            heapq.heappush(building_heap, (right_building, higher_building_height, index))

        while building_heap:


        return res


print(Solution().leftmostBuildingQueries([6, 4, 8, 5, 2, 7], [[0, 1], [0, 3], [2, 4], [3, 4], [2, 2]]), [2, 5, -1, 5, 2])
print(Solution().leftmostBuildingQueries([5, 3, 8, 2, 6, 1, 4, 6], [[0, 7], [3, 5], [5, 2], [3, 0], [1, 6]]), [7, 6, -1, 4, 6])
print(Solution().leftmostBuildingQueries([6, 4, 8, 5, 2, 7], [[0, 1], [0, 3], [2, 4], [3, 4], [2, 2]]) == [2, 5, -1, 5, 2])
print(Solution().leftmostBuildingQueries([5, 3, 8, 2, 6, 1, 4, 6], [[0, 7], [3, 5], [5, 2], [3, 0], [1, 6]]) == [7, 6, -1, 4, 6])
