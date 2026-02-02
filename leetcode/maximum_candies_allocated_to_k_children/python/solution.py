class Solution:
    def maximumCandies(self, candies: list[int], k: int) -> int:
        """
        Time complexity: O(nlogn)
        Auxiliary space complexity: O(1)
        Tags:
            A: binary search
        """
        left = 1
        right = min(max(candies), sum(candies) // k)
        res = 0

        while left <= right:
            # Estimated candies per child.
            mid = (left + right) // 2
            happy = 0
            
            for candy in candies:
                happy += candy // mid
                if happy >= k:
                    break

            if happy >= k:
                left = mid + 1
                res = mid
            else:
                right = mid - 1

        return res


print(Solution().maximumCandies([5, 8, 6], 3) == 5)
print(Solution().maximumCandies([2, 5], 11) == 0)
print(Solution().maximumCandies([5, 8, 6], 4) == 4)
print(Solution().maximumCandies([5, 8, 6], 5) == 3)
print(Solution().maximumCandies([4, 7, 5], 4) == 3)
print(Solution().maximumCandies([1, 2, 3, 4, 10], 5) == 3)
