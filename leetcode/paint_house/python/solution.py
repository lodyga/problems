class Solution:
    def minCost(self, houses: list[list[int]]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            A: bottom-up, in-place method
        """
        def paint(idx, color):
            houses[idx][color] += min(
                houses[idx + 1][(color + 1) % 3],
                houses[idx + 1][(color + 2) % 3]
            )

        N = len(houses)

        for idx in range(N - 2, -1, -1):
            for color in range(3):
                paint(idx, color)

        return min(houses[0])


class Solution:
    def minCost(self, houses: list[list[int]]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            A: bottom-up
        """
        cache = houses[0]

        for idx in range(1, len(houses)):
            house = houses[idx]
            cache = (
                house[0] + min(cache[1], cache[2]),
                house[1] + min(cache[0], cache[2]),
                house[2] + min(cache[0], cache[1])
            )

        return min(cache)


class Solution:
    def minCost(self, houses: list[list[int]]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: hash map
            A: top-down
        """
        memo = {
            (len(houses), 0): 0, 
            (len(houses), 1): 0, 
            (len(houses), 2): 0
        }
        
        def dfs(idx: int, prev_house_ind: int) -> int:
            if (idx, prev_house_ind) in memo:
                return memo[(idx, prev_house_ind)]
            
            cost = 10**9 + 7
        
            for house_ind, house in enumerate(houses[idx]):
                if house_ind != prev_house_ind:
                    cost = min(cost, house + dfs(idx + 1, house_ind))
        
            memo[(idx, prev_house_ind)] = cost
        
            return cost

        return dfs(0, -1)


print(Solution().minCost([[1, 2, 3]]) == 1)
print(Solution().minCost([[1, 2, 3], [1, 4, 6]]) == 3)
print(Solution().minCost([[17, 2, 17], [16, 16, 5], [14, 3, 19]]) == 10)
