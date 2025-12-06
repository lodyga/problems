class Solution:
    def rob(self, houses: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: 
            A: greedy
        """
        if len(houses) <= 3:
            return max(houses)

        def rob2(houses):
            cache = [0, 0]
            for index in range(len(houses) - 1, -1, -1):
                house = houses[index]
                skip_house = cache[0]
                rob_house = house + cache[1]
                cache[0], cache[1] = max(skip_house, rob_house), cache[0]
            return cache[0]

        return max(rob2(houses[: -1]), rob2(houses[1:]))


print(Solution().rob([2, 3, 2]) == 3)
print(Solution().rob([1, 2, 3, 1]) == 4)
print(Solution().rob([1, 2, 3]) == 3)
print(Solution().rob([1]) == 1)
print(Solution().rob([0, 0]) == 0)
print(Solution().rob([1, 3, 1, 3, 100]) == 103)
