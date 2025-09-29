class Solution:
    def rob(self, numbers: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: dp, bottom-up
        """
        if len(numbers) <= 3:
                return max(numbers)
        
        def rob2(numbers):
            cache = [0, 0]
            for index in reversed(range(len(numbers))):
                rob_house = numbers[index] + cache[1]
                skip_house = cache[0]
                cache[0], cache[1] = max(rob_house, skip_house), cache[0]
            return cache[0]
        return max(rob2(numbers[1:]), rob2(numbers[:-1]))


print(Solution().rob([2, 3, 2]) == 3)
print(Solution().rob([1, 2, 3, 1]) == 4)
print(Solution().rob([1, 2, 3]) == 3)
print(Solution().rob([1]) == 1)
print(Solution().rob([0, 0]) == 0)
print(Solution().rob([1, 3, 1, 3, 100]) == 103)