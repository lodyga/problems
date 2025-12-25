class Solution:
    def minCost(self, houses: list[list[int]]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: 
            A: bottom-up
        """
        cache = houses[0]

        for index in range(1, len(houses)):
            house = houses[index]
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
        memo = {(len(houses), 0): 0, (len(houses), 1): 0, (len(houses), 2): 0}
        
        def dfs(index: int, prev_house_ind: int) -> int:
            if (index, prev_house_ind) in memo:
                return memo[(index, prev_house_ind)]
            
            cost = 10**9 + 7
            for house_ind, house in enumerate(houses[index]):
                if house_ind != prev_house_ind:
                    cost = min(cost, house + dfs(index + 1, house_ind))
            memo[(index, prev_house_ind)] = cost
            return cost

        return dfs(0, -1)


print(Solution().minCost([[1, 2, 3]]) == 1)
print(Solution().minCost([[1, 2, 3], [1, 4, 6]]) == 3)
print(Solution().minCost([[17, 2, 17], [16, 16, 5], [14, 3, 19]]) == 10)
