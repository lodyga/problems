class Solution:
    def rob(self, numbers: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: dp, bottom-up
        """
        if len(numbers) <= 3:
                return max(numbers)
        
        def rob_inner(numbers: list[int]) -> int:
            if len(numbers) <= 2:
                return max(numbers)

            cache = (numbers[0], max(numbers[:2]))

            for number in numbers[2:]:
                cache = (cache[1], max(cache[0] + number, cache[1]))

            return cache[1]
        
        return max(rob_inner(numbers[:-1]), rob_inner(numbers[1:]))


print(Solution().rob([2, 3, 2]) == 3)
print(Solution().rob([1, 2, 3, 1]) == 4)
print(Solution().rob([1, 2, 3]) == 3)
print(Solution().rob([1]) == 1)
print(Solution().rob([0, 0]) == 0)
print(Solution().rob([1, 3, 1, 3, 100]) == 103)