class Solution:
    def maximumCandies(self, candies: list[int], child_count: int) -> int:
        """
        Time complexity: O(nlogn)
        Auxiliary space complexity: O(1)
        Tags: binary search
        """
        if child_count > sum(candies):
            return 0
        
        left = 1
        right = max(candies)
        candy_per_child = 0

        while left <= right:
            # estimated candy per child
            middle = (left + right) // 2
            happy_child_count = 0

            for candy in candies:
                if candy >= middle:
                    happy_child_count += candy // middle
                    if happy_child_count >= child_count:
                        break
            
            if happy_child_count >= child_count:
                left = middle + 1
                candy_per_child = middle
            else:
                right = middle - 1
            
        return candy_per_child


print(Solution().maximumCandies([5, 8, 6], 3) == 5)
print(Solution().maximumCandies([2, 5], 11) == 0)
print(Solution().maximumCandies([5, 8, 6], 4) == 4)
print(Solution().maximumCandies([5, 8, 6], 5) == 3)
print(Solution().maximumCandies([4, 7, 5], 4) == 3)
print(Solution().maximumCandies([1, 2, 3, 4, 10], 5) == 3)