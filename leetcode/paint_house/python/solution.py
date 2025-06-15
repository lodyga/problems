r"""
draft
                                .
                   /            |           \
                  17            2           17
              /       \     /      \      /     \
            16        5    16      5    16      16
          /    \    /  \   /  \   / \  /  \    /   \
        3      19  14  3  3   19 14  3  3  19 14   19
"""


class Solution:
    def minCost(self, houses: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: dp, bottom-up
        """
        cache = houses[0]

        for house in houses[1:]:
            cache = (
                house[0] + min(cache[1], cache[2]),
                house[1] + min(cache[0], cache[2]),
                house[2] + min(cache[0], cache[1])
            )

        return min(cache)


class Solution:
    def minCost(self, houses: list[list[int]]) -> int:
        """
        Time complexity: O(2^n)
        Auxiliary space complexity: O(n)
        Tags: brute-force, tle
        """
        def dfs(index: int, prev_house_ind: int) -> int:
            if index == len(houses):
                return 0

            return min(house + dfs(index + 1, house_ind) 
                       for house_ind, house in enumerate(houses[index])
                       if house_ind != prev_house_ind)
            
        return dfs(0, -1)


print(Solution().minCost([[1, 2, 3]]) == 1)
print(Solution().minCost([[1, 2, 3], [1, 4, 6]]) == 3)
print(Solution().minCost([[17, 2, 17], [16, 16, 5], [14, 3, 19]]) == 10)